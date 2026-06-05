import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5"

def get_current_weather(city):
    url = f"{BASE_URL}/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(url, params=params)    

    if response.status_code == 404:
        raise ValueError(f"City: '{city}' not found.")
    if response.status_code != 200:
        raise ConnectionError("Failed to fetch weather data.")
    
    return response.json()

def get_forecast(city):
    url = f"{BASE_URL}/forecast"
    params = {"q": city, "appid": API_KEY, "units": "metric", "cnt": 5}

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()