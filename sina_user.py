# -*- coding: utf-8 -*-
import requests
import json
import sys
import time
import math
reload(sys)
sys.setdefaultencoding('utf-8')

def fetch(url):
    response = requests.get(url)
    #print url
    data = response.text
    time.sleep(3)
    #print data
    parsedData = json.loads(data)
    return parsedData
    
class Detailed_info:
    def __init__(self,f):
        self.file_name = f
    
    def write(self):
        new_file_write = "C:\Users\Administrator\Desktop\\2detailed" + self.file_name +".txt"
        file_write = "C:\Users\Administrator\Desktop\\" + self.file_name +".txt"
        base_url = 'https://api.weibo.com/2/place/pois/users.json?access_token='
        access_token = "2.00juYUmF0dYhVk4f50df99a8UEuKkD&poiid="
        #2.00juYUmF0dYhVk4f50df99a8UEuKkD  2.00zJSBWCDDbLVD7f6c69828efeWmfB
        count = "&count=50&page="
        init_page_num = "1"
        
        f= open(file_write, 'r')
        total_pri = f.readlines()
        total_pri.pop(0) 
        
        with open(new_file_write, 'a') as d:
            default = "poiid;id;province;city;location;gender;followers_count;friends_count;statuses_count;created_at;checkin_at"
            d.write(default.encode('utf-8') + '\n')
            for u in range(55):
                single_ln = total_pri[u].split(',')
                single_poiid = single_ln[0].strip()
                init_url = base_url + access_token + single_poiid + count + init_page_num
                print init_url
                num_posts = fetch(init_url)["total_number"]
                num_pages = int(math.ceil(num_posts / 50.0))
                
                print num_posts,num_pages
                for i in range(1,num_pages+1):
                    page_num = str(i)
                    url = base_url + access_token + single_poiid + count + page_num
                    print url
                    posts = fetch(url)['users']
                    
                    for post in posts:
                        try:
                            uid = str(post.get('id',''))
                            prov = str(post.get('province',''))
                            city  = str(post.get('city',''))
                            loc = post.get('location','')
                            gender = post.get('gender','')
                            fo_c = str(post.get('followers_count',''))
                            fr_c = str(post.get('friends_count',''))
                            st_c = str(post.get('statuses',''))
                            created_at = post.get('created_at','')
                            checkin_at = post.get('checkin_at','')
                            to_write =single_poiid+';'+uid + ';' + prov + ';' + city+ ';' + loc+ ';' + gender + ';' + fo_c+ ';' + fr_c + ';'+ st_c+';'+created_at+';' +checkin_at 
                        except Exception,e:
                            to_write = ""    
                            print str(e)
                        d.write(to_write.encode('utf-8') + '\n')
        f.close()
        
teahouse = Detailed_info('sina_teahouse_users')   
teahouse.write()