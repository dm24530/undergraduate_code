# !/usr/bin/env python
# _*_ coding:utf-8 _*_
import pymysql
import sys
import os
from datetime import datetime
from configparser import ConfigParser
sys.path.insert(0, os.path.split(os.path.split(os.path.realpath(__file__))[0])[0] + os.sep)
import mysql_config
import data_query
import data_define
import data_manipulate
import extract_earth_element
import sql
def main_Normal():
	config_parser = ConfigParser()
	config_parser.read('earth_element_system.config')
	config_total_pages = config_parser.getint('systemconf', 'db_total_pages')
	config_total_items = config_parser.getint('systemconf', 'db_total_items')
	config_db_constructed_datetime = config_parser.get('systemconf', 'db_constructed_datetime')
	config_db_database = config_parser.get('systemconf', 'db_database')
	config_db_character_property = config_parser.get('systemconf', 'db_character_property')
	config_db_auto_rebuilt_intervl = config_parser.get('systemconf', 'db_auto_rebuilt_intervl')
	config_db_table_pageLog = config_parser.get('systemconf', 'db_table_pageLog')
	config_db_table_earthNormal = config_parser.get('systemconf', 'db_table_earthNormal')
	db_exist_flag, db_query_result = data_query.query_database()
	if db_exist_flag == 2:
		tables_exist_flag, tables_query_result = data_query.query_tableNames_for_database()
		if tables_exist_flag == 2:
			if (sql.db_table_earthNormal in tables_query_result) and (sql.db_table_pageLog in tables_query_result):
				print('Update earthElementSync')
				totalPages_flag, total_pages, total_items = extract_earth_element.obtainTotalPages()
				if totalPages_flag == 1:
					print('在线汉语字典（http://xh.5156edu.com/）的网页组织方式未改变！')
					if (total_pages == config_total_pages) and (total_items == config_total_items):
						pageLog_count_flag, pageLog_rowcount_info = data_query.count_items_for_pageLog()
						if pageLog_count_flag == 1:
							pageLog_rowcount = pageLog_rowcount_info
							if total_pages == pageLog_rowcount:
								if len(config_db_constructed_datetime) == 19:
									last_db_constructed_datetime = datetime.strptime(config_db_constructed_datetime, '%Y-%m-%d %H:%M:%S')
									datetime_now_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
									datetime_delta = datetime.strptime(datetime_now_str, '%Y-%m-%d %H:%M:%S') - last_db_constructed_datetime
									datetime_delta_seconds = datetime_delta.days * 24 * 60 * 60 + datetime_delta.seconds
									if datetime_delta_seconds < 604800:
										print('earthElementSync updated')
										sys.exit(0)
									else:
										print('距离首次完全将属性为{}的汉字全部存储到数据库{}到时间已经超过{}秒'.format(config_db_character_property, config_db_database, config_db_auto_rebuilt_intervl))
										print('现在开始自动重建数据库{}'.format(config_db_database))
										print('Dropping database {}'.format(config_db_database))
										drop_database_flag, drop_database_error_infomation = data_define.drop_database()
										if drop_database_flag == 1:
											print(drop_database_error_infomation)
											create_database_flag, create_database_error_infomation = data_define.create_database()
											if create_database_flag == 1:
												print(create_database_error_infomation)
												create_pageLog_flag, create_pageLog_error_infomation = data_define.create_table_pageLog()
												if create_pageLog_flag == 1:
													print(create_pageLog_error_infomation)
													create_earthNormal_flag, create_earthNormal_error_infomation = data_define.create_table_earthNormal()
													if create_earthNormal_flag == 1:
														print(create_earthNormal_error_infomation)
														totalPages_flag, total_pages, total_items = extract_earth_element.obtainTotalPages()
														if totalPages_flag == 1:
															print('在线汉语字典（http://xh.5156edu.com/）的网页组织方式未改变！')
															config_parser.set('systemconf', 'db_total_pages', str(total_pages))
															config_parser.set('systemconf', 'db_total_items', str(total_items))
															config_parser.write(open('earth_element_system.config', 'w+'), 'w')
															totalPages_urls = []
															for i in range(total_pages):
																generate_page_url = extract_earth_element.generatePageUrl(i + 1)
																totalPages_urls.append(generate_page_url)
															for page_url_index in range(total_pages):
																page_url = totalPages_urls[page_url_index]
																pageContent_flag, character_list = extract_earth_element.getPageContent(page_url)
																if pageContent_flag == 1:
																	earthNormal_executemany_flag, error_information = data_manipulate.insert_by_executemany_for_table_Normal(character_list)
																	if earthNormal_executemany_flag == 1:
																		print('The page content of {} has been inserted into database successfully.'.format(page_url))
																		page_rank = page_url_index + 1
																		page_written_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
																		insert_value = (page_rank, page_url, page_written_datetime)
																		pageLog_execute_flag, pageLog_execute_error_information = data_manipulate.insert_by_execute_for_table_pageLog(insert_value)
																		if pageLog_execute_flag == 1:
																			print('The log has been written to the database corresponding to the page content.')
																		elif pageLog_execute_flag == 0:
																			print(pageLog_execute_error_information)
																			sys.exit(0)
																		elif pageLog_execute_flag == -1:
																			print(pageLog_execute_error_information)
																			sys.exit(0)
																	elif earthNormal_executemany_flag == 0:
																		print(error_information)
																		sys.exit(0)
																	elif earthNormal_executemany_flag == -1:
																		print(error_information)
																		sys.exit(0)
																elif pageContent_flag == -1:
																	print('您本机到链接为:{}的网络页面网络不可达！'.format(page_url))
																	print('请确保您的本机已经联网，然后再重写启动系统！')
																	sys.exit(0)
															config_db_constructed_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
															print(config_db_constructed_datetime)
															config_parser.set('systemconf', 'db_constructed_datetime', config_db_constructed_datetime)
															config_parser.write(open('earth_element_system.config', 'w+'), 'w')
															print('earthElementSync updated')
															sys.exit(0)
														elif totalPages_flag == 0:
															print('在线汉语字典（http://xh.5156edu.com/）的网页组织方式已经改变！')
															print('即：首页 上一页 下一页 尾页 页次：M/N 每页：P 本类资料：Q的组织方式改变！')
															print('请根据在线汉语字典的新的网页组织方式来重构系统！')
															sys.exit(0)
														elif totalPages_flag == -1:
															print('您本机的网络到在线汉语字典（http://xh.5156edu.com/）的网络不可达！')
															print('请确保您的本机已经联网，然后再重写启动系统！')
															sys.exit(0)
													elif create_earthNormal_flag == 0:
														print(create_earthNormal_error_infomation)
														sys.exit(0)
													elif create_earthNormal_flag == -1:
														print(create_earthNormal_error_infomation)
														sys.exit(0)
												elif create_pageLog_flag == 0:
													print(create_pageLog_error_infomation)
													sys.exit(0)
												elif create_pageLog_flag == -1:
													print(create_pageLog_error_infomation)
													sys.exit(0)
											elif create_database_flag == 0:
												print(create_database_error_infomation)
												sys.exit(0)
											elif create_database_flag == -1:
												print(create_database_error_infomation)
												sys.exit(0)
										elif drop_database_flag == 0:
											print(drop_database_error_infomation)
											sys.exit(0)
										elif drop_database_flag == -1:
											print(drop_database_error_infomation)
											sys.exit(0)
								else:
									config_db_constructed_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
									print(config_db_constructed_datetime)
									config_parser.set('systemconf', 'db_constructed_datetime', config_db_constructed_datetime)
									config_parser.write(open('earth_element_system.config', 'w+'), 'w')
									print('earthElementSync updated')
									sys.exit(0)
							elif total_pages > pageLog_rowcount:
								totalPages_urls = []
								for i in range(pageLog_rowcount, total_pages):
									generate_page_url = extract_earth_element.generatePageUrl(i + 1)
									totalPages_urls.append(generate_page_url)
								new_range = total_pages - pageLog_rowcount
								for page_url_index in range(new_range):
									page_url = totalPages_urls[page_url_index]
									pageContent_flag, character_list = extract_earth_element.getPageContent(page_url)
									if pageContent_flag == 1:
										earthNormal_executemany_flag, error_information = data_manipulate.insert_by_executemany_for_table_Normal(character_list)
										if earthNormal_executemany_flag == 1:
											print('The page content of {} has been inserted into database successfully.'.format(page_url))
											page_rank = page_url_index + pageLog_rowcount + 1
											page_written_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
											insert_value = (page_rank, page_url, page_written_datetime)
											pageLog_execute_flag, pageLog_execute_error_information = data_manipulate.insert_by_execute_for_table_pageLog(insert_value)
											if pageLog_execute_flag == 1:
												print('The log has been written to the database corresponding to the page content.')
											elif pageLog_execute_flag == 0:
												print(pageLog_execute_error_information)
												sys.exit(0)
											elif pageLog_execute_flag == -1:
												print(pageLog_execute_error_information)
												sys.exit(0)
										elif earthNormal_executemany_flag == 0:
											print(error_information)
											sys.exit(0)
										elif earthNormal_executemany_flag == -1:
											print(error_information)
											sys.exit(0)
									elif pageContent_flag == -1:
										print('您本机到链接为:{}的网络页面网络不可达！'.format(page_url))
										print('请确保您的本机已经联网，然后再重写启动系统！')
										sys.exit(0)
								config_db_constructed_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
								print(config_db_constructed_datetime)
								config_parser.set('systemconf', 'db_constructed_datetime', config_db_constructed_datetime)
								config_parser.write(open('earth_element_system.config', 'w+'), 'w')
								print('earthElementSync updated')
								sys.exit(0)
						elif pageLog_count_flag == 0:
							print(pageLog_rowcount_info)
							sys.exit(0)
						elif pageLog_count_flag == -1:
							print(pageLog_rowcount_info)
							sys.exit(0)
					else:
						print('在线汉语字典（http://xh.5156edu.com/）的网页上的内容或页面组织结构有改变！')
						print('或者，人为修改系统配置文件earth_element_system.config中的db_total_pages 或者db_total_items的值')
						print('The system will execute to drop the database and rebuild it')
						print('Dropping database {}'.format(config_db_database))
						drop_database_flag, drop_database_error_infomation = data_define.drop_database()
						if drop_database_flag == 1:
							print(drop_database_error_infomation)
							create_database_flag, create_database_error_infomation = data_define.create_database()
							if create_database_flag == 1:
								print(create_database_error_infomation)
								create_pageLog_flag, create_pageLog_error_infomation = data_define.create_table_pageLog()
								if create_pageLog_flag == 1:
									print(create_pageLog_error_infomation)
									create_earthNormal_flag, create_earthNormal_error_infomation = data_define.create_table_earthNormal()
									if create_earthNormal_flag == 1:
										print(create_earthNormal_error_infomation)
										totalPages_flag, total_pages, total_items = extract_earth_element.obtainTotalPages()
										if totalPages_flag == 1:
											print('在线汉语字典（http://xh.5156edu.com/）的网页组织方式未改变！')
											config_parser.set('systemconf', 'db_total_pages', str(total_pages))
											config_parser.set('systemconf', 'db_total_items', str(total_items))
											config_parser.write(open('earth_element_system.config', 'w+'), 'w')
											totalPages_urls = []
											for i in range(total_pages):
												generate_page_url = extract_earth_element.generatePageUrl(i + 1)
												totalPages_urls.append(generate_page_url)
											for page_url_index in range(total_pages):
												page_url = totalPages_urls[page_url_index]
												pageContent_flag, character_list = extract_earth_element.getPageContent(page_url)
												if pageContent_flag == 1:
													earthNormal_executemany_flag, error_information = data_manipulate.insert_by_executemany_for_table_Normal(character_list)
													if earthNormal_executemany_flag == 1:
														print('The page content of {} has been inserted into database successfully.'.format(page_url))
														page_rank = page_url_index + 1
														page_written_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
														insert_value = (page_rank, page_url, page_written_datetime)
														pageLog_execute_flag, pageLog_execute_error_information = data_manipulate.insert_by_execute_for_table_pageLog(insert_value)
														if pageLog_execute_flag == 1:
															print('The log has been written to the database corresponding to the page content.')
														elif pageLog_execute_flag == 0:
															print(pageLog_execute_error_information)
															sys.exit(0)
														elif pageLog_execute_flag == -1:
															print(pageLog_execute_error_information)
															sys.exit(0)
													elif earthNormal_executemany_flag == 0:
														print(error_information)
														sys.exit(0)
													elif earthNormal_executemany_flag == -1:
														print(error_information)
														sys.exit(0)
												elif pageContent_flag == -1:
													print('您本机到链接为:{}的网络页面网络不可达！'.format(page_url))
													print('请确保您的本机已经联网，然后再重写启动系统！')
													sys.exit(0)
											config_db_constructed_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
											print(config_db_constructed_datetime)
											config_parser.set('systemconf', 'db_constructed_datetime', config_db_constructed_datetime)
											config_parser.write(open('earth_element_system.config', 'w+'), 'w')
											print('earthElementSync updated')
											sys.exit(0)
										elif totalPages_flag == 0:
											print('在线汉语字典（http://xh.5156edu.com/）的网页组织方式已经改变！')
											print('即：首页 上一页 下一页 尾页 页次：M/N 每页：P 本类资料：Q的组织方式改变！')
											print('请根据在线汉语字典的新的网页组织方式来重构系统！')
											sys.exit(0)
										elif totalPages_flag == -1:
											print('您本机的网络到在线汉语字典（http://xh.5156edu.com/）的网络不可达！')
											print('请确保您的本机已经联网，然后再重写启动系统！')
											sys.exit(0)
									elif create_earthNormal_flag == 0:
										print(create_earthNormal_error_infomation)
										sys.exit(0)
									elif create_earthNormal_flag == -1:
										print(create_earthNormal_error_infomation)
										sys.exit(0)
								elif create_pageLog_flag == 0:
									print(create_pageLog_error_infomation)
									sys.exit(0)
								elif create_pageLog_flag == -1:
									print(create_pageLog_error_infomation)
									sys.exit(0)
							elif create_database_flag == 0:
								print(create_database_error_infomation)
								sys.exit(0)
							elif create_database_flag == -1:
								print(create_database_error_infomation)
								sys.exit(0)
						elif drop_database_flag == 0:
							print(drop_database_error_infomation)
							sys.exit(0)
						elif drop_database_flag == -1:
							print(drop_database_error_infomation)
							sys.exit(0)
				elif totalPages_flag == 0:
					print('在线汉语字典（http://xh.5156edu.com/）的网页组织方式已经改变！')
					print('即：首页 上一页 下一页 尾页 页次：M/N 每页：P 本类资料：Q的组织方式改变！')
					print('请根据在线汉语字典的新的网页组织方式来重构系统！')
					sys.exit(0)
				elif totalPages_flag == -1:
					print('您本机的网络到在线汉语字典（http://xh.5156edu.com/）的网络不可达！')
					print('请确保您的本机已经联网，然后再重写启动系统！')
					sys.exit(0)
			elif (sql.db_table_earthNormal not in tables_query_result) and (sql.db_table_pageLog not in tables_query_result):
				create_pageLog_flag, create_pageLog_error_infomation = data_define.create_table_pageLog()
				if create_pageLog_flag == 1:
					print(create_pageLog_error_infomation)
					create_earthNormal_flag, create_earthNormal_error_infomation = data_define.create_table_earthNormal()
					if create_earthNormal_flag == 1:
						print(create_earthNormal_error_infomation)
						totalPages_flag, total_pages, total_items = extract_earth_element.obtainTotalPages()
						if totalPages_flag == 1:
							print('在线汉语字典（http://xh.5156edu.com/）的网页组织方式未改变！')
							config_parser.set('systemconf', 'db_total_pages', str(total_pages))
							config_parser.set('systemconf', 'db_total_items', str(total_items))
							config_parser.write(open('earth_element_system.config', 'w+'), 'w')
							totalPages_urls = []
							for i in range(total_pages):
								generate_page_url = extract_earth_element.generatePageUrl(i + 1)
								totalPages_urls.append(generate_page_url)
							for page_url_index in range(total_pages):
								page_url = totalPages_urls[page_url_index]
								pageContent_flag, character_list = extract_earth_element.getPageContent(page_url)
								if pageContent_flag == 1:
									earthNormal_executemany_flag, error_information = data_manipulate.insert_by_executemany_for_table_Normal(character_list)
									if earthNormal_executemany_flag == 1:
										print('The page content of {} has been inserted into database successfully.'.format(page_url))
										page_rank = page_url_index + 1
										page_written_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
										insert_value = (page_rank, page_url, page_written_datetime)
										pageLog_execute_flag, pageLog_execute_error_information = data_manipulate.insert_by_execute_for_table_pageLog(insert_value)
										if pageLog_execute_flag == 1:
											print('The log has been written to the database corresponding to the page content.')
										elif pageLog_execute_flag == 0:
											print(pageLog_execute_error_information)
											sys.exit(0)
										elif pageLog_execute_flag == -1:
											print(pageLog_execute_error_information)
											sys.exit(0)
									elif earthNormal_executemany_flag == 0:
										print(error_information)
										sys.exit(0)
									elif earthNormal_executemany_flag == -1:
										print(error_information)
										sys.exit(0)
								elif pageContent_flag == -1:
									print('您本机到链接为:{}的网络页面网络不可达！'.format(page_url))
									print('请确保您的本机已经联网，然后再重写启动系统！')
									sys.exit(0)
							config_db_constructed_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
							print(config_db_constructed_datetime)
							config_parser.set('systemconf', 'db_constructed_datetime', config_db_constructed_datetime)
							config_parser.write(open('earth_element_system.config', 'w+'), 'w')
							print('earthElementSync updated')
							sys.exit(0)
						elif totalPages_flag == 0:
							print('在线汉语字典（http://xh.5156edu.com/）的网页组织方式已经改变！')
							print('即：首页 上一页 下一页 尾页 页次：M/N 每页：P 本类资料：Q的组织方式改变！')
							print('请根据在线汉语字典的新的网页组织方式来重构系统！')
							sys.exit(0)
						elif totalPages_flag == -1:
							print('您本机的网络到在线汉语字典（http://xh.5156edu.com/）的网络不可达！')
							print('请确保您的本机已经联网，然后再重写启动系统！')
							sys.exit(0)
					elif create_earthNormal_flag == 0:
						print(create_earthNormal_error_infomation)
						sys.exit(0)
					elif create_earthNormal_flag == -1:
						print(create_earthNormal_error_infomation)
						sys.exit(0)
				elif create_pageLog_flag == 0:
					print(create_pageLog_error_infomation)
					sys.exit(0)
				elif create_pageLog_flag == -1:
					print(create_pageLog_error_infomation)
					sys.exit(0)
			elif (sql.db_table_earthNormal not in tables_query_result):
				create_earthNormal_flag, create_earthNormal_error_infomation = data_define.create_table_earthNormal()
				if create_earthNormal_flag == 1:
					print(create_earthNormal_error_infomation)
					totalPages_flag, total_pages, total_items = extract_earth_element.obtainTotalPages()
					if totalPages_flag == 1:
						print('在线汉语字典（http://xh.5156edu.com/）的网页组织方式未改变！')
						config_parser.set('systemconf', 'db_total_pages', str(total_pages))
						config_parser.set('systemconf', 'db_total_items', str(total_items))
						config_parser.write(open('earth_element_system.config', 'w+'), 'w')
						totalPages_urls = []
						for i in range(total_pages):
							generate_page_url = extract_earth_element.generatePageUrl(i + 1)
							totalPages_urls.append(generate_page_url)
						for page_url_index in range(total_pages):
							page_url = totalPages_urls[page_url_index]
							pageContent_flag, character_list = extract_earth_element.getPageContent(page_url)
							if pageContent_flag == 1:
								earthNormal_executemany_flag, error_information = data_manipulate.insert_by_executemany_for_table_Normal(character_list)
								if earthNormal_executemany_flag == 1:
									print('The page content of {} has been inserted into database successfully.'.format(page_url))
									page_rank = page_url_index + 1
									page_written_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
									insert_value = (page_rank, page_url, page_written_datetime)
									pageLog_execute_flag, pageLog_execute_error_information = data_manipulate.insert_by_execute_for_table_pageLog(insert_value)
									if pageLog_execute_flag == 1:
										print('The log has been written to the database corresponding to the page content.')
									elif pageLog_execute_flag == 0:
										print(pageLog_execute_error_information)
										sys.exit(0)
									elif pageLog_execute_flag == -1:
										print(pageLog_execute_error_information)
										sys.exit(0)
								elif earthNormal_executemany_flag == 0:
									print(error_information)
									sys.exit(0)
								elif earthNormal_executemany_flag == -1:
									print(error_information)
									sys.exit(0)
							elif pageContent_flag == -1:
								print('您本机到链接为:{}的网络页面网络不可达！'.format(page_url))
								print('请确保您的本机已经联网，然后再重写启动系统！')
								sys.exit(0)
						config_db_constructed_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
						print(config_db_constructed_datetime)
						config_parser.set('systemconf', 'db_constructed_datetime', config_db_constructed_datetime)
						config_parser.write(open('earth_element_system.config', 'w+'), 'w')
						print('earthElementSync updated')
						sys.exit(0)
					elif totalPages_flag == 0:
						print('在线汉语字典（http://xh.5156edu.com/）的网页组织方式已经改变！')
						print('即：首页 上一页 下一页 尾页 页次：M/N 每页：P 本类资料：Q的组织方式改变！')
						print('请根据在线汉语字典的新的网页组织方式来重构系统！')
						sys.exit(0)
					elif totalPages_flag == -1:
						print('您本机的网络到在线汉语字典（http://xh.5156edu.com/）的网络不可达！')
						print('请确保您的本机已经联网，然后再重写启动系统！')
						sys.exit(0)
				elif create_earthNormal_flag == 0:
					print(create_earthNormal_error_infomation)
					sys.exit(0)
				elif create_earthNormal_flag == -1:
					print(create_earthNormal_error_infomation)
					sys.exit(0)
			elif (sql.db_table_pageLog not in tables_query_result):
				create_pageLog_flag, create_pageLog_error_infomation = data_define.create_table_pageLog()
				if create_pageLog_flag == 1:
					print(create_pageLog_error_infomation)
					totalPages_flag, total_pages, total_items = extract_earth_element.obtainTotalPages()
					if totalPages_flag == 1:
						print('在线汉语字典（http://xh.5156edu.com/）的网页组织方式未改变！')
						config_parser.set('systemconf', 'db_total_pages', str(total_pages))
						config_parser.set('systemconf', 'db_total_items', str(total_items))
						config_parser.write(open('earth_element_system.config', 'w+'), 'w')
						totalPages_urls = []
						for i in range(total_pages):
							generate_page_url = extract_earth_element.generatePageUrl(i + 1)
							totalPages_urls.append(generate_page_url)
						for page_url_index in range(total_pages):
							page_url = totalPages_urls[page_url_index]
							pageContent_flag, character_list = extract_earth_element.getPageContent(page_url)
							if pageContent_flag == 1:
								earthNormal_executemany_flag, error_information = data_manipulate.insert_by_executemany_for_table_Normal(character_list)
								if earthNormal_executemany_flag == 1:
									print('The page content of {} has been inserted into database successfully.'.format(page_url))
									page_rank = page_url_index + 1
									page_written_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
									insert_value = (page_rank, page_url, page_written_datetime)
									pageLog_execute_flag, pageLog_execute_error_information = data_manipulate.insert_by_execute_for_table_pageLog(insert_value)
									if pageLog_execute_flag == 1:
										print('The log has been written to the database corresponding to the page content.')
									elif pageLog_execute_flag == 0:
										print(pageLog_execute_error_information)
										sys.exit(0)
									elif pageLog_execute_flag == -1:
										print(pageLog_execute_error_information)
										sys.exit(0)
								elif earthNormal_executemany_flag == 0:
									print(error_information)
									sys.exit(0)
								elif earthNormal_executemany_flag == -1:
									print(error_information)
									sys.exit(0)
							elif pageContent_flag == -1:
								print('您本机到链接为:{}的网络页面网络不可达！'.format(page_url))
								print('请确保您的本机已经联网，然后再重写启动系统！')
								sys.exit(0)
						config_db_constructed_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
						print(config_db_constructed_datetime)
						config_parser.set('systemconf', 'db_constructed_datetime', config_db_constructed_datetime)
						config_parser.write(open('earth_element_system.config', 'w+'), 'w')
						print('earthElementSync updated')
						sys.exit(0)
					elif totalPages_flag == 0:
						print('在线汉语字典（http://xh.5156edu.com/）的网页组织方式已经改变！')
						print('即：首页 上一页 下一页 尾页 页次：M/N 每页：P 本类资料：Q的组织方式改变！')
						print('请根据在线汉语字典的新的网页组织方式来重构系统！')
						sys.exit(0)
					elif totalPages_flag == -1:
						print('您本机的网络到在线汉语字典（http://xh.5156edu.com/）的网络不可达！')
						print('请确保您的本机已经联网，然后再重写启动系统！')
						sys.exit(0)
				elif create_pageLog_flag == 0:
					print(create_pageLog_error_infomation)
					sys.exit(0)
				elif create_pageLog_flag == -1:
					print(create_pageLog_error_infomation)
					sys.exit(0)
		elif tables_exist_flag == 1:
			create_pageLog_flag, create_pageLog_error_infomation = data_define.create_table_pageLog()
			if create_pageLog_flag == 1:
				print(create_pageLog_error_infomation)
				create_earthNormal_flag, create_earthNormal_error_infomation = data_define.create_table_earthNormal()
				if create_earthNormal_flag == 1:
					print(create_earthNormal_error_infomation)
					totalPages_flag, total_pages, total_items = extract_earth_element.obtainTotalPages()
					if totalPages_flag == 1:
						print('在线汉语字典（http://xh.5156edu.com/）的网页组织方式未改变！')
						config_parser.set('systemconf', 'db_total_pages', str(total_pages))
						config_parser.set('systemconf', 'db_total_items', str(total_items))
						config_parser.write(open('earth_element_system.config', 'w+'), 'w')
						totalPages_urls = []
						for i in range(total_pages):
							generate_page_url = extract_earth_element.generatePageUrl(i + 1)
							totalPages_urls.append(generate_page_url)
						for page_url_index in range(total_pages):
							page_url = totalPages_urls[page_url_index]
							pageContent_flag, character_list = extract_earth_element.getPageContent(page_url)
							if pageContent_flag == 1:
								earthNormal_executemany_flag, error_information = data_manipulate.insert_by_executemany_for_table_Normal(character_list)
								if earthNormal_executemany_flag == 1:
									print('The page content of {} has been inserted into database successfully.'.format(page_url))
									page_rank = page_url_index + 1
									page_written_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
									insert_value = (page_rank, page_url, page_written_datetime)
									pageLog_execute_flag, pageLog_execute_error_information = data_manipulate.insert_by_execute_for_table_pageLog(insert_value)
									if pageLog_execute_flag == 1:
										print('The log has been written to the database corresponding to the page content.')
									elif pageLog_execute_flag == 0:
										print(pageLog_execute_error_information)
										sys.exit(0)
									elif pageLog_execute_flag == -1:
										print(pageLog_execute_error_information)
										sys.exit(0)
								elif earthNormal_executemany_flag == 0:
									print(error_information)
									sys.exit(0)
								elif earthNormal_executemany_flag == -1:
									print(error_information)
									sys.exit(0)
							elif pageContent_flag == -1:
								print('您本机到链接为:{}的网络页面网络不可达！'.format(page_url))
								print('请确保您的本机已经联网，然后再重写启动系统！')
								sys.exit(0)
						config_db_constructed_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
						print(config_db_constructed_datetime)
						config_parser.set('systemconf', 'db_constructed_datetime', config_db_constructed_datetime)
						config_parser.write(open('earth_element_system.config', 'w+'), 'w')
						print('earthElementSync updated')
						sys.exit(0)
					elif totalPages_flag == 0:
						print('在线汉语字典（http://xh.5156edu.com/）的网页组织方式已经改变！')
						print('即：首页 上一页 下一页 尾页 页次：M/N 每页：P 本类资料：Q的组织方式改变！')
						print('请根据在线汉语字典的新的网页组织方式来重构系统！')
						sys.exit(0)
					elif totalPages_flag == -1:
						print('您本机的网络到在线汉语字典（http://xh.5156edu.com/）的网络不可达！')
						print('请确保您的本机已经联网，然后再重写启动系统！')
						sys.exit(0)
				elif create_earthNormal_flag == 0:
					print(create_earthNormal_error_infomation)
					sys.exit(0)
				elif create_earthNormal_flag == -1:
					print(create_earthNormal_error_infomation)
					sys.exit(0)
			elif create_pageLog_flag == 0:
				print(create_pageLog_error_infomation)
				sys.exit(0)
			elif create_pageLog_flag == -1:
				print(create_pageLog_error_infomation)
				sys.exit(0)
		elif tables_exist_flag == 0:
			print(tables_query_result)
			sys.exit(0)
		elif tables_exist_flag == -1:
			print(tables_query_result)
			sys.exit(0)
	elif db_exist_flag == 1:
		print('Initialize earthElementSync')
		create_database_flag, create_database_error_infomation = data_define.create_database()
		if create_database_flag == 1:
			print(create_database_error_infomation)
			create_pageLog_flag, create_pageLog_error_infomation = data_define.create_table_pageLog()
			if create_pageLog_flag == 1:
				print(create_pageLog_error_infomation)
				create_earthNormal_flag, create_earthNormal_error_infomation = data_define.create_table_earthNormal()
				if create_earthNormal_flag == 1:
					print(create_earthNormal_error_infomation)
					totalPages_flag, total_pages, total_items = extract_earth_element.obtainTotalPages()
					if totalPages_flag == 1:
						print('在线汉语字典（http://xh.5156edu.com/）的网页组织方式未改变！')
						config_parser.set('systemconf', 'db_total_pages', str(total_pages))
						config_parser.set('systemconf', 'db_total_items', str(total_items))
						config_parser.write(open('earth_element_system.config', 'w+'), 'w')
						totalPages_urls = []
						for i in range(total_pages):
							generate_page_url = extract_earth_element.generatePageUrl(i + 1)
							totalPages_urls.append(generate_page_url)
						for page_url_index in range(total_pages):
							page_url = totalPages_urls[page_url_index]
							pageContent_flag, character_list = extract_earth_element.getPageContent(page_url)
							if pageContent_flag == 1:
								earthNormal_executemany_flag, error_information = data_manipulate.insert_by_executemany_for_table_Normal(character_list)
								if earthNormal_executemany_flag == 1:
									print('The page content of {} has been inserted into database successfully.'.format(page_url))
									page_rank = page_url_index + 1
									page_written_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
									insert_value = (page_rank, page_url, page_written_datetime)
									pageLog_execute_flag, pageLog_execute_error_information = data_manipulate.insert_by_execute_for_table_pageLog(insert_value)
									if pageLog_execute_flag == 1:
										print('The log has been written to the database corresponding to the page content.')
									elif pageLog_execute_flag == 0:
										print(pageLog_execute_error_information)
										sys.exit(0)
									elif pageLog_execute_flag == -1:
										print(pageLog_execute_error_information)
										sys.exit(0)
								elif earthNormal_executemany_flag == 0:
									print(error_information)
									sys.exit(0)
								elif earthNormal_executemany_flag == -1:
									print(error_information)
									sys.exit(0)
							elif pageContent_flag == -1:
								print('您本机到链接为:{}的网络页面网络不可达！'.format(page_url))
								print('请确保您的本机已经联网，然后再重写启动系统！')
								sys.exit(0)
						config_db_constructed_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
						print(config_db_constructed_datetime)
						config_parser.set('systemconf', 'db_constructed_datetime', config_db_constructed_datetime)
						config_parser.write(open('earth_element_system.config', 'w+'), 'w')
						print('earthElementSync updated')
						sys.exit(0)
					elif totalPages_flag == 0:
						print('在线汉语字典（http://xh.5156edu.com/）的网页组织方式已经改变！')
						print('即：首页 上一页 下一页 尾页 页次：M/N 每页：P 本类资料：Q的组织方式改变！')
						print('请根据在线汉语字典的新的网页组织方式来重构系统！')
						sys.exit(0)
					elif totalPages_flag == -1:
						print('您本机的网络到在线汉语字典（http://xh.5156edu.com/）的网络不可达！')
						print('请确保您的本机已经联网，然后再重写启动系统！')
						sys.exit(0)
				elif create_earthNormal_flag == 0:
					print(create_earthNormal_error_infomation)
					sys.exit(0)
				elif create_earthNormal_flag == -1:
					print(create_earthNormal_error_infomation)
					sys.exit(0)
			elif create_pageLog_flag == 0:
				print(create_pageLog_error_infomation)
				sys.exit(0)
			elif create_pageLog_flag == -1:
				print(create_pageLog_error_infomation)
				sys.exit(0)
		elif create_database_flag == 0:
			print(create_database_error_infomation)
			sys.exit(0)
		elif create_database_flag == -1:
			print(create_database_error_infomation)
			sys.exit(0)
	elif db_exist_flag == 0:
		print(db_query_result)
		sys.exit(0)
	elif db_exist_flag == -1:
		print(db_query_result)
		sys.exit(0)
if __name__ == '__main__':
	main_Normal()
