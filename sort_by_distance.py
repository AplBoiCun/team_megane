# coding:utf-8

from urllib import request,parse
import json

places = [{'title': '北海道', 'lat': 22, 'lng': 139}, {'title': '沖縄', 'lat': 23, 'lng': 140}, {'title': '東京', 'lat': 21,'lng': 150}]
yourPlace = {'lat': 40, 'lng': 140}

url = 'http://vldb.gsi.go.jp/sokuchi/surveycalc/surveycalc/bl2st_calc.pl?'

distance = {}               # 距離の辞書

for i in range(0, len(places)):
    param = {
        'outputType': 'json',
        'ellipsoid':  'bessel',
        'latitude1': yourPlace['lat'],            # 使用者の緯度
        'longitude1': yourPlace['lng'],          # 使用者の経度
        'latitude2': places[i]['lat'],            # 比較地点の緯度
        'longitude2': places[i]['lng'],          # 比較地点の経度
    }
    paramStr = parse.urlencode(param)
    readObj = request.urlopen(url + paramStr)
    res = readObj.read().decode()
    data =json.loads(res)
#distance[str(places[i]['title'])] = data['OutputData']['geoLength']    # ２点間の距離(KM)をtitleと共に追加
    places[i]['distance'] = data['OutputData']['geoLength']
#print(distance)

places.sort(key=lambda x: x['distance'])

for k in range(0, len(places)):
    print(places[k]['title'])
    print(places[k]['distance'])
    print()

