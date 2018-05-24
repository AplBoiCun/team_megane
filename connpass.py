
from urllib import parse, request
import json
from datetime import datetime, date, timedelta
from tinydb import TinyDB

db = TinyDB('event_db01.json')                  # データベース作成
db.purge_tables()

url = 'https://connpass.com/api/v1/event/?'
days = ""
for i in range(14):
    days += datetime.strftime((date.today()+timedelta(days=i)),"%Y%m%d")+","
days = days[:-1]

param = {
    'ymd': days,
}

readObj = request.urlopen(url + parse.urlencode(param))

res = readObj.read().decode()

data = json.loads(res)

event_info = data['events']

for k in range(0, len(event_info)):
    db.insert({
    'title': event_info[k]['title'],
    'catch': event_info[k]['catch'],
    'description': event_info[k]['description'],
    'event_url': event_info[k]['event_url'],
    'started_at': event_info[k]['started_at'],
    'ended_at': event_info[k]['ended_at'],
    'address': event_info[k]['address'],
    'place': event_info[k]['place'],
    'latitude': event_info[k]['lat'],
    'longitude': event_info[k]['lon'],
    })

for item in db:
    print(item)
