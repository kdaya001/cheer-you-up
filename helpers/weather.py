import requests
import os

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

def get_location(ip):
    response = requests.get(f'http://ip-api.com/json/{ip}')
    json = response.json()
    if json['status'] != 'success':
        return None
    else:
        return json['city']

def get_weather(city):
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}'
    response = requests.get(api_url)
    json = response.json()
    print(json)
    return json