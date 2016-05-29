# -*- coding: utf-8 -*-
import urllib2
import json

baseURL = "http://api.map.baidu.com/geocoder/v2/?address="
ak = "&output=json&ak=g1m6DeA6pc0ToMr2wZeFF5q6Ob1hH2R3"

file_write = "C:\Users\Administrator\Desktop\\bizdata1.txt"
f= open(file_write, 'r')
address = f.readlines()
address.pop(0)

def fetch(url):
    response = urllib2.urlopen(url)
    data = response.read()
    parsedData = json.loads(data)
    return parsedData


fileWrite = "C:\Users\Administrator\Desktop\\try.txt"


    
with open(fileWrite, 'w') as f:
    for u in range(0,len(address)):
        
        single_ln = address[u].split(',')
        single_address = single_ln[1]
        uid = single_ln[0]
        url = baseURL + single_address.strip() + ak
        print url
        
        try:
            response = fetch(url)
            content = response['result']
            lat = str(content['location']['lat'])
            lng = str(content['location']['lng']) 
            pre = str(content['precision'])
            confi = str(content['confidence'])
            #if content['detail'].isequal(1):
            toWrite = str(uid) + ';' + lat + ';' + lng + pre + ';' + confi + '\n'
            
        except:
            toWrite = str(uid)
            print('no data')
        
        f.write(toWrite.encode('utf-8') + '\n')

f.close()
        
    #f = open(fileWrite, 'a')
#f.close()    
            
            
            
        
    

