from email import header
import webbrowser
import requests
from bs4 import BeautifulSoup
import datetime
import time
from win10toast import ToastNotifier


URL = "https://www.cbc.ca/news"
page = requests.get(URL)

if page.status_code == 403:
    browser_str = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
    headers = {
        'User-Agent': 
        browser_str
        }
    page = requests.get(URL, headers=headers)


if page.status_code == 200:
    print(page.status_code)
    soup = BeautifulSoup(page.content, 'html.parser')
    news_articles = soup.find_all('h3', class_='headline')
    toaster = ToastNotifier()

    for article in news_articles:
        # news_link = article.find('href')
        # news_title = article.find('h3')
        toaster.show_toast(title="News",
        msg=article.text,
        duration=10)
        # print(news_link)
        # print(news_title)
        # print(article.text)
