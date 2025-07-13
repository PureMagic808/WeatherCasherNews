import requests

def get_currency():
    url = "https://api.exchangerate.host/latest?base=USD&symbols=RUB,EUR"
    response = requests.get(url).json()
    usd_rub = response["rates"]["RUB"]
    usd_eur = response["rates"]["EUR"]
    return f"💵 Курсы валют:\n1 USD = {usd_rub:.2f} RUB\n1 USD = {usd_eur:.2f} EUR"
