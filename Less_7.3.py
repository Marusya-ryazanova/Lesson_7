import requests
import datetime
import pandas as pd
API_KEY = 'f9ada9efec6a3934dad5f30068fdcbb8'
city_name = input('Please enter your city name:')
cnt = int(input('Please enter the quantity of days:'))
request = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?',
                           params={'q': city_name, 'cnt': cnt, 'appid': API_KEY})
data = request.json()

print(data)

data_table=pd.DataFrame.from_dict(data['list'], orient='columns')
print(data_table)

data_table2=data_table[["dt","temp","feels_like"]]
print(data_table2)

data_table3=pd.DataFrame([data_table2], columns=data_table2.keys())
print(data_table3)

