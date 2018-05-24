import urllib
from urllib import request,parse
import json
from tinydb import TinyDB, Query

db = TinyDB('event_db.json')                  #データベース作成
db.purge_tables()


url_eventon = 'http://eventon.jp/api/events.json?'
param_eventon = {
    'ymd_between': '20180528, 20180611',       #イベント年月日範囲
        'limit': '100',        #表示件数
}
paramStr_eventon = urllib.parse.urlencode(param_eventon)
readObj_eventon = urllib.request.urlopen(url_eventon + paramStr_eventon)
res_eventon = readObj_eventon.read().decode()
data_eventon =json.loads(res_eventon)
event_info_eventon=data_eventon['events']
for k in range(0,len(event_info_eventon)):
    db.insert({
              'title':event_info_eventon[k]['title'],
              'started_at':event_info_eventon[k]['started_at'],
              'latitude':event_info_eventon[k]['lat'],
              'longitude':event_info_eventon[k]['lng'],
              'tag':event_info_eventon[k]['categories']
              })


url_atnd = 'http://api.atnd.org/events/?'
param_atnd = {
    #'area':'1',  #北海道
    'ym': '201805',       #イベント年月
    'count': '100',        #表示件数
    'format': 'json'
}
paramStr_atnd = urllib.parse.urlencode(param_atnd)
readObj_atnd = urllib.request.urlopen(url_atnd + paramStr_atnd)
res_atnd = readObj_atnd.read().decode()
data_atnd =json.loads(res_atnd)
event_info_atnd=data_atnd['events']
for k in range(0,len(event_info_atnd)):
    db.insert({
              'title':event_info_atnd[k]['event']['title'],
              'started_at':event_info_atnd[k]['event']['started_at'],
              'latitude':str(event_info_atnd[k]['event']['lat']),
              'longitude':str(event_info_atnd[k]['event']['lon']),
              'tag':event_info_atnd[k]['event']['description']
              })

#for item in db:
#   print(item)
#   print()
#   print()



