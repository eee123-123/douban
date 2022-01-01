# -*- codeing = utf-8 -*-
# @Time : 2021/8/15 21:33
# @Author : 军
# @File : t2.py
# @Software: PyCharm

#引入自定义模块
from test1 import t1

print(t1.add(1,1))

#引入系统模块 import time等、

#引入第三方模块
import bs4     #网页解析，获取数据
import re      #正则表达式，进行文字匹配
import urllib.request,urllib.error     #制定URL，获取网页数据
import xlwt     #进行Excel操作
import sqlite3     #进行SQLite数据库操作