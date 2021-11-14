from bs4 import BeautifulSoup
import requests
url = "https://airdrops.io/latest/"
req = requests.get(url)


soup = BeautifulSoup(req.text, "html.parser")
show_more = soup.find('div', {'class': 'airdrops-shortcoded airdrop-hover'})
print(show_more)
# print(soup.find_all('div',{'class': 'inside-article'})[0])