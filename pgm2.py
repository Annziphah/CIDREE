"""2. API Integration
You have to build a Python script that pulls weather data from an API and stores only temperature
and humidity in a CSV file every hour."""
import requests
import csv
import time
urll = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=your_api_key&units=metric"
with open("weather_data.csv", mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["temperature", "humidity"])  
while True:
    response = requests.get(urll)
    data = response.json()
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    with open("weather.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([temp, humidity])
    time.sleep(3600)  
