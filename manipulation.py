#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 13:42
# @Author  : Zhangyp
# @File    : manipulation.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from Common.ReadConfig import PARA
from models import User, Product
import datetime

engine = create_engine(PARA['connect_string'], encoding='utf-8', echo=True, convert_unicode=True)  # 初始化数据库连接 echo设置日志记录
DBSession = sessionmaker(bind=engine)  # 创建DBsession类型
session = DBSession()


# 获取user清单
def get_user():
	users = session.query(User).all()
	session.close()  # 关闭会话
	_list = []
	for i in range(len(users)):
		# kv = {}
		kv = dict() # PEP8要求这么写
		kv['id'] = users[i].id
		kv['name'] = users[i].name
		_list.append(kv)
	return _list


# 获取product清单
def get_product():
	products = session.query(Product).all()
	session.close()
	_list = []
	for i in range(len(products)):
		kv = dict()
		kv['id'] = products[i].id
		kv['name'] = products[i].p_name
		_list.append(kv)
	return _list


# 获取QS数量
today = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')  # 当天时间


def get_QS(begin_date='1990-02-13 00:00:00', end_date=today):
	conn = engine.connect()
	sql = "SELECT A.product_name,A.NAME,total_count,critical_count,reopen_count FROM (SELECT product_name, NAME, count( * ) AS total_count, id FROM quality_statistics WHERE closedDate BETWEEN :dt1 AND :dt2 GROUP BY product_name, NAME ) AS A LEFT JOIN ( SELECT product_name, NAME, count( * ) AS critical_count, id FROM quality_statistics WHERE severity <= 2 and closedDate BETWEEN :dt1 AND :dt2 GROUP BY product_name, NAME ) AS B ON A.id = B.id LEFT JOIN ( SELECT product_name, NAME, count( * ) AS reopen_count, id FROM quality_statistics WHERE activatedCount >= 1 and closedDate BETWEEN :dt1 AND :dt2 GROUP BY product_name, NAME ) AS C ON A.id = C.id ORDER BY A.NAME DESC"
	# sql = "SELECT A.product_name,A.NAME,total_count,critical_count,reopen_count FROM (SELECT product_name, NAME, count( * ) AS total_count, id FROM quality_statistics WHERE closedDate BETWEEN :dt1 AND :dt2 GROUP BY product_name, NAME ) AS A LEFT JOIN ( SELECT product_name, NAME, count( * ) AS critical_count, id FROM quality_statistics WHERE severity <= 2 GROUP BY product_name, NAME ) AS B ON A.id = B.id LEFT JOIN ( SELECT product_name, NAME, count( * ) AS reopen_count, id FROM quality_statistics WHERE activatedCount >= 1 GROUP BY product_name, NAME ) AS C ON A.id = C.id ORDER BY A.NAME DESC"
	s = text(sql)
	result = conn.execute(s, dt1=begin_date, dt2=end_date).fetchall()  # 替换时间变量
	conn.close()  # 查询完毕关闭连接
	for i in range(len(result)):  # 处理列表中的None值
		result[i] = list(result[i])
		for j in range(len(result[i])):
			if result[i][j] is None:
				result[i][j] = 0
	# print(result)
	_list = []
	for i in range(len(result)):  # 序列化数据
		kv = dict()
		kv['product_name'] = result[i][0]
		kv['user_name'] = result[i][1]
		kv['total_bug'] = result[i][2]
		kv['critical_count'] = result[i][3]
		kv['critical_rate'] = result[i][3] / result[i][2]
		kv['reopen_count'] = result[i][4]
		kv['reopen_rate'] = result[i][4] / result[i][2]
		_list.append(kv)
	return _list


if __name__ == "__main__":
	# print(get_QS())
	print(get_product())
