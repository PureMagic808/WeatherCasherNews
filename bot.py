import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from config import BOT_TOKEN
from utils.currency import get_currency
from utils.weather import get_weather
from utils.news import get_news

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message(lambda msg: msg.text == "/start")
async def start(message: types.Message):
    await message.answer(
        "👋 Привет! Я бот.\n"
        "Вот что я умею:\n"
        "/currency — курс валют\n"
        "/weather <город> — погода\n"
        "/news — последние новости"
    )

@dp.message(lambda msg: msg.text == "/currency")
async def currency(message: types.Message):
    result = get_currency()
    await message.answer(result)

@dp.message(lambda msg: msg.text.startswith("/weather"))
async def weather(message: types.Message):
    try:
        city = message.text.split(maxsplit=1)[1]
        report = get_weather(city)
        await message.answer(report)
    except IndexError:
        await message.answer("❗ Укажи город: /weather Москва")

@dp.message(lambda msg: msg.text == "/news")
async def news(message: types.Message):
    headlines = get_news()
    await message.answer(headlines)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
