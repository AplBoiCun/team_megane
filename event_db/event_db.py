from urllib import request, parse
import json
from datetime import datetime, date, timedelta
from tinydb import TinyDB

# eventon
def eventon(db, day):
    url_eventon = 'http://eventon.jp/api/events.json?'
    param_eventon = {
        'ymd': day,       # イベント年月日範囲
        'limit': '100',        # 表示件数
    }
    paramStr_eventon = parse.urlencode(param_eventon)
    readObj_eventon = request.urlopen(url_eventon + paramStr_eventon)
    res_eventon = readObj_eventon.read().decode()
    data_eventon = json.loads(res_eventon)
    event_info_eventon = data_eventon['events']
    for k in range(0, len(event_info_eventon)):
        db.insert({
                  'service': 'eventon',
                  'title': event_info_eventon[k]['title'],
                  'started_at': event_info_eventon[k]['started_at'],
                  'latitude': event_info_eventon[k]['lat'],
                  'longitude': event_info_eventon[k]['lng'],
                  'tag': event_info_eventon[k]['categories']
                  })


# attend API
def attend(db, day):
    url_atnd = 'http://api.atnd.org/events/?'
    param_atnd = {
        # 'area':'1',  #北海道
        'ymd': day,       # イベント年月
        'count': '100',        # 表示件数
        'format': 'json'
    }
    paramStr_atnd = parse.urlencode(param_atnd)
    readObj_atnd = request.urlopen(url_atnd + paramStr_atnd)
    res_atnd = readObj_atnd.read().decode()
    data_atnd = json.loads(res_atnd)
    event_info_atnd = data_atnd['events']
    for k in range(0, len(event_info_atnd)):
        db.insert({
                  'service': 'atnd',
                  'title': event_info_atnd[k]['event']['title'],
                  'started_at': event_info_atnd[k]['event']['started_at'],
                  'latitude': str(event_info_atnd[k]['event']['lat']),
                  'longitude': str(event_info_atnd[k]['event']['lon']),
                  'tag': event_info_atnd[k]['event']['description']
                  })


# connpass API
def connpass(db, day):
    url = 'https://connpass.com/api/v1/event/?'
    param = {
        'ymd': day,
        'count': '100'
    }
    readObj = request.urlopen(url + parse.urlencode(param))

    res = readObj.read().decode()

    data = json.loads(res)

    event_info = data['events']

    for k in range(0, len(event_info)):
        db.insert({
            'service': 'connpass',
            'title': event_info[k]['title'],
            'catch': event_info[k]['catch'],
            'description': event_info[k]['description'],
            'event_url': event_info[k]['event_url'],
            'started_at': event_info[k]['started_at'],
            'ended_at': event_info[k]['ended_at'],
            'address': event_info[k]['address'],
            'place': event_info[k]['place'],
            'latitude': event_info[k]['lat'],
            'longitude': event_info[k]['lon']
        })

def main():
    db = TinyDB('event_db.json')                  # データベース作成
    db.purge_tables()
    for i in range(14):
        day = datetime.strftime((date.today()+timedelta(days=i)),"%Y%m%d")
        eventon(db, day)
        attend(db, day)
        connpass(db, day)

if __name__ == "__main__":
    main()


# for item in db:
#   print(item)
#   print()
#   print()
