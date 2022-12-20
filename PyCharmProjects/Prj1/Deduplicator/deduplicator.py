import pandas as pd


# define kw_list
kw_list = ['cancer', 'prostate', 'urolog']

# import publications and journals list and putting them in dataframe, so they are in 2 columns
publications = pd.read_csv('input_publications.csv', encoding='latin-1')

pubs = publications.iloc[::2]
journals = publications.iloc[1::2]

pubs_journals = pd.merge(pubs.reset_index(), journals.reset_index(), left_index=True,
                         right_index=True).reset_index().drop(columns=['index', 'index_x', 'index_y'])
pubs_journals.rename(columns={'name_x': 'pub', 'name_y': 'journal'}, inplace=True)
# pubs_journals.to_csv('test.csv')
print(pubs_journals)

# import links and leaving only PubMed_ID
links = pd.read_csv('input_links.csv')
links['link'] = links.apply(lambda text: text['link'].replace("https://pubmed.ncbi.nlm.nih.gov/", ""), axis=1)
print(links)

# merge links and pubs
all_data = pd.merge(pubs_journals, links, left_index=True, right_index=True).reset_index().drop(columns=['index'])
all_data.to_csv('test.csv')

result = []

for index, row in all_data.iterrows():
    for keyword in kw_list:
        if str(row['pub']).lower().find(keyword) >= 0 or str(row['journal']).lower().find(keyword) >= 0:
            row['link'] = '"' + str(row['link']) + '",'
            result.append(row['link'])

result = list(dict.fromkeys(result))

textfile = open("result.txt", "w")
for element in result:
    textfile.write(element + "\n")
textfile.close()
