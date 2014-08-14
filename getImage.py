#http://unsplash.com/
import urllib.parse
import urllib.request
import re,os

def getImages(myurl):
    imgSum = 0
    badImg = 0
    
    req = urllib.request.Request(myurl)
    response = urllib.request.urlopen(req)
    urlStr = response.read()
    #urlStr = urllib.request.urlopen(myurl).read()

    #hrefCmp = re.compile("""<img src=".*?" .*?>""")
    #hrefCmp = re.compile("""<.*? src="(.*?)" .*?>""")
    #hrefCmp = re.compile("""<img src="(.*?)"(.*?)>""")
    hrefCmp = re.compile("""<img.*?src="(.*?)".*?>""")  #ok
    hreflist = hrefCmp.findall(urlStr)

    drive = "E:\\img"
    if not os.path.exists(drive):
        os.mkdir(drive)

    for href in hreflist:
        #print href
        if href.find("""http://""")==0: # must start with http
            imageName = href[href.rindex("/")+1:]
            try:
                urllib.urlretrieve(href, os.path.join(drive,imageName))
                imgSum += 1
                print (imageName + "    OK")
            except :    #default
                print ("cannot download this image: "+imageName)
                #print href
        else:
            badImg += 1
            print (href)
    print ("Success: ",imgSum,"    Failed: ",badImg)

if __name__ == "__main__":
    imgurl = input("url -> ")
    getImages(imgurl)
