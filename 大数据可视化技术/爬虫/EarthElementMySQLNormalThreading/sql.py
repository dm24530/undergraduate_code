#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sys
import os
sys.path.insert(0,os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]+os.sep)
import mysql_config
db_name = "earthElement"
db_table_pageLog = 'pageLog'
db_table_earthNormal = 'earthNormal'
information_schema_tables = 'information_schema.tables'
information_schema_schemata = 'information_schema.schemata'
earthElement_db_exist_sql = """SELECT * FROM information_schema.schemata WHERE schema_name='{}'""".format(mysql_config.db_name)
earthElement_tables_exist_sql = """SELECT table_name FROM information_schema.tables WHERE table_schema='{}'""".format(mysql_config.db_name)
earthElement_db_create_sql = """CREATE DATABASE IF NOT EXISTS %s""" % (mysql_config.db_name)
earthElement_db_drop_sql ="""DROP DATABASE IF EXISTS %s"""%(mysql_config.db_name)
create_table_pageLog = """CREATE TABLE IF NOT EXISTS pageLog (
                                        page_rank int not null,
                                        page_url varchar(256) not null,
                                        page_written_datetime varchar(128),
                                        primary key (page_rank)
                                    ); """
drop_table_pageLog = """DROP TABLE IF EXISTS %s"""%(db_table_pageLog)
earth_table_for_database_earthElement_Normal = 'earthNormal'
create_earth_table_for_database_earthElement_Normal = """ CREATE TABLE IF NOT EXISTS earthNormal (
                                        earth_character varchar(32) not null,
                                        earth_pinyin varchar(32) not null,
                                        stroke_number int not null,
                                        radical_in_chinese_character varchar(32) not null,
                                        item_url varchar(128) not null,
                                        primary key (earth_character)
                                    ); """
drop_earth_table_for_database_earthElement_Normal = """DROP TABLE IF EXISTS %s"""%(db_table_earthNormal)
insert_manyRecords_for_database_earthElement_table_earthNormal = '''REPLACE INTO earthNormal (earth_character,earth_pinyin,stroke_number,radical_in_chinese_character,item_url) VALUES (%s,%s,%s,%s,%s)'''
insert_record_for_database_earthElement_table_pageLog = '''REPLACE INTO pageLog (page_rank,page_url,page_written_datetime) VALUES (%s,%s,%s)'''
insert_record_for_database_earthElement_table_earthNormal = '''REPLACE INTO earthNormal (earth_character,earth_pinyin,stroke_number,radical_in_chinese_character,item_url) VALUES (%s,%s,%s,%s,%s)'''
sql_count_items_for_pageLog = '''SELECT count(*) FROM pageLog'''
sql_count_items_for_earthNormal = '''SELECT count(earth_character) FROM earthNormal'''
sql_query_table_earthNormal = """SELECT * FROM earthNormal WHERE earth_character='{}'"""
