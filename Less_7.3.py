import requests
import datetime
import pandas as pd
API_KEY = 'f9ada9efec6a3934dad5f30068fdcbb8'
city_name = input('Please enter your city name:')
cnt = int(input('Please enter the quantity of days:'))
request = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?', params={'q': city_name, 'cnt': cnt, 'appid': API_KEY, 'units': 'metric'})
data = request.json()
print(data)

df2 = pd.json_normalize(data['list'])

df2=df2[["dt","temp.day","feels_like.day"]]
df2.head()

from datetime import datetime
df2['dt']=pd.to_datetime(df2['dt'], unit='ms')
df2.head()

df2['dt']=pd.to_datetime(df2['dt'])