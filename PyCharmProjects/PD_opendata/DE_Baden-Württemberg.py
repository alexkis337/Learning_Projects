import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://www.arztsuche-bw.de/index.php?suchen=1&offset=40&id_z_arzt_praxis=0&id_fachgruppe=0&id_zusatzbezeichnung=0&id_genehmigung=0&id_dmp=0&id_zusatzvertraege=0&id_sprache=0&vorname=&nachname=&arztgruppe=alle&geschlecht=alle&wochentag=alle&zeiten=alle&fa_name=&plz=&ort=&strasse=&schluesselnr=&schluesseltyp=lanr7&landkreis=&id_leistungsort_art=0&id_praxis_zusatz=0&sorting=name&direction=ASC&checkbox_content=&name_schnellsuche=&fachgebiet_schnellsuche=', 'html.parser')
soup = BeautifulSoup(page.content, features='html.parser')

#for parent in soup.li.parents:
#    print(parent)

result_list = soup.find(attrs={'class': 'resultlist cols4 asu'})

for child in result_list.children:
    qual = child.find('dd', {'class': 'qualifikation'})
    name = child.find('dd', {'class': 'name'})
    adr  = child.find('dd', {'class': 'adresse'})
    #doc = dd.find(attrs={'class': 'name'})
    print(name, qual, adr, '\n')

#print(soup.find_all(attrs={'class': 'row resultrow odd'}))