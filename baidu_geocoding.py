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


baseURL = 'http://api.map.baidu.com/geocoder/v2/?ak=g1m6DeA6pc0ToMr2wZeFF5q6Ob1hH2R3&output=json&address='
city = '&city=杭州市'
new_file_write = "C:\Users\Administrator\Desktop\\detailed" + 'public_choice_teahouse' +".txt"
file_write = "C:\Users\Administrator\Desktop\\" + 'public_choice_teahouse' +".txt"

f= open(file_write, 'r')
total_pri = f.readlines()
total_pri.pop(0)
with open(new_file_write, 'w+') as d:
    default = "id;address;latitude;longitude;precise;confidence"
    d.write(default.encode('utf-8') + '\n')
    for u in range(len(total_pri)):
        
        single_ln = total_pri[u].split(',')
        single_id = single_ln[0]
        single_address = single_ln[1].strip()
        #uid = single_ln[0]
        url = baseURL + single_address + city
        print single_id,single_address
            
        try:
            
            response = fetch(url)
            print response
            content = response['result']
            lat = str(content['location']['lat'])
            lng = str(content['location']['lng'])
            
            print "this is the " + str(u) + "th line of data"
            #print content
            pre = str(content['precise'])
            confi = str(content['confidence'])
            
            toWrite = str(single_id) + ';'+ single_address + ';' + lat + ';' + lng + ';' + pre + ';' + confi      
                
        except Exception,e:
                
                print str(e)
                toWrite = str(single_id) + ';' + single_address
        
            
        d.write(toWrite.encode('utf-8') + '\n')
        print "end of for loop"
        print "***************"
        print "^^^^^^^^^^^^^^^"
    
d.close()
