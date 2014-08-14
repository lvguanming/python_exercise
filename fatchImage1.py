#-*- coding:utf-8 -*-
import urllib.request
import re,os

#获取百度贴吧上的html代码
def getHtml(url):
    #获取html对象
    objHtml = urllib.request.urlopen(url)
    html = objHtml.read().decode("gbk")
    return html

#下载图片
def getImg(html):
    #bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=c28c9a79f4246b607b0eb27cdbc31b4c/a044ad345982b2b7ac27fdee33adcbef76099b64.jpg" class="
    #html正则表达式分析
    reHtml = r'bpic="(http\:\/\/imgsrc\.baidu\.com\/forum\/.*?\.jpg)" class'
    compileRe = re.compile(reHtml)
    #获取图片地址
    imgHtml = re.findall(compileRe,html)
    imgNameNum = 0
    #下载图片并重命名
    drive = "E:\\img"
    if not os.path.exists(drive):
        os.mkdir(drive)
    for imglist in imgHtml:
        urllib.request.urlretrieve(imglist,os.path.join(drive,"{0}.jpg".format(imgNameNum)))
        imgNameNum += 1
    print("finished")
        
        
    
url = "http://tieba.baidu.com/f?ie=utf-8&kw=%E6%A1%8C%E9%9D%A2%E5%A3%81%E7%BA%B8"
html = getHtml(url)
getImg(html)