# coding:utf-8

from urllib import request,parse
import json
import get_location as gl

#places = [{'title': '北海道', 'latitude': 22, 'longitude': 139}, {'title': '沖縄', 'latitude': 23, 'longitude': 140}, {'title': '東京', 'latitude': 21,'longitude': 150}]


def get(places,postcode):

    geocoding = gl.get(postcode)
    yourPlace = {'lat': geocoding['lat'], 'lng': geocoding['lng']}
    print('aho')
    url = 'http://vldb.gsi.go.jp/sokuchi/surveycalc/surveycalc/bl2st_calc.pl?'


    for i in range(0, len(places)):
        if places[i]['latitude'] == '':
            continue
        else:
            param = {
                'outputType': 'json',
                'ellipsoid':  'bessel',
                'latitude1': yourPlace['lat'],            # 使用者の緯度
                'longitude1': yourPlace['lng'],          # 使用者の経度
                'latitude2': places[i]['latitude'],            # 比較地点の緯度
                'longitude2': places[i]['longitude'],          # 比較地点の経度
            }
            paramStr = parse.urlencode(param)
            readObj = request.urlopen(url + paramStr)
            res = readObj.read().decode()
            data_distance =json.loads(res)
            print(data_distance)
            places[i]['distance'] = data_distance['OutputData']['geoLength']      # ２点間の距離(M)を追加
                #print(distance)

    places.sort(key=lambda x: x['distance'])

    for k in range(0, len(places)):
        print(places[k]['title'])
        print(places[k]['distance'])
        print()

#get(places)
