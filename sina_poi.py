# -*- coding: utf-8 -*-
import urllib2
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def fetch(url):
    response = urllib2.urlopen(url)
    #print url
    data = response.read()
    #print data
    parsedData = json.loads(data)
    return parsedData

def my_urlencode(str) :
    reprStr = repr(str).replace(r'\x', '%')
    return reprStr[1:-1]

class Pri_info:
    
    def __init__(self,s,f):
        self.search_name = s
        self.file_name = f
     
    def write(self):
        access_token = "2.00juYUmF0dYhVk4f50df99a8UEuKkD&keyword="
        # 2.00zJSBWCDDbLVD7f6c69828efeWmfB
        base_url = "https://api.weibo.com/2/place/pois/search.json?access_token="
        keyword = my_urlencode(self.search_name)
        city = "&city=0571&count=50&page="
        page = "1"
        
        url = base_url + access_token + keyword + city + page
        print url
        file_write = "C:\Users\Administrator\Desktop\\" + self.file_name + ".txt"
        
        with open(file_write,'w+') as f:
            num_posts = fetch(url)["total_number"]
            print num_posts
            num_pages = num_posts / 50
            default = "poiid;title;address;latitude;longitude;category;category_name;categorys;checkin_num;checkin_user_num;photo_num"
            f.write(default.encode('utf-8') + '\n')
            for i in range(1,num_pages +1):
                page_num = str(i)
                print "This is page " + str(i)
                url = base_url + access_token + keyword + city + page_num
                posts = fetch(url)["pois"]
                #print url
                for post in posts:
                    try:
                        poiid = str(post['poiid'])
                        title = post['title']
                        address = str(post['address'])
                        lat = str(post['lat'])
                        lon = str(post['lon'])
                        category = str(post.get('category',' '))
                        category_name = post.get('category_name',' ')
                        categorys = str(post.get('categorys',' '))
                        checkin_num = str(post.get('checkin_num',' '))
                        photo_num = str(post.get('photo_num',' '))
                        checkin_user_num = str(post.get('checkin_user_num',' '))
                        #to_write = poiid + ';' + title + ';' + address + ';' + lat + ';' + lon + ';' + category + ';' + category_name + ';'+ categorys +';'+checkin_num+';'+checkin_user_num+';'+photo_num
                        to_write = '%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s'%(poiid, title, address, lat, lon, category, category_name, categorys, checkin_num, photo_num, checkin_user_num, photo_num)
                    except Exception,e:
                        to_write = ""
                        print str(e)   
                    f.write(to_write.encode('utf-8') + '\n')
            f.close()
            #f = open(file_write,"a")

teahouse = Pri_info("奶茶","sina_milktea")
teahouse.write()