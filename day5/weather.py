import requests
import json
from pprint import pprint

s='ab' 'bc'
print(s)
print('--------第一チェック----------')
url = ('https://api.openweathermap.org/data/2.5/weather'
        '?q={city}&appid={key}&lang=ja&units=metric')
url = url.format(city='Tokyo,JP',key='8221af5f0f8cf8040f060a7321ef09bd')
jsondata=requests.get(url).json()
pprint(jsondata)
print('--------第二チェック----------')

url = ('https://api.openweathermap.org/data/2.5/weather'
        '?q={zip}&appid={key}&lang=ja&units=metric')
url = url.format(zip='170-0001,JP',key='8221af5f0f8cf8040f060a7321ef09bd')
jsondata = requests.get(url).json()

print('都市名:',jsondata['name'])
print('気温:',jsondata['main']['temp'])
print('天気:',jsondata['weather'][0]['main'])
print('天気詳細:',jsondata['weather'][0]['description'])
