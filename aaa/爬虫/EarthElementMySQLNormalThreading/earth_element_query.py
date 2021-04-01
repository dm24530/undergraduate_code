#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sys
import data_query
def main(argv=None):
	if len(sys.argv) < 2:
		print('Please input single chinese character, such as : python earth_element_query.py 土')
		sys.exit(0)
	status, queryResult = data_query.query_for_table_earthNormal(str(sys.argv[1]))
	if status == 1:
		print('{}的五行属性分类为：属土'.format(sys.argv[1]))
	elif status == 0:
		print('{}的五行属性分类不是属土'.format(sys.argv[1]))
	elif status == -1:
		print('Unable to connect to database!')
if __name__ == '__main__':
	main()
