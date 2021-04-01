# !/usr/bin/env python
# _*_ coding:utf-8 _*_
import pymysql
import sys
import os
sys.path.insert(0, os.path.split(os.path.split(os.path.realpath(__file__))[0])[0] + os.sep)
import mysql_config
import sql
def query_database():
	db_exist_flag = -1
	create_connection_flag = False
	execute_sql_flag = False
	try_number_outer = 10
	try_number_inner = 10
	query_rowcount = 0
	error_information = ''
	query_result = ''
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
					database='information_schema')
				create_connection_flag = True
				break
			except pymysql.Error as e:
				mdb_Error = e
			except pymysql.DatabaseError as dbe:
				mdb_DatabaseError = dbe
		if create_connection_flag == False:
			if mdb_Error:
				error_information = 'Error connecting to MySQL Platform: {}'.format(mdb_Error)
			elif mdb_DatabaseError:
				error_information = 'DatabaseError connecting to MySQL Platform: {}'.format(mdb_DatabaseError)
			else:
				error_information = 'Unknown Error connecting to MySQL Platform'
			return db_exist_flag, error_information
		mdb_OperationalError = ''
		mdb_DataError = ''
		try:
			mdb_cursor = conn.cursor()
			mdb_cursor.execute(sql.earthElement_db_exist_sql)
			query_result = mdb_cursor.fetchall()
			query_rowcount = mdb_cursor.rowcount
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
		db_exist_flag = 0
		if mdb_OperationalError:
			error_information = 'Database table query operational error: {}'.format(mdb_OperationalError)
		elif mdb_DataError:
			error_information = 'Database table query data error: {}'.format(mdb_DataError)
		else:
			error_information = 'Unkonwn database table query error'
		return db_exist_flag, error_information
	error_information = 'The database table {} has been queried successfully.'.format(sql.information_schema_schemata)
	if query_rowcount == 1:
		db_exist_flag = 2
	elif query_rowcount == 0:
		db_exist_flag = 1
	return db_exist_flag, error_information
def query_tableNames_for_database():
	tables_exist_flag = -1
	create_connection_flag = False
	execute_sql_flag = False
	try_number_outer = 10
	try_number_inner = 10
	query_rowcount = 0
	query_result = []
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
					port=mysql_config.db_port,database='information_schema')
				create_connection_flag = True
				break
			except pymysql.Error as e:
				mdb_Error = e
			except pymysql.DatabaseError as dbe:
				mdb_DatabaseError = dbe
		if create_connection_flag == False:
			if mdb_Error:
				query_result = 'Error connecting to MySQL Platform: {}'.format(mdb_Error)
			elif mdb_DatabaseError:
				query_result = 'DatabaseError connecting to MySQL Platform: {}'.format(mdb_DatabaseError)
			else:
				query_result = 'Unknown Error connecting to MySQL Platform'
			return tables_exist_flag, query_result
		mdb_OperationalError = ''
		mdb_DataError = ''
		try:
			mdb_cursor = conn.cursor()
			mdb_cursor.execute(sql.earthElement_tables_exist_sql)
			query_result = mdb_cursor.fetchall()
			query_rowcount = mdb_cursor.rowcount
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
		tables_exist_flag = 0
		if mdb_OperationalError:
			query_result = 'Database table query operational error: {}'.format(mdb_OperationalError)
		elif mdb_DataError:
			query_result = 'Database table query data error: {}'.format(mdb_DataError)
		else:
			query_result = 'Unkonwn database table query error'
		return tables_exist_flag, query_result
	if query_rowcount == 0:
		tables_exist_flag = 1
		return tables_exist_flag, query_result
	else:
		tables_exist_flag = 2
		query_result_list = []
		for query_result_element in query_result:
			query_result_list.append(query_result_element[0])
		return tables_exist_flag, query_result_list
def count_items_for_pageLog():
	pageLog_count_flag = -1
	create_connection_flag = False
	execute_sql_flag = False
	try_number_outer = 10
	try_number_inner = 10
	pageLog_rowcount_info = 0
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
				pageLog_rowcount_info = 'Error connecting to MySQL Platform: {}'.format(mdb_Error)
			elif mdb_DatabaseError:
				pageLog_rowcount_info = 'DatabaseError connecting to MySQL Platform: {}'.format(mdb_DatabaseError)
			else:
				pageLog_rowcount_info = 'Unknown Error connecting to MySQL Platform'
			return pageLog_count_flag, pageLog_rowcount_info
		mdb_OperationalError = ''
		mdb_DataError = ''
		try:
			mdb_cursor = conn.cursor()
			mdb_cursor.execute(sql.sql_count_items_for_pageLog)
			query_result = mdb_cursor.fetchall()
			pageLog_rowcount_info = mdb_cursor.rowcount
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
		pageLog_count_flag = 0
		if mdb_OperationalError:
			pageLog_rowcount_info = 'Database table query operational error: {}'.format(mdb_OperationalError)
		elif mdb_DataError:
			pageLog_rowcount_info = 'Database table query data error: {}'.format(mdb_DataError)
		else:
			pageLog_rowcount_info = 'Unkonwn database table query error'
		return pageLog_count_flag, pageLog_rowcount_info
	pageLog_count_flag = 1
	if pageLog_rowcount_info == 1:
		pageLog_rowcount_info = query_result[0][0]
	return pageLog_count_flag, pageLog_rowcount_info
def count_items_for_earthNormal():
	earthNormal_count_flag = -1
	create_connection_flag = False
	execute_sql_flag = False
	try_number_outer = 10
	try_number_inner = 10
	earthNormal_rowcount_info = 0
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
				earthNormal_rowcount_info = 'Error connecting to MySQL Platform: {}'.format(mdb_Error)
			elif mdb_DatabaseError:
				earthNormal_rowcount_info = 'DatabaseError connecting to MySQL Platform: {}'.format(mdb_DatabaseError)
			else:
				earthNormal_rowcount_info = 'Unknown Error connecting to MySQL Platform'
			return earthNormal_count_flag, earthNormal_rowcount_info
		mdb_OperationalError = ''
		mdb_DataError = ''
		try:
			mdb_cursor = conn.cursor()
			mdb_cursor.execute(sql.sql_count_items_for_earthNormal)
			query_result = mdb_cursor.fetchall()
			earthNormal_rowcount_info = mdb_cursor.rowcount
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
		earthNormal_count_flag = 0
		if mdb_OperationalError:
			earthNormal_rowcount_info = 'Database table query operational error: {}'.format(mdb_OperationalError)
		elif mdb_DataError:
			earthNormal_rowcount_info = 'Database table query data error: {}'.format(mdb_DataError)
		else:
			earthNormal_rowcount_info = 'Unkonwn database table query error'
		return earthNormal_count_flag, earthNormal_rowcount_info
	earthNormal_count_flag = 1
	if earthNormal_rowcount_info == 1:
		earthNormal_rowcount_info = query_result[0][0]
	return earthNormal_count_flag, earthNormal_rowcount_info
def query_for_table_earthNormal(query_character):
	create_connection_flag = False
	execute_sql_flag = False
	try_number_outer = 10
	try_number_inner = 10
	query_rowcount = 0
	query_result = ()
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
				create_connection_error_info ='Unknown Error connecting to MySQL Platform'
			print(create_connection_error_info)
			return -1, query_result
		mdb_OperationalError = ''
		mdb_DataError = ''
		try:
			mdb_cursor = conn.cursor()
			mdb_cursor.execute(sql.sql_query_table_earthNormal.format(query_character))
			query_result = mdb_cursor.fetchall()
			query_rowcount = mdb_cursor.rowcount
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
			execute_sql_error_info = 'Database table query operational error: {}'.format(mdb_OperationalError)
		elif mdb_DataError:
			execute_sql_error_info = 'Database table query data error: {}'.format(mdb_DataError)
		else:
			execute_sql_error_info = 'Unkonwn database table query error'
		print(execute_sql_error_info)
		return -1,query_result
	if query_rowcount == 1:
		return 1,query_result
	elif query_rowcount == 0:
		return 0,query_result
