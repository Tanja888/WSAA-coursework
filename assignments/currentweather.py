# Assignment: Current weather
# Write a python program called currentweather.py that will print out:
# the current temperature on the console (and only the temperature)
# Also print the current wind direction (10m) from: https://open-meteo.com/
# Author: Tanja Juric

import requests
import json

url1 = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m,wind_speed_10m"
response = requests.get(url1)
# print(response)
data = response.json()

current = data["current"]
temperature = current["temperature_2m"]
print("Current temperature:", temperature)


url2 = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m,wind_direction_10m&forecast_days=1"
response = requests.get(url2)
# print(response)
data = response.json()

current = data["current"]
#temperature = current["temperature_2m"]
wind_direction = current["wind_direction_10m"]
print("Wind direction 10m:", wind_direction )
