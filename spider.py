# -*- codeing = utf-8 -*-
# @Time : 2021/8/15 21:26
# @Author : 军
# @File : spider.py
# @Software: PyCharm

#引入第三方模块
import bs4     #网页解析，获取数据
import re      #正则表达式，进行文字匹配
import urllib.request,urllib.error     #制定URL，获取网页数据
import xlwt     #进行Excel操作
import sqlite3     #进行SQLite数据库操作
from bs4 import BeautifulSoup

def main():
    baseurl="https://movie.douban.com/top250?start="
    #1.爬取网页
    datelist=getData(baseurl)
    #savepath="豆瓣电影Top250.xls"
    dbpath = "movie.db"
    #3.保存数据
    #saveData(datelist,savepath)
    saveData2DB(datelist,dbpath)

    #askURL("https://movie.douban.com/top250?start=)


#影片详情链接规则
findlink=re.compile(r'<a href="(.*?)">')    #创建正则表达式对象，表示规则
#影片图片链接规则
findimgsrc=re.compile(r'<img.*src="(.*?)"',re.S)     #re.S让换行符包含在字符中
#影片片名规则
findtitle=re.compile(r'<span class="title">(.*)</span>')
#影片评分规则
findrating=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#影片评价人数规则
findjudge=re.compile(r'<span>(\d*)人评价</span>')
#影片概况规则
findinq=re.compile(r'<span class="inq">(.*)</span>')
#影片的相关内容规则
findbd=re.compile(r'<p class="">(.*?)</p>',re.S)


#爬取网页
def getData(baseurl):
    datalist=[]
    for i in range(0,10):  #调用获取页面信息的函数10次
        url=baseurl+str(i*25)
        html=askURL(url)   #保存获取到的网页源码
        #2.解析数据
        soup=BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):    #查找符合要求的内容，以列表形式.   加下划线代表属性值
            #print(item)     测试查看电影全部信息
            data=[]     #保存一部电影的所有信息
            item=str(item)
            #影片详情链接
            link=re.findall(findlink,item)[0]    #re通过正则表达式查找指定字符串
            data.append(link)    #添加链接
            imgSrc=re.findall(findimgsrc,item)[0]
            data.append(imgSrc)    #添加图片
            titles=re.findall(findtitle,item)
            if(len(titles)==2):
                ctitle=titles[0]
                data.append(ctitle)
                otitle=titles[1].replace("/","")
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append('  ')    #外国名留空
            rating=re.findall(findrating,item)[0]
            data.append(rating)    #添加评分
            judgenum=re.findall(findjudge,item)[0]
            data.append(judgenum)    #添加评价人数
            inq=re.findall(findinq,item)
            if len(inq)!=0:
                inq=inq[0].replace("。","")    #去掉句号
                data.append(inq)    #添加概述
            else:
                data.append("  ")    #留空
            bd=re.findall(findbd,item)[0]
            bd=re.sub('<br(\s+)?/>(\s+)?'," ",bd)    #去掉<br/>
            data.append(bd.strip())    #去掉全部空格
            datalist.append(data)    #将处理好的一部电影信息放入daralist


    return datalist


#得到指定一个URL的网页内容
def askURL(url):
    head={
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 92.0.4515 .131 Safari / 537.36 Edg / 92.0 .902 .73"
    }     #用户代理，表示告诉豆瓣服务器我们是什么类型的机器，伪装用
    request=urllib.request.Request(url,headers=head)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

def saveData(datalist,savepath):
    print("save")
    book=xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet=book.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True)
    col=("电影详情链接","图片链接","影片中文名","影片外文名","评分","评论数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i]) #列名
    for i in range(0,250):
        print("第%d条" %(i+1))
        data=datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])

    book.save(savepath)


def saveData2DB(datalist,dbpath):
    init_db(dbpath)
    conn=sqlite3.connect(dbpath)
    cur=conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index]='"'+data[index]+'"'
        sql='''
                insert into movie250(
                info_link,pic_link,cname,ename,score,rated,instroduction,info)
                values(%s)'''%",".join(data)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()

def init_db(dbpath):
    sql='''
        create table movie250
        (
        id integer primary key autoincrement ,
        info_link text ,
        pic_link text ,
        cname varchar ,
        ename varchar ,
        score numeric ,
        rated numeric ,
        instroduction text ,
        info text
        )
    '''    #创建数据表
    conn=sqlite3.connect(dbpath)
    cursor=conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == '__main__':     #当程序执行时  用以控制流程，程序入口，方便
#调用函数
    main()
    #init_db("movietest.db")
    print("爬取完毕")

