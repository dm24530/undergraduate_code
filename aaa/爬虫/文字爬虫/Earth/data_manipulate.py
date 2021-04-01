# !/usr/bin/env python
# _*_ coding:utf-8 _*_
import pymysql
import sys
import os
sys.path.insert(0, os.path.split(os.path.split(os.path.realpath(__file__))[0])[0] + os.sep)
import mysql_config
import sql
def insert_by_executemany_for_table_Normal(insert_values):
	earthNormal_executemany_flag = -1
	create_connection_flag = False
	execute_sql_flag = False
	try_number_outer = 10
	try_number_inner = 10
	while (execute_sql_flag == False) and (try_number_outer > 0):
		mdb_Error = ''
		mdb_DatabaseError = ''
		try_number_outer = try_number_outer - 1
		for i in range(try_number_inner):
			try:
				conn = pymysql.connect(
					user=mysql_config.db_user,
					password=mysql_config.db_password,
					host=mysql_config.db_host,
					port=mysql_config.db_port,
					database=mysql_config.db_name)
				create_connection_flag = True
				break
			except pymysql.Error as e:
				mdb_Error = e
			except pymysql.DatabaseError as dbe:
				mdb_DatabaseError = dbe
		if create_connection_flag == False:
			if mdb_Error:
				create_connection_error_info = 'Error connecting to MySQL Platform: {}'.format(mdb_Error)
			elif mdb_DatabaseError:
				create_connection_error_info = 'DatabaseError connecting to MySQL Platform: {}'.format(mdb_DatabaseError)
			else:
				create_connection_error_info = 'Unknown Error connecting to MySQL Platform'
			return earthNormal_executemany_flag, create_connection_error_info
		mdb_OperationalError = ''
		mdb_DataError = ''
		try:
			mdb_cursor = conn.cursor()
			mdb_cursor.executemany(sql.insert_manyRecords_for_database_earthElement_table_earthNormal,insert_values)
			conn.commit()
			mdb_cursor.close()
			conn.close()
			execute_sql_flag = True
		except pymysql.OperationalError as operational_error:
			mdb_OperationalError = operational_error
			if mdb_cursor:
				mdb_cursor.close()
			if conn:
				conn.close()
		except pymysql.DataError as data_error:
			mdb_DataError = data_error
			if mdb_cursor:
				mdb_cursor.close()
			if conn:
				conn.close()
		try_number_outer = try_number_outer - 1
	if execute_sql_flag == False:
		if mdb_OperationalError:
			execute_sql_error_info = 'Database table insertion operational error: {}'.format(mdb_OperationalError)
		elif mdb_DataError:
			execute_sql_error_info = 'Database table insertion data error: {}'.format(mdb_DataError)
		else:
			execute_sql_error_info = 'Unkonwn database table insertion error'
		earthNormal_executemany_flag = 0
		return earthNormal_executemany_flag, execute_sql_error_info
	earthNormal_executemany_flag = 1
	return earthNormal_executemany_flag,''
def insert_by_execute_for_table_pageLog(insert_value):
	pageLog_execute_flag = -1
	create_connection_flag = False
	execute_sql_flag = False
	try_number_outer = 10
	try_number_inner = 10
	while (execute_sql_flag == False) and (try_number_outer > 0):
		mdb_Error = ''
		mdb_DatabaseError = ''
		try_number_outer = try_number_outer - 1
		for i in range(try_number_inner):
			try:
				conn = pymysql.connect(
					user=mysql_config.db_user,
					password=mysql_config.db_password,
					host=mysql_config.db_host,
					port=mysql_config.db_port,
					database=mysql_config.db_name)
				create_connection_flag = True
				break
			except pymysql.Error as e:
				mdb_Error = e
			except pymysql.DatabaseError as dbe:
				mdb_DatabaseError = dbe
		if create_connection_flag == False:
			if mdb_Error:
				create_connection_error_info = 'Error connecting to MySQL Platform: {}'.format(mdb_Error)
			elif mdb_DatabaseError:
				create_connection_error_info = 'DatabaseError connecting to MySQL Platform: {}'.format(mdb_DatabaseError)
			else:
				create_connection_error_info = 'Unknown Error connecting to MySQL Platform'
			return pageLog_execute_flag, create_connection_error_info
		mdb_OperationalError = ''
		mdb_DataError = ''
		try:
			mdb_cursor = conn.cursor()
			mdb_cursor.execute(sql.insert_record_for_database_earthElement_table_pageLog,insert_value)
			conn.commit()
			mdb_cursor.close()
			conn.close()
			execute_sql_flag = True
		except pymysql.OperationalError as operational_error:
			mdb_OperationalError = operational_error
			if mdb_cursor:
				mdb_cursor.close()
			if conn:
				conn.close()
		except pymysql.DataError as data_error:
			mdb_DataError = data_error
			if mdb_cursor:
				mdb_cursor.close()
			if conn:
				conn.close()
	if execute_sql_flag == False:
		if mdb_OperationalError:
			execute_sql_error_info = 'Database table insertion operational error: {}'.format(mdb_OperationalError)
		elif mdb_DataError:
			execute_sql_error_info = 'Database table insertion data error: {}'.format(mdb_DataError)
		else:
			execute_sql_error_info = 'Unkonwn database table insertion error'
		pageLog_execute_flag = 0
		return pageLog_execute_flag, execute_sql_error_info
	pageLog_execute_flag = 1
	return pageLog_execute_flag, ''
def insert_by_execute_for_table_Normal(insert_value):
	create_connection_flag = False
	execute_sql_flag = False
	try_number_outer = 10
	try_number_inner = 10
	while (execute_sql_flag == False) and (try_number_outer > 0):
		mdb_Error = ''
		mdb_DatabaseError = ''
		try_number_outer = try_number_outer - 1
		for i in range(try_number_inner):
			try:
				conn = pymysql.connect(
					user=mysql_config.db_user,
					password=mysql_config.db_password,
					host=mysql_config.db_host,
					port=mysql_config.db_port,
					database=mysql_config.db_name)
				create_connection_flag = True
				break
			except pymysql.Error as e:
				mdb_Error = e
			except pymysql.DatabaseError as dbe:
				mdb_DatabaseError = dbe
		if create_connection_flag == False:
			if mdb_Error:
				create_connection_error_info = 'Error connecting to MySQL Platform: {}'.format(mdb_Error)
			elif mdb_DatabaseError:
				create_connection_error_info = 'DatabaseError connecting to MySQL Platform: {}'.format(mdb_DatabaseError)
			else:
				create_connection_error_info = 'Unknown Error connecting to MySQL Platform'
			print(create_connection_error_info)
			sys.exit(1)
		mdb_OperationalError = ''
		mdb_DataError = ''
		try:
			mdb_cursor = conn.cursor()
			mdb_cursor.execute(sql.insert_record_for_database_earthElement_table_earthNormal,insert_value)
			conn.commit()
			mdb_cursor.close()
			conn.close()
			execute_sql_flag = True
		except pymysql.OperationalError as operational_error:
			mdb_OperationalError = operational_error
			if mdb_cursor:
				mdb_cursor.close()
			if conn:
				conn.close()
		except pymysql.DataError as data_error:
			mdb_DataError = data_error
			if mdb_cursor:
				mdb_cursor.close()
			if conn:
				conn.close()
	if execute_sql_flag == False:
		if mdb_OperationalError:
			execute_sql_error_info = 'Database table insertion operational error: {}'.format(mdb_OperationalError)
		elif mdb_DataError:
			execute_sql_error_info = 'Database table insertion data error: {}'.format(mdb_DataError)
		else:
			execute_sql_error_info = 'Unkonwn database table insertion error'
		print(execute_sql_error_info)
