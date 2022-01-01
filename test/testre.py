# -*- codeing = utf-8 -*-
# @Time : 2021/8/17 19:46
# @Author : 军
# @File : testre.py
# @Software: PyCharm

#正则表达式：字符串模式（判断字符串是否符合一定标准）
import re

#创建模式对象
# pat=re.compile("AA")   #此处AA是正则表达式，用以验证其他字符串,compile用以生成
# m=pat.search("CBA")    #search字符串被校验的内容,只能找到第一次出现的
# n=pat.search("AABGAA")
# print(m)
# print(n)

#无模式对象
# m=re.search("as","aaass")    #前为规则，后为校验
# print(m)

# m=re.findall("a","SDWAaadffewav")   #前为规则，后为校验
# print(m)

#print(re.findall("[A-Z]","ADGegdhDFHY"))
#print(re.findall("[A-Z]+","DAfherhHETR"))

#sub

#print(re.sub("a","A","Asfafragea"))    #被替换对象   替换对象    校验对象

#建议在正则表达式中，被比较的字符串前加r，就不用担心转义字符问题
# a=r"\aabd-\'"
# print(a)
