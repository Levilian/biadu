# -*- coding: utf-8 -*-
import urllib2 
import json 

class Detail_info:
    
    def __init__(self,s,f):
        self.search_name = s
        self.file_name = f 
    
    def fetch(self,url):
        response = urllib2.urlopen(url)
        #print url
        data = response.read()
       #print data
        parsedData = json.loads(data)
        return parsedData
    
    def write(self):
        baseUrl = "http://api.map.baidu.com/place/v2/search?query="
        size = "&page_size=20"
        accessKey = "g1m6DeA6pc0ToMr2wZeFF5q6Ob1hH2R3"
        page_num = "0" 
        url = baseUrl + self.search_name + size + "&page_num=" +page_num + "&scope=1&region=杭州&output=json&ak=" + accessKey
        file_write = "C:\Users\Administrator\Desktop\\" + self.file_name + ".txt"
        
        with open(file_write,'a') as f:
            num_posts = self.fetch(url)["total"]
            num_pages = num_posts / 20
            for i in range(num_pages +1):
                page_num = str(i)
                print "This is page " + str(i)
                url = baseUrl + self.search_name + size + "&page_num=" +page_num + "&scope=1&region=杭州&output=json&ak=" + accessKey
                posts = self.fetch(url)["results"]
                print url
                for post in posts:
                    uid = str(post["uid"])
                    lat = str(post['location']['lat'])
                    lng = str(post['location']['lng'])
                    address = post["address"]
                    name = post["name"]
                    print name
                    #try:
                    #   street_id = str(post["street_id"])
                    #except:
                        #street_id =''
                    #street_id = str(post.get("street_id", ''))
                    to_write = name + ';' + address + ';' +  uid + ';' + lat + ';' + lng
                    f.write(to_write.encode('utf-8') + '\n')
            f.close()
            f = open(file_write,"a")
        
tea_house = Detail_info("茶馆","tea_house")
tea_house.write()

