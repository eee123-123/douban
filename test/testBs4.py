# -*- codeing = utf-8 -*-
# @Time : 2021/8/17 11:05
# @Author : 军
# @File : testBs4.py
# @Software: PyCharm

'''
BeautifulSoup4将复杂的HTML文件转换成一个复杂的树形结构，每个节点都是Python对象，所有对象可归纳为四种：
Tag
NavigableString
BeautifulSoup
Comment
'''

from bs4 import BeautifulSoup
file=open("./baidu.html","rb")
html=file.read()
bs=BeautifulSoup(html,"html.parser")

#print(bs.title)
#print(bs.a)
#print(bs.head)


#1、Tag   标签及其内容：拿到它所找到的第一个内容
#print(type(bs.title))    #<class 'bs4.element.Tag'>


#2、NavigableString    标签里的内容（字符串）
# print(bs.title.string)  #只获取内容
# print(type(bs.title.string))    #<class 'bs4.element.NavigableString'>
# print(bs.a.attrs)    #键值对形式获取所拥有的标签


#3、BeautifulSoup    整个文档
#print(type(bs))    #<class 'bs4.BeautifulSoup'>


#4、Comment    一个特殊的NavigableString，输出的内容不包括注释符号
# print(bs.a.string)
# print(type(bs.a.string))    #<class 'bs4.element.Comment'>

#---------------------------------------------------------------------------


#文档的遍历  不常用
# print(bs.head.contents)      #contents得到相关键值对
# print(bs.head.contents[1])

import re   #正则表达式
#文档的搜索
#字符串过滤：会查找与字符串完全匹配的内容
#t_list=bs.find_all("a")   #a：超链接
#t_list=bs.find_all(re.compile("a"))   #包含a的内容会被显示

#方法：传入一个函数，根据函数要求搜索(了解)
# def name_is_exists(tag):
#     return tag.has_attr("name")
#
# t_list=bs.find_all(name_is_exists)
# for item in t_list:
#     print(item)   #列表形式
#print(t_list)

#kwargs    参数
#t_list=bs.find_all(id="head")
# t_list=bs.find_all(class_=True)
#t_list=bs.find_all(href="http://news.baidu.com")
#for item in t_list:
#    print(item)   #列表形式

#text参数
# t_list=bs.find_all(text= "hao123")
# t_list=bs.find_all(text=re.compile("\d"))   #应用正则表达式查找包含特定文本的内容（标签里的字符串）
# for item in t_list:
#     print(item)   #列表形式

#limit参数
# t_list=bs.find_all("a",limit=3)   #限制为三次
# for item in t_list:
#     print(item)

#css选择器
#t_list=bs.select('title')   #按标签查
#t_list=bs.select(".mnav")    #按类名
#t_list=bs.select("#u1")   #按id查找
#t_list=bs.select("a[class='bri']")    #按属性查
#t_list=bs.select("head > title")   #head里面的title,通过子标签访问
#t_list=bs.select(".mnav ~.bri")
#print(t_list[0].get_text()) #通过兄弟标签访问
# for item in t_list:
#     print(item)


