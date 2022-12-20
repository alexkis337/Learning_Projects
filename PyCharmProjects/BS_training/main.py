from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

page = requests.get('https://trans.info/pl')
soup = bs(page.content, 'html.parser')

all_mts = soup.find_all(attrs={'class': 'article-intro-view_text'})
top_articles = []
for article in all_mts:
    top_articles.append(article.text)

images = []
for elem in soup.find_all(attrs={'class': 'cover-img zoomable darken'}):
    images.append(elem.get('src'))

print(top_articles)
print(images)

with open('result.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(top_articles))
    file.write('\n'.join(images))