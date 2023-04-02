import pandas as pd
from bs4 import BeautifulSoup
import requests

df = pd.DataFrame(columns=['name', 'weight'])

for num in range(10):
    rp = 'http://rutor.info/search/' + str(num) + '/8/010/0/RPG'
    page = requests.get(rp, 'html.parser')
    soup = BeautifulSoup(page.content)

    for elem in soup.findAll('table')[2]:
        row = (elem.findAll('td')[1], elem.findAll('td')[3])
        df = df.append({'name': elem.findAll('td')[1].text, 'weight': elem.findAll('td')[3].text}, ignore_index=True)

#print(df)
df.to_excel('test.xlsx')

#for child in soup.tbody.children:
#    print(child)



#print(soup)