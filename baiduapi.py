# -*- coding: utf-8 -*-
baseUrl = "http://api.map.baidu.com/place/v2/search?query=社区&page_size=20"
accessKey = "g1m6DeA6pc0ToMr2wZeFF5q6Ob1hH2R3"
page_num = "0"

url = baseUrl + "&page_num=" +page_num + "&scope=1&region=杭州&output=json&ak=" + accessKey
print url
file_write = "C:\Users\Administrator\Desktop\\baiduapi2.txt"

import urllib2 
import json 


def fetch(url):
    response = urllib2.urlopen(url)
    data = response.read()
    parsedData = json.loads(data)
    return parsedData

with open(file_write,'a') as f:
    num_posts = fetch(url)["total"]
    num_pages = num_posts / 20
    for i in range(0, num_pages +1):
        page_num = str(i)
        print "This is page " + str(i)
        url = baseUrl + "&page_num=" +page_num + "&scope=1&region=杭州&output=json&ak=" + accessKey
        fetch(url)
    
        posts = fetch(url)["results"]
        
        for post in posts:
            uid = str(post["uid"])
            lat = str(post['location']['lat'])
            lng = str(post['location']['lng'])
            address = post["address"]
            name = post["name"]
            try:
                street_id = str(post["street_id"])
            except:
                street_id =''
                address = ''
            to_write = name + ';' + address + ';' +  uid + ';' + lat + ';' + lng
            f.write(to_write.encode('utf-8') + '\n')
    f.close()
    f = open(file_write,"a")


