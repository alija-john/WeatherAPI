import json       # json and request are the libraries needed 
import requests

# API - to fetch temperature of a city

city_name = input('Enter a City Name : ')

api_key = '1afcbb961aa976067177e6d455b54a9e'

#To build the API URL
api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'


get_server_information = requests.get(api_url)

json_data = get_server_information.json()



# for arranging the data in good format

pretty_data = json.dumps(json_data,indent=4)
print(pretty_data)

#to fetch specific data from json

D = json_data["weather"][0]['description']
#print(D)

T = json_data["main"]["temp"]
#print(T)

print(f'The current weather Description is : {D} &  Temperature is : {T} ')
