import requests
from config import NEWS_API

def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=ru&pageSize=3&apiKey={NEWS_API}"
    response = requests.get(url).json()
    articles = response.get("articles", [])
    if not articles:
        return "❌ Новости не найдены."

    result = "📰 Топ 3 новости:\n\n"
    for article in articles:
        title = article["title"]
        link = article["url"]
        result += f"• <a href='{link}'>{title}</a>\n"
    return result
