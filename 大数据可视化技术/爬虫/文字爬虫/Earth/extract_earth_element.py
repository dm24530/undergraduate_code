# !/usr/bin/env python
# encoding: utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import re, pandas as pd
import time
import threading
import queue
from configparser import ConfigParser
chrome_driver = r'D:/python/Install_python/Scripts/chromedriver'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
q_in = queue.Queue()
q_out = queue.Queue()
worker_abnormal_exit = threading.Event()
config_parser = ConfigParser()
config_parser.read('earth_element_system.config')
abnormal_url = {'http://xh.5156edu.com/html3/1713.html':('也', 'yě', 3, '乙', 'http://xh.5156edu.com/html3/1713.html'),
                'http://xh.5156edu.com/html3/1751.html':('为', 'wéi,wèi', 4, '丶', 'http://xh.5156edu.com/html3/1751.html'),
                'http://xh.5156edu.com/html3/2198.html':('阳', 'yáng', 6, '阝', 'http://xh.5156edu.com/html3/2198.html'),
                'http://xh.5156edu.com/html3/2706.html':('以', 'yǐ', 4, '人', 'http://xh.5156edu.com/html3/2706.html'),
                'http://xh.5156edu.com/html3/2854.html':('位', 'wèi', 7, '亻', 'http://xh.5156edu.com/html3/2854.html'),
                'http://xh.5156edu.com/html3/3593.html':('友', 'yǒu', 4, '又', 'http://xh.5156edu.com/html3/3593.html'),
                'http://xh.5156edu.com/html3/4716.html':('运', 'yùn', 7, '辶', 'http://xh.5156edu.com/html3/4716.html'),
                'http://xh.5156edu.com/html3/5114.html':('应', 'yìng,yīng', 7, '广', 'http://xh.5156edu.com/html3/5114.html'),
                'http://xh.5156edu.com/html3/5369.html':('叶', 'shè,xié,yè', 5, '口', 'http://xh.5156edu.com/html3/5369.html'),
                'http://xh.5156edu.com/html3/5374.html':('右', 'yòu', 5, '口', 'http://xh.5156edu.com/html3/5374.html'),
                'http://xh.5156edu.com/html3/5447.html':('呀', 'yɑ,yā', 7, '口', 'http://xh.5156edu.com/html3/5447.html'),
                'http://xh.5156edu.com/html3/6226.html':('安', 'ān', 6, '宀', 'http://xh.5156edu.com/html3/6226.html'),
                'http://xh.5156edu.com/html3/6233.html':('完', 'wán', 7, '宀', 'http://xh.5156edu.com/html3/6233.html'),
                'http://xh.5156edu.com/html3/9427.html':('地', 'dì,de', 6, '土', 'http://xh.5156edu.com/html3/9427.html'),
                'http://xh.5156edu.com/html3/9430.html':('圾', 'jī', 6, '土', 'http://xh.5156edu.com/html3/9430.html'),
                'http://xh.5156edu.com/html3/9453.html':('坏', 'huài', 7, '土', 'http://xh.5156edu.com/html3/9453.html'),
                'http://xh.5156edu.com/html3/9494.html':('垃', 'lā', 8, '土', 'http://xh.5156edu.com/html3/9494.html'),
                'http://xh.5156edu.com/html3/9500.html':('坡', 'pō', 8, '土', 'http://xh.5156edu.com/html3/9500.html'),
                'http://xh.5156edu.com/html3/9889.html':('因', 'yīn', 6, '囗', 'http://xh.5156edu.com/html3/9889.html'),
                'http://xh.5156edu.com/html3/9899.html':('园', 'yuán', 7, '囗', 'http://xh.5156edu.com/html3/9899.html'),
                'http://xh.5156edu.com/html3/10813.html':('爷', 'yé', 6, '父', 'http://xh.5156edu.com/html3/10813.html'),
                'http://xh.5156edu.com/html3/13280.html':('王', 'wáng,wàng', 4, '王', 'http://xh.5156edu.com/html3/13280.html'),
                'http://xh.5156edu.com/html3/13830.html':('有', 'yòu,yǒu', 6, '月', 'http://xh.5156edu.com/html3/13830.html'),
                'http://xh.5156edu.com/html3/13834.html':('肚', 'dù,dǔ', 7, '月', 'http://xh.5156edu.com/html3/13834.html'),
                'http://xh.5156edu.com/html3/15307.html':('鸟', 'niǎo,diǎo', 5, '鸟', 'http://xh.5156edu.com/html3/15307.html'),
                'http://xh.5156edu.com/html3/15838.html':('画', 'huà', 8, '田', 'http://xh.5156edu.com/html3/15838.html'),
                'http://xh.5156edu.com/html3/16241.html':('用', 'yòng', 5, '用', 'http://xh.5156edu.com/html3/16241.html'),
                'http://xh.5156edu.com/html3/17571.html':('羽', 'yǔ', 6, '羽', 'http://xh.5156edu.com/html3/17571.html'),
                'http://xh.5156edu.com/html3/22413.html':('衣', 'yī', 6, '衣', 'http://xh.5156edu.com/html3/22413.html'),
                'http://xh.5156edu.com/html3/22419.html':('羊', 'yáng', 6, '羊', 'http://xh.5156edu.com/html3/22419.html'),
                'http://xh.5156edu.com/html3/22419.html':('羊', 'yáng', 6, '羊', 'http://xh.5156edu.com/html3/22419.html')
}
def obtainTotalPages():

	totalPages_flag = -1
	start_page_url = 'http://xh.5156edu.com/wx/tu.html'
	driver = webdriver.Chrome(executable_path=chrome_driver, options=chrome_options)
	driver.get(start_page_url)
	wait_flag = False
	for i in range(10):
		try:
			wait = WebDriverWait(driver, 2)
			if wait_flag == False:
				wait_flag = True
			break
		except TimeoutException:
			continue
	if wait_flag == False:
		print('您本机的网络到在线汉语字典（http://xh.5156edu.com/）的网络不可达！')
		print('请确保您的本机已经联网，然后再重写启动系统！')
		driver.close()
		totalPages_flag = -1
		return totalPages_flag,-1,-1
	f_input_flag = False
	for i in range(10):
		try:
			f_input = wait.until(EC.presence_of_element_located((By.NAME, 'f_key')))
			f_input_flag = True
			break
		except TimeoutException:
			continue
	if f_input_flag == False:
		print('要抽取信息的网页%s，其内容未完全加载完成！\n'%start_page_url)
		print('您本机的网络到在线汉语字典（http://xh.5156edu.com/）的网络不可达！')
		print('请确保您的本机已经联网，然后再重写启动系统！')
		driver.close()
		totalPages_flag = -1
		return totalPages_flag, -1,-1
	pattern = re.compile('页次：\s*\d+/(\d+)\s*每页：\s*\d+\s*本类资料：(\d+)')
	p_list = driver.find_elements_by_tag_name('p')
	total_pages = 0
	total_items = 0
	p_element_flag = False
	for p_element in p_list:
		p_element_list = re.findall(pattern, p_element.text)
		p_element_len = len(p_element_list)
		if p_element_len == 1:
			p_element_tuple_len = len(p_element_list[0])
			if p_element_tuple_len == 2:
				total_pages = int(p_element_list[0][0])
				total_items = int(p_element_list[0][1])
				p_element_flag = True
				break
			else:
				continue
		else:
			continue
	if p_element_flag == False:
		print('在线汉语字典（http://xh.5156edu.com/）的网页组织方式已经改变！')
		print('即：首页 上一页 下一页 尾页 页次：M/N 每页：P 本类资料：Q的组织方式改变！')
		print('请根据在线汉语字典的新的网页组织方式来重构系统！')
		driver.close()
		totalPages_flag = 0
		return totalPages_flag, -1,-1
	first_page_no = True
	try:
		first_page = driver.find_element_by_link_text('首页').get_attribute('href')
		first_page_no = False
	except NoSuchElementException:
		first_page = ''
	previous_page_no = True
	try:
		previous_page = driver.find_element_by_link_text('上一页').get_attribute('href')
		previous_page_no = False
	except NoSuchElementException:
		previous_page = ''
	next_page_no = True
	try:
		next_page = driver.find_element_by_link_text('下一页').get_attribute('href')
		next_page_no = False
	except NoSuchElementException:
		next_page = ''
	last_page_no = True
	try:
		last_page = driver.find_element_by_link_text('尾页').get_attribute('href')
		last_page_no = False
	except NoSuchElementException:
		last_page = ''
	if first_page_no == False or previous_page_no == False or next_page_no == False or last_page_no == False:
		totalPages_flag = 1
		return totalPages_flag, total_pages,total_items
	else:
		print('在线汉语字典（http://xh.5156edu.com/）的网页组织方式已经改变！')
		print('即首页 上一页 下一页 尾页的链接方式改变！')
		print('请根据在线汉语字典的新的网页组织方式来重构系统！')
		driver.close()
		totalPages_flag = 0
		return totalPages_flag, -1, -1
def generatePageUrl(page_number=1):
	if page_number == 1:
		return 'http://xh.5156edu.com/wx/tu.html'
	else:
		return 'http://xh.5156edu.com/wx/tu_{}.html'.format(str(page_number))
def getPageItemUrls(page_url):
	pageItemUrls_flag = -1
	driver = webdriver.Chrome(executable_path=chrome_driver, options=chrome_options)
	driver.get(page_url)
	wait_flag = False
	for i in range(10):
		try:
			wait = WebDriverWait(driver, 2)
			if wait_flag == False:
				wait_flag = True
			break
		except TimeoutException:
			continue
	if wait_flag == False:
		print('您本机到链接为:{}的网络页面网络不可达！'.format(page_url))
		print('请确保您的本机已经联网，然后再重写启动系统！')
		driver.close()
		return pageItemUrls_flag, -1
	f_input_flag = False
	for i in range(10):
		try:
			f_input = wait.until(EC.presence_of_element_located((By.NAME, 'f_key')))
			f_input_flag = True
			break
		except TimeoutException:
			continue
	if f_input_flag == False:
		print('要抽取信息的网页{}，其内容未完全加载完成！\n'.format(page_url))
		print('您本机到链接为:{}的网络页面网络不可达！'.format(page_url))
		print('请确保您的本机已经联网，然后再重写启动系统！')
		driver.close()
		return pageItemUrls_flag, -1
	fontbox_list = driver.find_elements_by_class_name('fontbox2')
	pageItemUrl_list = []
	for fontbox_element in fontbox_list:
		fontbox_content_split = fontbox_element.text.split('\n')
		fontbox_character = fontbox_content_split[0]
		fontbox_url = fontbox_element.get_attribute('href')
		fontbox_content_tuple = (fontbox_character,fontbox_content_split[1][:-1],fontbox_url)
		pageItemUrl_list.append(fontbox_content_tuple)
	driver.close()
	pageItemUrls_flag = 1
	return pageItemUrls_flag, pageItemUrl_list
def get_url_content_worker(q_in, q_out):
	driver = webdriver.Chrome(executable_path=chrome_driver, options=chrome_options)
	continue_flag = True
	allow_request_url_failure_number = config_parser.getint('systemconf','allow_request_url_failure_number_for_worker_threading')
	while (continue_flag) and (not worker_abnormal_exit.is_set()):
		try:
			pageItemUrl = q_in.get(timeout=1)
		except queue.Empty:
			continue_flag = False
			continue
		abnormal_url_flag = abnormal_url.get(pageItemUrl[2], -1)
		if abnormal_url_flag == -1:
			driver.get(pageItemUrl[2])
			wait_flag = False
			for i in range(allow_request_url_failure_number):
				try:
					wait = WebDriverWait(driver, 3)
					if wait_flag == False:
						wait_flag = True
					break
				except TimeoutException:
					continue
			if wait_flag == False:
				print('您本机到链接为:{}的网络页面网络不可达！'.format(pageItemUrl))
				print('请确保您的本机已经联网，然后再重写启动系统！')
				worker_abnormal_exit.set()
				continue
			f_input_flag = False
			for i in range(allow_request_url_failure_number):
				try:
					f_input = wait.until(EC.presence_of_element_located((By.NAME, 'f_key')))
					f_input_flag = True
					break
				except TimeoutException:
					continue
			if f_input_flag == False:
				print('要抽取信息的网页{}，其内容未完全加载完成！\n'.format(pageItemUrl[2]))
				print('您本机到链接为:{}的网络页面网络不可达！'.format(pageItemUrl[2]))
				print('请确保您的本机已经联网，然后再重写启动系统！')
				worker_abnormal_exit.set()
				continue
			fontbox_list = driver.find_elements_by_class_name('table4')
			fontbox_text_list = []
			for fontbox_element in fontbox_list:
				fontbox_text_list.append(fontbox_element.text.split('\n')[0].strip())
			stroke_number_flag = fontbox_text_list.count('笔划：')
			radical_in_chinese_character_flag = fontbox_text_list.count('部首：')
			if (stroke_number_flag == 1) and (radical_in_chinese_character_flag == 1):
				stroke_number_index = fontbox_text_list.index('笔划：') + 1
				radical_in_chinese_character_index = fontbox_text_list.index('部首：') + 1
				stroke_number = int(fontbox_text_list[stroke_number_index])
				radical_in_chinese_character = fontbox_text_list[radical_in_chinese_character_index]
			else:
				worker_abnormal_exit.set()
				continue
			character_quintuple = (pageItemUrl[0], pageItemUrl[1], stroke_number, radical_in_chinese_character, pageItemUrl[2])
			q_out.put(character_quintuple)
		else:
			character_quintuple = abnormal_url_flag
			q_out.put(character_quintuple)
def getPageContent(page_url):
	pageContent_flag = -1
	q_in_size = 0
	q_out_size = 0
	character_list = []
	pageItemUrls_flag, pageItemUrl_list = getPageItemUrls(page_url)
	if pageItemUrls_flag == 1:
		for pageItemUrl in pageItemUrl_list:
			q_in.put(pageItemUrl)
		q_in_size = q_in.qsize()
		worker_threading_number = config_parser.getint('systemconf', 'worker_threading_number')
		threads = []
		for i in range(worker_threading_number):
			worker_thread = threading.Thread(target=get_url_content_worker, args=(q_in, q_out))
			worker_thread.start()
			threads.append(worker_thread)
		for worker_threading in threads:
			worker_threading.join()
		if not worker_abnormal_exit.is_set():
			q_out_size = q_out.qsize()
			if (q_in_size > 0) and (q_in_size == q_out_size):
				while (not q_out.empty()):
					character_list.append(q_out.get())
				pageContent_flag = 1
				return pageContent_flag, character_list
			else:
				return pageContent_flag, character_list
		else:
			return pageContent_flag, character_list
	elif pageItemUrls_flag == -1:
		return pageContent_flag, character_list
if __name__ == '__main__':
	pageContent_flag, character_list = getPageContent('http://xh.5156edu.com/wx/tu_2.html')
	print(character_list)