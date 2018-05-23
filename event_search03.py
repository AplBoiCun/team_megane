import urllib
from urllib import request,parse
import json

url = 'http://api.atnd.org/events/?'

param = {
    #'area':'1',  #北海道
    'ym': '201805',       #イベント年月
    'count': '100',        #表示件数
    'format': 'json'
}

paramStr = urllib.parse.urlencode(param)
#print(paramStr)

readObj = urllib.request.urlopen(url + paramStr)

res = readObj.read().decode()

data =json.loads(res)
#print(data)
event_info=data['events']
#print(type(event_info))
#print(event_info)
#print(event_info['title'])
for k in range(0,len(event_info)):
    print(event_info[k]['event']['title'])   #イベント名
    print(event_info[k]['event']['started_at'])  #イベント開始日
    print(str(event_info[k]['event']['lat']) + " " + str(event_info[k]['event']['lon']))       #イベント場所
    #print(event_info[k]['event']['description'])  #イベントカテゴリー
    print()

