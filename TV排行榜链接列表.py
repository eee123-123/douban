#!/usr/bin/env python
# encoding: utf-8
"""
@author: Zengjc
@time: 2019/8/9 20:53
"""
import requests
import re
from pyquery import PyQuery as pq

header = { 'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Referer': 'http://www.tvtv.hk/archives/category/tv',}
# 有修改
header2 = {
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.tvtv.hk/archives/category/tv',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
}
# 有修改
cookies = {
    'cookietest': '1',
    'first_h': '1565436903037',
    'count_h': '1',
    'first_m': '1565436903039',
    'count_m': '1',
    'tanbot': '4',
    'preurl': '/archives/7992.html',
    'captchaKey': '8da7e0f68f',
    'captchaExpire': '1565437504',
    'UM_distinctid': '16c7b4f7fe54b5-0fdecd134540e-46531b29-1fa400-16c7b4f7fe63db',
    'CNZZDATA1274893240': '812355175-1565431531-null^%^7C1565431531',
    'Hm_lvt_472301bdad2dfd559bccec6997e84552': '1565436904',
    'Hm_lpvt_472301bdad2dfd559bccec6997e84552': '1565436930',
}
#   爬取每日TV收视率的网址 start
print('爬取每日TV收视率的网址')
for i in range(1,30):
    url = 'http://www.tvtv.hk/archives/category/tv/page/%s'% str(i)
    print(url)
    response = requests.get(url,headers=header)
    response.encoding = 'utf-8'
    html = response.text
    doc = pq(html)# 格式化了一下
    articles = doc.find('.status-publish')#每个 article 都有这么一个类，即找到了该页所有 article 标签
    hrefs = {}
    for article in articles.items():
        alink = article.find('h2 a')
        # print(alink.attr('href'))# 提取网页 href链接属性
        # print(alink.attr('title'))# 提取网页 title标题
        hrefs[alink.attr('title')] = alink.attr('href')# 以title 为key 以href 为 value形成一个字典
    f = open('TV排行榜链接列表.txt', 'a', encoding='utf-8')
    for key in hrefs.keys():
        if key.find('榜（') > 0:
            f.write(key + ',' + hrefs[key] + '\n')
    f.close()
#   爬取每日TV收视率的网址 start

#   爬取每日TV收视率 start
print('爬取每日TV收视率')
out = open('TV收视率排行榜列表.txt', 'a', encoding='utf-8')
fb = open('TV排行榜链接列表.txt', 'r', encoding='utf-8')
for line in fb:  # 遍历排行榜链接列表
    strs = line.split(',')
    # 有修改
    rank_response = requests.get(strs[1], headers=header2, cookies=cookies, verify=False, timeout = 10000 )  # strs[1] 为该日的排行榜链接
    rank_response.encoding = 'utf-8'
    rank_html = rank_response.text
    rank_doc = pq(rank_html)
    print(rank_doc)
    paragraph = rank_doc.find('.entry-content p').text()
    ranks = paragraph.split(' ')
    n = 0
    for rank in ranks:
        # print(str(rank))
        if not 1 <= n < 3:
            out.write(' %s' % rank)
        n = n + 1
    out.write('\n')
fb.close()
out.close()
#   爬取每日TV收视率 end
