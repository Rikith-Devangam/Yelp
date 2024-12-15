import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import requests


WEATHER_API_KEY = "eddacab204556abb88fa48befcf38e02"
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"


MENU = {
    "Butter Chicken": 12,
    "Paneer Tikka": 10,
    "Biryani": 15,
    "Naan Basket": 8
}

""" Training og the model """
data = {
    'temp': [32, 45, 50, 60, 35, 55, 40, 70, 65, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125], # temp in Fahrenheit
    'weather': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], # 1: Snow/Rain, 0: Clear
    'current_people': [50, 100, 30, 150, 75, 60, 90, 120, 110, 130, 140, 160, 170, 180, 190, 200, 210, 220, 230, 240],  # Number of people
    'price_multiplier': [0.95, 1.5, 0.8, 1.5, 1, 1.2, 0.9, 1.3, 1.1, 1.4, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5] # Price multiplier based on conditions
}


df = pd.DataFrame(data)

X = df[['temp', 'weather', 'current_people']]
y = df['price_multiplier']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train, y_train)
"""End of training"""


def predict_price(temp_fahrenheit, weather, current_people):
    input_data = np.array([[temp_fahrenheit, weather, current_people]])
    input_data = scaler.transform(input_data)
    price_multiplier = model.predict(input_data)[0]
    predicted_prices = {item: price * price_multiplier for item, price in MENU.items()}
    return predicted_prices

def get_weather(location):
    params = {"q": location, "appid": WEATHER_API_KEY}
    response = requests.get(WEATHER_URL, params=params)
    data = response.json()
    kelvin_temp = data["main"]["temp"]
    fahrenheit_temp = (kelvin_temp - 273.15) * 9/5 + 32
    weather = data["weather"][0]["main"].lower()
    return fahrenheit_temp, weather

#hard coded values for testing the model
#menu price is also hard coded

VILLAGE_LOCATION = "Hicksville,NY,usa"
temp, weather = get_weather(VILLAGE_LOCATION)

if weather == "rain" or weather == "snow":
    weather_code = 1
else:
    weather_code = 0
current_people = 150

predicted_prices = predict_price(temp, weather_code, current_people)
print("\n")

print("Current prices:")
for i in MENU:
    print(i,MENU[i])
print("\n")
print(f"Predicted prices for {VILLAGE_LOCATION} in current temperature: {temp:.2f}°F, weather: {weather}, current people: {current_people}")
for item, price in predicted_prices.items():
    print(f"{item}: ${price:.2f}")