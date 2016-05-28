# -*- coding: utf-8 -*-
import urllib2
import json
import time

baseURL = 'http://api.map.baidu.com/geocoder/v2/?address='
ak = '&output=json&ak=g1m6DeA6pc0ToMr2wZeFF5q6Ob1hH2R3&callback=showLocation'

file_write = "C:\Users\Administrator\Desktop\\bizdata1.txt"
f= open(file_write, 'r')
uid = f.readline()


print uid

def fetch(url):
    feedback = urllib2.urlopen(url)
    data = feedback.read()
    response = json.loads(data)
    #time.sleep(0.3)
    return response
    

    
    