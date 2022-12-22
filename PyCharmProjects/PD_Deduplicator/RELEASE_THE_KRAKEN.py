import pandas as pd
import requests
from bs4 import BeautifulSoup



#webpage = requests.get('https://preprod.webapp.peakdata.com/fr-azsaphnelo/person-details/3520#publications', 'html5lib')
#soup = BeautifulSoup(webpage.content)
#print(webpage)
# INPUT HERE KEYWORDS TO INCLUDE AND EXCLUDE FROM SEARCH
keywords_incl = []
keywords_excl = ['biolog', 'chemistry', 'anesthesia', 'gynecolog', 'Gynecolog']
result = []

links = pd.read_excel('_input/input_links.xlsx')
link_index = links.loc[links['Name'] == 'missing a publication?'].index.tolist()[0]
links = links[link_index + 1:].reset_index(drop=True)
jp = pd.read_excel('_input/input_jp.xlsx')

publications = jp.loc[lambda row: row.index % 2 == 0].reset_index(drop=True)
journals = jp.loc[lambda row: row.index % 2 == 1].reset_index(drop=True)

merged = pd.merge(links, publications, left_index=True, right_index=True)
merged = merged.merge(journals, left_index=True, right_index=True).drop(columns='Name'). \
    rename(columns={'Links': 'Link', 'title (DON’T TOUCH IT)_x': 'Publication', 'title (DON’T TOUCH IT)_y': 'Journal'})
merged.to_excel('_output/out.xlsx')
#print(merged.head())

def checker(check_j, check_p):
    for word in keywords_incl:
        if check_j.find(word) > -1 or check_p.find(word) > -1:
            return 'Good Match'
    for word in keywords_excl:
        if check_j.find(word) > -1 or check_p.find(word) > -1:
            return 'Delete'


merged['Check'] = merged.apply(lambda x: checker(x.Journal, x.Publication), axis=1)
merged.to_excel('_output/out_checked.xlsx')

for elem in merged.loc[merged['Check'] == 'Delete']['Link'].tolist():
    result.append(elem.replace('https://pubmed.ncbi.nlm.nih.gov/', ''))

with open('_output/result.txt', 'w') as file:
    file.write(str(result))

