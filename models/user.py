import database
import requests
import os

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

def insert_user(first_name, last_name, email, hashed_password, avatar):
    database.sql_write('INSERT INTO users (first_name, second_name, password, email, avatar_url) VALUES (%s, %s, %s, %s, %s) RETURNING id', [first_name, last_name, hashed_password, email, avatar])

def get_user_by_email(email):
    return database.sql_select('SELECT * FROM users WHERE email = %s', [email])

def get_user(user_id):
    return database.sql_select('SELECT * FROM users WHERE id = %s', [user_id])

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
    return json['weather'][0]['icon']