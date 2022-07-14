import requests
import json
from datetime import datetime,timedelta,timezone

url = ('https://api.openweathermap.org/data/2.5/forecast'
'?q={city}&appid={key}&lang=ja&units=metric')
url = url.format(city='Tokyo,JP',key='8221af5f0f8cf8040f060a7321ef09bd')
jsondata = requests.get(url).json()

print(url)

tz=timezone(timedelta(hours = +9),'JST')
for dat in jsondata['list']:
    jst=str(datetime.fromtimestamp(dat['dt'],tz))[:-14]
    weather=dat['weather'][0]['description']
    temp=dat['main']['temp']
    print(f'日時:{jst},天気:{weather},気温:{temp}度')
"""
tz=timezone(timedelta(hours = +9),'JST')
for dat in jsondata['list']:
    jst = str(datetime.fromtimestamp(dat['dt'],tz))[:-9]
    weather = dat['weather'][0]['description']
    temp = dat['main']['temp']
    print(f'日時:{jst},天気:{weather},気温:{temp}度')
"""
