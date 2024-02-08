import requests
import json

response = requests.get(f"https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={input()}&format=json")

# print(response, type(response))
# print(response.status_code)
# print(response.reason)
# print(response.content)

if response:
    print(response)
    json_response = response.json()
    toponym = json_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
    toponym_name = toponym['metaDataProperty']['GeocoderMetaData']['Address']['formatted']
    toponym_coord = toponym['Point']['pos']
    print(f'{toponym_name} имеет координаты: {toponym_coord}')
else:
    print('Error!')
    print(response)
    print(f'HTTP status: {response.status_code}({response.reason})')