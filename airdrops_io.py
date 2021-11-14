from bs4 import BeautifulSoup
import requests
from send_telegram import send_message

url = "https://airdrops.io/latest/"
req = requests.get(url)


soup = BeautifulSoup(req.text, "html.parser")
all_articles = soup.find('div', {'class': 'airdrops-shortcoded airdrop-hover'})
for article in all_articles.find_all('article'):
    span_val = article.find_all('span')[0] if len(article.find_all('span')) == 1 else article.find_all('span')[1]
    print(span_val.contents[0])
    title = article.find('h3').contents[0]
    text = article.find('div', {'class': 'inside-article'})['onclick'].split("'")[1].split("'")[0] + '\n' + \
           span_val.contents[0]
    print(article.find('h3').contents[0])
    print(article.find('div', {'class': 'inside-article'})['onclick'].split("'")[1].split("'")[0])
    send_message(title, text)
    print('----------')