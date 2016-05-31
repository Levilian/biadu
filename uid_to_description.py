# -*- coding: utf-8 -*-
import urllib2
import json


def fetch(url):
    response = urllib2.urlopen(url)
    #print url
    data = response.read()
    #print data
    parsedData = json.loads(data)
    return parsedData

class Pri_info:
    
    def __init__(self,s,f):
        self.search_name = s
        self.file_name = f
    
    def write(self):
        baseUrl = "http://api.map.baidu.com/place/v2/search?query="
        size = "&page_size=20"
        #accessKey = "DO3WrKcoP5il0HK3dW1xSSYlbTvbALEe"
        #accessKey = 'o218vlEHEYiismhbYEyBMi9FGY0FWKMC'
        accessKey = 'riOdXPNrkmETYEYFGxuTXi1XsqBYCB8z'
        page_num = "0" 
        url = baseUrl + self.search_name + size + "&page_num=" +page_num + "&scope=1&region=杭州&output=json&ak=" + accessKey
        file_write = "C:\Users\Administrator\Desktop\\" + self.file_name + ".txt"
        
        with open(file_write,'w+') as f:
            num_posts = fetch(url)["total"]
            num_pages = num_posts / 20
            default = "name;address;uid;latitude;longitude"
            f.write(default.encode('utf-8') + '\n')
            for i in range(num_pages +1):
                page_num = str(i)
                print "This is page " + str(i)
                url = baseUrl + self.search_name + size + "&page_num=" +page_num + "&scope=1&region=杭州&output=json&ak=" + accessKey
                posts = fetch(url)["results"]
                #print url
                for post in posts:
                    uid = str(post["uid"])
                    lat = str(post['location']['lat'])
                    lng = str(post['location']['lng'])
                    address = post["address"]
                    name = post["name"]
                    
                    #try:
                    #   street_id = str(post["street_id"])
                    #except:
                        #street_id =''
                    #street_id = str(post.get("street_id", ''))
                    to_write = name + ';' + address + ';' +  uid + ';' + lat + ';' + lng
                    f.write(to_write.encode('utf-8') + '\n')
            f.close()
            #f = open(file_write,"a")
             
class Detailed_info(Pri_info):
    def __init__(self,s,f):
        Pri_info.__init__(self,s,f)
   # def fetch(self,url):
    #    .fetch(url)
    
    def write(self):
        baseURL = "http://api.map.baidu.com/place/v2/detail?uid="
        ak = "&output=json&scope=2&ak=riOdXPNrkmETYEYFGxuTXi1XsqBYCB8z"
        new_file_write = "C:\Users\Administrator\Desktop\\detailed" + self.file_name +".txt"
        file_write = "C:\Users\Administrator\Desktop\\" + self.file_name +".txt"
        
        f= open(file_write, 'r')
        total_pri = f.readlines()
        total_pri.pop(0)    
        with open(new_file_write, 'w+') as d:
            default = "name;latitude;longitude;address;uid;tag;type;price;overall_rating;image_num;comment_num"
            d.write(default.encode('utf-8') + '\n')
            for u in range(len(total_pri)):
               
                single_ln = total_pri[u].split(';')
                single_uid = single_ln[2]
                #uid = single_ln[0]
                url = baseURL + single_uid.strip() + ak
                
                response = fetch(url)
                
                content = response['result']
                    
                try:
                    
                    response = fetch(url)
                    content = response['result']
                    name = content['name']
                    lat = str(content['location']['lat'])
                    lng = str(content['location']['lng'])
                    addr = content['address']
                    uid = str(content['uid'])
                    print "this is the " + str(u) + "th line of data"
                    #print content
                    #pre = str(content['precision'])
                    #confi = str(content['confidence'])
                    if content['detail'] == 1:
                        print "entering if"
                        tag = content['detail_info']['tag']
                        typ = str(content['detail_info']['type'])
                        price = str(content['detail_info'].get('price',''))
                        ovr_rtn = str(content['detail_info'].get('overall_rating',''))
                        tst_rtn= str(content['detail_info'].get('taste_rating',''))
                        srv_rtn = str(content['detail_info'].get('service_rating',''))
                        envir_rtn = str(content['detail_info'].get('environment_rating',''))
                        #print "envir_rtn"
                        img_num = str(content['detail_info'].get('image_num',''))
                        cmm_num = str(content['detail_info'].get('comment_num',''))
                        print "cmm_num"
                        shp_h = content['detail_info'].get('shop_hours','')
                        print "before toWrite"
                        #toWrite = name + ';' + lat + ';' + lng + ';' + addr + ';' + uid + ';' + tag + ';' + typ + ';' + price + ';' + ovr_rtn + ';' + img_num + ';' + cmm_num + '\n'
                        toWrite = name + ';' + lat + ';' + lng + ';' + addr + ';' + uid + ';' + tag + ';' + typ + ';' + price + ';' + ovr_rtn + ';' +tst_rtn + ';'+  srv_rtn+';'+ envir_rtn +';'+img_num + ';' + cmm_num +shp_h +';'+ '\n'
                        print "after toWrite"
                    else:
                        print "else before toWrite"
                        toWrite = name + ';' + lat + ';' + lng + ';' + addr + ';' + uid + '\n'         
                        print "else before toWrite"
                except Exception,e:
                        
                        print str(e)
                        toWrite = 'No Data'
                
                    
                d.write(toWrite.encode('utf-8') + '\n')
                print "end of for loop"
                print "***************"
                print "^^^^^^^^^^^^^^^"
        d.close()
                
            #f = open(fileWrite, 'a')
        #f.close()    

tea_house1 = Pri_info("甜品","dessert")
tea_house1.write()
tea_house = Detailed_info("甜品","dessert")           
tea_house.write()                    
                
            
        
