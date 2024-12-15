import requests
import json

WEATHER_API_KEY = "eddacab204556abb88fa48befcf38e02"
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(village_name):
    params = {
        'q': village_name,
        'appid': WEATHER_API_KEY,
        'units': 'metric'
    }
    response = requests.get(WEATHER_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather(weather_data):
    if weather_data:
        temp = weather_data['main']['temp']
        rain = weather_data['weather'][0]['description']
        print(f"Temperature: {temp}°C")
        print(f"Weather: {rain}")
    else:
        print("Could not retrieve weather data")

def main():
    village_name = "Hicksville,NY,usa"
    weather_data = get_weather(village_name)
    display_weather(weather_data)

if __name__ == "__main__":
    main()