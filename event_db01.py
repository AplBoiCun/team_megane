import urllib
from urllib import request,parse
import json
from tinydb import TinyDB, Query

db = TinyDB('event_db01.json')                  #データベース作成
db.purge_tables()

url = 'http://eventon.jp/api/events.json?'

param = {
    #'prefecture_id':'1',  #北海道
    'ymd_between': '20180528, 20180611',       #イベント年月日範囲
        'limit': '100',        #表示件数
}

paramStr = urllib.parse.urlencode(param)
#print(paramStr)

readObj = urllib.request.urlopen(url + paramStr)

res = readObj.read().decode()

data =json.loads(res)

event_info=data['events']

for k in range(0,len(event_info)):
    db.insert({'title':event_info[k]['title'], 'started_at':event_info[k]['started_at'], 'latitude':event_info[k]['lat'], 'longitude':event_info[k]['lng'], 'tag':event_info[k]['categories']})

for item in db:
    print(item)
    print()
    print()
    #print(event_info[k]['title'])   #イベント名
    #print(event_info[k]['started_at'])  #イベント開始日
    #print(event_info[k]['lat'] + " " + event_info[k]['lng'])       #イベント場所
    #print(event_info[k]['categories'])  #イベントカテゴリー
    #print()

