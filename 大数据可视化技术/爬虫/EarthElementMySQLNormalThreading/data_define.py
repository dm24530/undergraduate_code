# !/usr/bin/env python
# _*_ coding:utf-8 _*_
import pymysql
import sys
import os
sys.path.insert(0, os.path.split(os.path.split(os.path.realpath(__file__))[0])[0] + os.sep)
import mysql_config
import sql
'''
数据表的创建可以创建一个创建数据的函数，该函数需要有要创建数据表的SQL语句
目前的版本创建数据库表是以每个数据库一个数据表的形式来创建
'''
def create_database():
	create_database_flag = -1
	create_connection_flag = False
	execute_sql_flag = False
	try_number_outer = 10
	try_number_inner = 10
	while(execute_sql_flag == False) and (try_number_outer>0):
		mdb_Error = ''
		mdb_DatabaseError = ''
		try_number_outer = try_number_outer - 1
		for i in range(try_number_inner):
			try:
				conn = pymysql.connect(
					user=mysql_config.db_user,
					password=mysql_config.db_password,
					host=mysql_config.db_host,
					port=mysql_config.db_port)
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
			return create_database_flag, error_information
		mdb_OperationalError = ''
		try:
			mdb_cursor = conn.cursor()
			mdb_cursor.execute(sql.earthElement_db_create_sql)
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
	if execute_sql_flag == False:
		create_database_flag = 0
		if mdb_OperationalError:
			error_information = 'Database creation error: {}'.format(mdb_OperationalError)
		else:
			error_information = 'Unkonwn database creation error'
		return create_database_flag, error_information
	create_database_flag = 1
	error_information = 'The database {} has been created successfully.'.format(mysql_config.db_name)
	return create_database_flag, error_information
def drop_database():
	drop_database_flag = -1
	create_connection_flag = False
	execute_sql_flag = False
	try_number_outer = 10
	try_number_inner = 10
	while(execute_sql_flag == False) and (try_number_outer>0):
		mdb_Error = ''
		mdb_DatabaseError = ''
		try_number_outer = try_number_outer - 1
		for i in range(try_number_inner):
			try:
				conn = pymysql.connect(
					user=mysql_config.db_user,
					password=mysql_config.db_password,
					host=mysql_config.db_host,
					port=mysql_config.db_port)
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
			return drop_database_flag, error_information
		mdb_OperationalError = ''
		try:
			mdb_cursor = conn.cursor()
			mdb_cursor.execute(sql.earthElement_db_drop_sql)
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
	if execute_sql_flag == False:
		drop_database_flag = 0
		if mdb_OperationalError:
			error_information = 'Database dropping error: {}'.format(mdb_OperationalError)
		else:
			error_information = 'Unkonwn database dropping error'
		return drop_database_flag, error_information
	error_information = 'The database {} has been dropped successfully.'.format(mysql_config.db_name)
	drop_database_flag = 1
	return drop_database_flag,error_information
def create_table_pageLog():
	create_pageLog_flag = -1
	create_connection_flag = False
	execute_sql_flag = False
	try_number_outer = 10
	try_number_inner = 10
	while (execute_sql_flag == False) and (try_number_outer > 0):
		mdb_Error = ''
		mdb_DatabaseError = ''
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
				error_information = 'Error connecting to MySQL Platform: {}'.format(mdb_Error)
			elif mdb_DatabaseError:
				error_information = 'DatabaseError connecting to MySQL Platform: {}'.format(mdb_DatabaseError)
			else:
				error_information = 'Unknown Error connecting to MySQL Platform'
			return create_pageLog_flag, error_information
		mdb_OperationalError = ''
		try:
			mdb_cursor = conn.cursor()
			mdb_cursor.execute(sql.create_table_pageLog)
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
	if execute_sql_flag == False:
		create_pageLog_flag = 0
		if mdb_OperationalError:
			error_information = 'Database table creation error: {}'.format(mdb_OperationalError)
		else:
			error_information = 'Unkonwn database table creation error'
		return create_pageLog_flag, error_information
	create_pageLog_flag = 1
	error_information = 'The database table {} has been created successfully.'.format(sql.db_table_pageLog)
	return create_pageLog_flag, error_information
def drop_table_pageLog():
	drop_pageLog_flag = -1
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
				error_information = 'Error connecting to MySQL Platform: {}'.format(mdb_Error)
			elif mdb_DatabaseError:
				error_information = 'DatabaseError connecting to MySQL Platform: {}'.format(mdb_DatabaseError)
			else:
				error_information = 'Unknown Error connecting to MySQL Platform'
			return drop_pageLog_flag, error_information
		mdb_OperationalError = ''
		try:
			mdb_cursor = conn.cursor()
			mdb_cursor.execute(sql.drop_table_pageLog)
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
	if execute_sql_flag == False:
		drop_pageLog_flag = 0
		if mdb_OperationalError:
			error_information = 'Database table dropping error: {}'.format(mdb_OperationalError)
		else:
			error_information = 'Unkonwn database table dropping error'
		return drop_pageLog_flag, error_information
	drop_pageLog_flag = 1
	error_information = 'The database table {} has been dropped successfully.'.format(sql.db_table_pageLog)
	return drop_pageLog_flag, error_information
def create_table_earthNormal():
	create_earthNormal_flag = -1
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
				error_information = 'Error connecting to MySQL Platform: {}'.format(mdb_Error)
			elif mdb_DatabaseError:
				error_information = 'DatabaseError connecting to MySQL Platform: {}'.format(mdb_DatabaseError)
			else:
				error_information = 'Unknown Error connecting to MySQL Platform'
			return create_earthNormal_flag, error_information
		mdb_OperationalError = ''
		try:
			mdb_cursor = conn.cursor()
			mdb_cursor.execute(sql.create_earth_table_for_database_earthElement_Normal)
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
	if execute_sql_flag == False:
		create_earthNormal_flag = 0
		if mdb_OperationalError:
			error_information = 'Database table creation error: {}'.format(mdb_OperationalError)
		else:
			error_information = 'Unkonwn database table creation error'
		return create_earthNormal_flag, error_information
	create_earthNormal_flag = 1
	error_information = 'The database table {} has been created successfully.'.format(sql.db_table_earthNormal)
	return create_earthNormal_flag, error_information
def drop_table_earthNormal():
	drop_earthNormal_flag = -1
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
				error_information = 'Error connecting to MySQL Platform: {}'.format(mdb_Error)
			elif mdb_DatabaseError:
				error_information = 'DatabaseError connecting to MySQL Platform: {}'.format(mdb_DatabaseError)
			else:
				error_information = 'Unknown Error connecting to MySQL Platform'
			return drop_earthNormal_flag, error_information
		mdb_OperationalError = ''
		try:
			mdb_cursor = conn.cursor()
			mdb_cursor.execute(sql.drop_earth_table_for_database_earthElement_Normal)
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
	if execute_sql_flag == False:
		drop_earthNormal_flag = 0
		if mdb_OperationalError:
			error_information = 'Database table dropping error: {}'.format(mdb_OperationalError)
		else:
			error_information = 'Unkonwn database table dropping error'
		return drop_earthNormal_flag, error_information
	drop_earthNormal_flag = 1
	error_information = 'The database table {} has been dropped successfully.'.format(sql.db_table_earthNormal)
	return drop_earthNormal_flag, error_information
