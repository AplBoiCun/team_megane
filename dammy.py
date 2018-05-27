import json

f = open('event_db.json')
data = json.load(f)
places = data['event_table']
f.close

