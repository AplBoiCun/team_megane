import urllib
from urllib import request,parse
import json

url = 'http://eventon.jp/api/events.json?'

param = {
  #'prefecture_id':'1',  #北海道
  'ym': '201805',       #イベント年月日
  'limit': '10',        #表示件数
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
    print(event_info[k]['title'])   #イベント名
    print(event_info[k]['started_at'])  #イベント開始日
    print(event_info[k]['lat'] + " " + event_info[k]['lng'])       #イベント場所
    print(event_info[k]['categories'])  #イベントカテゴリー
    print()
