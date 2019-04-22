#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 18:08
# @Author  : Zhangyp
# @File    : handle.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

# u = ['胡东慧', '吴美杰']
# p = ['按需打印', 'eWordIMCIS', 'eWordToken']
# p1 = ['eWordIMCIS']
# p2 = ['医学影像浏览器']
# u1=['吴美杰']
# u2=[]
from manipulation import get_QS
def set_body(user_list, product_list):
	L = []
	if user_list != [] and product_list == []:
		L = user_list
	elif user_list == [] and product_list != []:
		L = product_list
	elif user_list == [] and product_list == []:
		pass
	else:
		for u in range(len(user_list)):
			for p in range(len(product_list)):
				L.append(user_list[u] + product_list[p])
	return L

def return_score(body_list,result_list):
	r_list = []
	if body_list==[]:
		return result_list
	for j in range(len(body_list)):
		for f in range(len(result_list)):
			if body_list[j] in result_list[f]['product_name']+result_list[f]['user_name']:
				r_list.append(result_list[f])
			else:
				pass
	return r_list
	

if __name__ == "__main__":
	# score = return_score(["李明"],get_QS())
	print(score)