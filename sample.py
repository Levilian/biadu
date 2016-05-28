import urllib2
import json


# This part is to test place detail API
# Set base url
baseURL = 'http://api.map.baidu.com/geocoder/v2/?address='
ak = '&output=json&ak=g1m6DeA6pc0ToMr2wZeFF5q6Ob1hH2R3&callback=showLocation'

# Set working path
path2 = 'C:\Users\Administrator\Desktop\\'

# Read coordinate file of Shenzhen
coordinateFile = open(path2 + 'Sites_Cors.txt', 'rb')
fileWrite = path2 + 'Sites_Cors.txt'
coordinates = coordinateFile.readlines()
coordinates.pop(0)


# Define fetch
def fetch(url):
    feedback = urllib2.urlopen(url)
    data = feedback.read()
    response = json.loads(data)

    return response

startPage = 0

# Loop the coord file
with open(fileWrite, 'a') as f:
    for c in range(startPage, len(coordinates)):
        coord = coordinates[c].split(',')
        lat = coord[2].strip()
        lng = coord[1].strip()
        locator = coord[0]
        print 'This is ' + str(locator) + ' of ' + str(len(coordinates))

        initialURL = baseURL + 'ak=' + ak + '&query=' + query + '&scope=' + scope + '&location=' + \
                     lat + ',' + lng + '&radius=750' + '&page_size=20&page_num=0'


        try:
            response = fetch(initialURL)
            totalNum = response['total']
            numPages = totalNum/20
            print numPages
            for i in range(numPages+1):
                print 'this is page ' + str(i)
                URL = baseURL + 'ak=' + ak + '&query=' + query + '&scope=' + scope + '&location=' + lat + ',' + lng + \
                      '&radius=750' + '&page_size=20&page_num=' + str(i)
                response = fetch(URL)
                contents = response['results']
                for content in contents:
                    name = content['name']
                    lat = str(content['location']['lat'])
                    lng = str(content['location']['lng'])
                    uid = str(content['uid'])
                    try:
                        price = str(content['detail_info']['price'])
                    except:
                        price = 'no data'

                    toWrite = name + ';' + lat + ';' + lng + ';' + uid + ';' + price
                    print toWrite
                    f.write(toWrite.encode('utf-8') + '\n')
        except:
            continue

        f.close()
        f = open(fileWrite, 'a')
    f.close()
