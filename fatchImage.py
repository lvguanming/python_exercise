#-*- coding:utf-8 -*-
import urllib.request
import re,os,sys

def getHtml(url):
    #获取html对象
    objHtml = urllib.request.urlopen(url)
    html = objHtml.read().decode("utf-8")
    return html

def getImg(html):
    reHtml = 'src="(.*?\.jpg)'
    compileRe = re.compile(reHtml)
    imgHtml = re.findall(compileRe,html)
    drive = "E:\\img"
    if not os.path.exists(drive):
        os.mkdir(drive)
    for imglist in imgHtml:
        #fileName = imglist[imglist.rindex("/")+1:]
        #print(fileName)
        #urllib.request.urlretrieve(imglist,os.path.join(drive,fileName))
        print(imglist)
    print("finished")


url = "http://unsplash.com/page/{0}"
sys.stdout = open("stdout.txt", "a")
for i in range(1, 105 + 1):
    curl = url.format(i)
    #print(curl)
    html = getHtml(curl)
    getImg(html)
