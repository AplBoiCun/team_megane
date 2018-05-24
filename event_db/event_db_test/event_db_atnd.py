import urllib
from urllib import request,parse
import json
from tinydb import TinyDB, Query

db = TinyDB('event_db03.json')                  #データベース作成
db.purge_tables()                       #テーブル初期化

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
    db.insert({
              'title':event_info[k]['event']['title'],
              'started_at':event_info[k]['event']['started_at'],
              'latitude':str(event_info[k]['event']['lat']),
              'longitude':str(event_info[k]['event']['lon']),
              'description':event_info[k]['event']['description']
              })

for item in db:
    print(item)
    print()
    print()


