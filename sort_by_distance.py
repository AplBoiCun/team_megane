from math import sin, cos, sqrt, atan2, radians
import get_location as gl

#places = [{'title': '北海道', 'latitude': 22, 'longitude': 139}, {'title': '沖縄', 'latitude': 23, 'longitude': 140}, {'title': '東京', 'latitude': 21,'longitude': 150}]


def get(places,postcode):
    geocoding = gl.get(postcode)

    for i in range(0, len(places)):
        try:
            # approximate radius of earth in km
            R = 6373.0
            
            lat1 = radians(geocoding['lat'])
            lon1 = radians(geocoding['lng'])
            lat2 = radians(float(places[i]['latitude']))
            lon2 = radians(float(places[i]['longitude']))

            dlon = lon2 - lon1
            dlat = lat2 - lat1

            a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))

            distance = R * c
            
            places[i]['distance'] = distance
    
        except:
            places[i]['distance'] = 20000
            continue
            

    places.sort(key=lambda x: x['distance'])

    return places
