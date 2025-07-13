import requests
from config import WEATHER_API

def get_weather(city: str) -> str:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API}&units=metric&lang=ru"
    response = requests.get(url).json()

    if response.get("cod") != 200:
        return "❌ Город не найден."

    temp = response["main"]["temp"]
    desc = response["weather"][0]["description"]
    return f"🌤 Погода в {city.title()}:\n{temp}°C, {desc}"
