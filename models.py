#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 11:02
# @Author  : Zhangyp
# @File    : models.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

ModelBase = declarative_base()  # 元类


class User(ModelBase):
	__tablename__ = "dev_user"
	
	id = Column(Integer, primary_key=True)
	name = Column(String)
	__table_args__ = {"mysql_charset": "utf8"}


class Product(ModelBase):
	__tablename__ = "product"
	
	id = Column(Integer, primary_key=True)
	p_name = Column(String)
	__table_args__ = {"mysql_charset": "utf8"}

class Qs(ModelBase):
	__tablename__ = "quality_statistics"
	
	bug_id = Column(Integer, primary_key=True)
	product_name = Column(String)
	name = Column(String)
	id = Column(String)
	confirmed = Column(Integer)
	severity = Column(Integer)
	activatedCount = Column(Integer)
	closedDate = Column(DateTime)


if __name__ == "__main__":
	engine = create_engine('mysql://root:123456@192.168.1.43:3306/zentao', encoding='latin1',
						   echo=True)  # 初始化数据库连接 echo设置日志记录
	DBSession = sessionmaker(bind=engine)  # 创建DBsession类型
	session = DBSession()  # 创建session对象
	users = session.query(User).all()
	user_list = []
	dict = {}
	for i in range(len(users)):
		dict = {}
		dict['id'] = users[i].id
		dict['name'] = users[i].name
		user_list.append(dict)
	# print({users[i].id,users[i].name})
	print(user_list)
