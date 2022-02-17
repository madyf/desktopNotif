from email import header
import webbrowser
import requests
from bs4 import BeautifulSoup
import datetime
import time
from win10toast_click import ToastNotifier


URL = "https://www.cbc.ca/news"
page = requests.get(URL)

def open_url(website_url):
    try:
        webbrowser.open_new(website_url)
        print('opening url....')
    except:
        print('didnt work')

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
    news_articles = soup.find_all('a', {'data-test' : 'type-story'})
    # news_title = news_articles.findChildren()
    # time = soup.find_all('a').find('time')
    toaster = ToastNotifier()

    for article in news_articles:
        news_link = article['href']
        news_time = article.findChild('time')

        toaster.show_toast(title=article.text,
        msg=news_time.text,
        icon_path=None,
        duration=10,
        threaded=False,
        callback_on_click=lambda : open_url('https://www.cbc.ca' + news_link))
