import smtplib
import requests
import datetime as dt
MY_EMAIL = "Your EMAIL"
PASSWORD = "YOUR PASSWORD"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API = "KH52T15DIYISWNU3"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
api_key = "cdd22c10f6844220b33062e170c9cfc5"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": STOCK_API
}
news_params = {
    "apikey": api_key,
    "q": COMPANY_NAME
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
print(stock_response.json())
stock_data =stock_response.json()["Time Series (Daily)"]
stock_list = [value for (key, value) in stock_data.items()]
yesterday_price = stock_list[0]["4. close"]
before_yesterday_price = stock_list[1]["4. close"]
diff = abs(float(float(yesterday_price) - float(before_yesterday_price)))
diff_percent = round((diff / float(yesterday_price)) * 100,3)

if diff_percent > 0.1:
    new_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles =new_response.json()["articles"]
    three_articles = articles[:3]
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs="EMAIL ADDRESS",
                        msg=f"{three_articles[0]}")
    connection.sendmail(from_addr=MY_EMAIL, to_addrs="EMAIL ADDRESS",
                        msg=f"{three_articles[1]}")
    connection.sendmail(from_addr=MY_EMAIL, to_addrs="EMAIL ADDRESS",
                        msg=f"{three_articles[2]}")
    connection.quit()
    connection.close()

