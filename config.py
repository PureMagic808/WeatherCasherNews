import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEATHER_API = os.getenv("OPENWEATHER_API_KEY")
NEWS_API = os.getenv("NEWS_API_KEY")
