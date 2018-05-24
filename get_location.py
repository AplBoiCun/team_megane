# coding:utf-8

from urllib import request,parse
import json


url_getTown = 'https://postcode-jp.appspot.com/api/postcode?'
param_getTown = {
    'postcode': '1130001'      # 郵便番号

}
paramStr_getTown = parse.urlencode(param_getTown)
#print(paramStr_getTown)
readObj_getTown = request.urlopen(url_getTown + paramStr_getTown)
res_getTown = readObj_getTown.read().decode()
data_getTown = json.loads(res_getTown)
town = data_getTown['data'][0]['allAddress']    # 市区町村名を入手
#print(town)


url = 'https://maps.googleapis.com/maps/api/geocode/json?'
param = {
    'address': town      # 上で得た市区町村を代入

}
paramStr = parse.urlencode(param)
#print(paramStr)
readObj = request.urlopen(url + paramStr)
res = readObj.read().decode()
data =json.loads(res)
#print(data)
geocoding = data['results'][0]['geometry']['location']
print(geocoding['lat'])
print(geocoding['lng'])
