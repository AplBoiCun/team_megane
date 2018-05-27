# coding:utf-8

from urllib import request,parse
import json
import get_location as gl


f = open('main_db.json')
data = json.load(f)
places = data['event_table']
f.close


yourPlace = {'lat': gl.geocoding['lat'], 'lng': gl.geocoding['lng']}

url = 'http://vldb.gsi.go.jp/sokuchi/surveycalc/surveycalc/bl2st_calc.pl?'

distance = {}               # 距離の辞書

for i in range(0, len(places)):
    if str(i) not in places or len(places[str(i)]['latitude']) == 0:
        continue
    else:
        param = {
        'outputType': 'json',
        'ellipsoid':  'bessel',
        'latitude1': yourPlace['lat'],            # 使用者の緯度
        'longitude1': yourPlace['lng'],          # 使用者の経度
        'latitude2': places[str(i)]['latitude'],            # 比較地点の緯度
        'longitude2': places[str(i)]['longitude'],          # 比較地点の経度
        }
        paramStr = parse.urlencode(param)
        readObj = request.urlopen(url + paramStr)
        res = readObj.read().decode()
        calc =json.loads(res)
        print(calc)
        distance[str(i)] = calc['OutputData']['geoLength']  # ２点間の距離(KM)を追加

distance = sorted(distance.items())

for k in range(0, len(distance)):
    print(places[str(distance[k])]['title'])
    print(places[str(distance[k])]['distance'])
    print()
