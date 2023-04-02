import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

final_df = pd.DataFrame(columns=['HCP name', 'HCP spec', 'HCO name', 'HCO address'])
page = requests.get('https://www.arztsuche-bw.de/index.php?suchen=1&offset=+60&id_z_arzt_praxis=0&id_fachgruppe=0&id_zusatzbezeichnung=0&id_genehmigung=0&id_dmp=0&id_zusatzvertraege=0&id_sprache=0&vorname=&nachname=&arztgruppe=alle&geschlecht=alle&wochentag=alle&zeiten=alle&fa_name=&plz=&ort=&strasse=&schluesselnr=&schluesseltyp=lanr7&landkreis=&id_leistungsort_art=0&id_praxis_zusatz=0&sorting=name&direction=ASC&checkbox_content=&name_schnellsuche=&fachgebiet_schnellsuche=', 'html.parser')
soup = BeautifulSoup(page.content, features='html.parser')
result_list = soup.find(attrs={'class': 'resultlist cols4 asu'})
for child in result_list.children:
    new_row = {}
    # for tag in child.find_all_next({'class': 'name'}):
    name = child.find_next('dd', {'class': 'name'}).find('dt').text
    new_row['HCP name'] = name
    qual = child.find_next('dd', {'class': 'qualifikation'}).find('dd').text
    new_row['HCP spec'] = qual
    address = child.find_next('dd', {'class': 'adresse'}).getText(strip=True,
                                                                  separator='\n').splitlines()  # .find('br')
    HCO_name = address[0]
    new_row['HCO name'] = HCO_name
    HCO_address = address[1:3]
    new_row['HCO address'] = HCO_address
    final_df = final_df.append(new_row, ignore_index=True)
    print(final_df)


final_df.to_csv('out_test3.csv', encoding='utf-16')

#print(soup.find_all(attrs={'class': 'row resultrow odd'}))