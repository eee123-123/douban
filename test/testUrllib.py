# -*- codeing = utf-8 -*-
# @Time : 2021/8/16 19:23
# @Author : 军
# @File : testUrllib.py
# @Software: PyCharm

import urllib.request

#获取一个get请求
# response=urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))

#获取一个post请求
# import urllib.parse  #进行解码
# data=bytes(urllib.parse.urlencode({"hello":"world"}),encodings="utf-8")  #使用字节文件转换，post通常用于网站密码登录
# response=urllib.request.urlopen("http://httpbin.org/post",date=data)
# print(response.read().decode('utf-8'))


# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print("Time out!")

# response = urllib.request.urlopen("http://httpbin.org/get")
# print(response.status)
# print(response.getheader("Server"))

# import urllib.parse
# url="http://httpbin.org/post"
# headers={
# "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"
# }
# data=bytes(urllib.parse.urlencode({'hello':'world'}),"utf-8")
# req=urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response=urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

import urllib.parse
url="https://www.douban.com"
#url="https://movie.douban.com/top250?start"
headers={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"
}
# cookie={
# 'Cookie': 'bid=6wGJc1fkXPk; ll="118250"; __utmz=223695111.1629168169.2.2.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; dbcl2="244912182:pxawqauNAkA"; ck=_eSp; __gads=ID=3b2a5e8e28074089-2206f811d0ca00ad:T=1629032271:S=ALNI_MZExaGvQXG6Ev8M8-R3BGrzV3LlPA; push_noty_num=0; push_doumail_num=0; __utmc=30149280; __utmz=30149280.1629460360.3.3.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=30149280.24491; __utmc=223695111; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1629463993%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_id.100001.4cf6=9b5471ae1a1c35ff.1629032270.4.1629463993.1629460432.; _pk_ses.100001.4cf6=*; __utma=30149280.885673448.1629032270.1629460360.1629463993.4; __utmb=30149280.0.10.1629463993; __utma=223695111.396136727.1629032270.1629460402.1629463993.4; __utmb=223695111.0.10.1629463993'
# }
req=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(req)
print(response.read().decode("utf-8"))