from bs4 import BeautifulSoup
import requests
url = "https://airdrops.io/latest/"
req = requests.get(url)


soup = BeautifulSoup(req.text, "html.parser")
all_articles = soup.find('div', {'class': 'airdrops-shortcoded airdrop-hover'})
for article in all_articles.find_all('article'):
    print(article.find('h3').contents[0])
    print(article.find('div', {'class': 'inside-article'})['onclick'].split("'")[1].split("'")[0])
    span_val = article.find_all('span')[0] if len(article.find_all('span')) == 1 else article.find_all('span')[1]
    print(span_val.contents[0])
    print('----------')