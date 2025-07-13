# 💬 Telegram-бот: Погода, Валюта и Новости

Простой Telegram-бот на Python, который по командам присылает:
- Текущий курс валют (USD → RUB, EUR)
- Погоду в указанном городе
- Последние новости в России

## 📦 Функции
- /start — справка
- /currency — курс валют
- /weather <город> — погода
- /news — топ-3 новостей

## 🛠️ Используемые технологии

| Задача                 | Библиотека / API             |
|------------------------|------------------------------|
| Telegram Bot           | aiogram                      |
| Работа с API           | requests                     |
| Переменные окружения   | python-dotenv                |
| Погода                 | OpenWeather API              |
| Валюта                 | Exchangerate.host            |
| Новости                | NewsAPI                      |

## 🚀 Установка и запуск

1. Клонируй проект:
```bash
git clone https://github.com/твой_ник/bot-currency-weather-news.git
cd bot-currency-weather-news
```

2. Установи зависимости:
```bash
pip install -r requirements.txt
```

3. Создай .env файл и добавь ключи:
```
BOT_TOKEN=твой_токен_бота
OPENWEATHER_API_KEY=твой_ключ_openweather
NEWS_API_KEY=твой_ключ_newsapi
```

4. Запусти бота:
```bash
python bot.py
```

## 📁 Структура проекта

```
project/
├── bot.py
├── config.py
├── .env
├── .gitignore
├── requirements.txt
├── utils/
│   ├── currency.py
│   ├── weather.py
│   └── news.py
```

## 🛡 Безопасность

- Все ключи хранятся в `.env`
- `.env` добавлен в `.gitignore`

## 🧠 Автор

Разработчик: [Твоё имя или никнейм]
Контакт: [Telegram или e-mail]

## ⭐ Лицензия

MIT License
