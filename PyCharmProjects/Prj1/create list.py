import pandas as pd

all = pd.read_csv('smart pubmed.csv')
all.to_excel('smart_pubmed.xlsx')
top50 = all[:50]
allsplit = all['author'].str.split(expand=True)
allsplit['lastnames'] = allsplit[allsplit.columns[1:]].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)
allsplit = allsplit.drop(1, axis=1)
allsplit = allsplit.drop(2, axis=1)
allsplit = allsplit.drop(3, axis=1)
allsplit = allsplit.drop(4, axis=1)
print(allsplit.head(10))

top50split = top50['author'].str.split(expand=True)
top50split['lastnames'] = top50split[top50split.columns[1:]].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)
top50split = top50split.drop(1, axis=1)
top50split = top50split.drop(2, axis=1)
top50split = top50split.drop(3, axis=1)
print(top50split.head(10))

print(top50split['lastnames'].tolist())

lastname_check = lambda row: 'duplicate' if row['lastnames'] in top50split['lastnames'].tolist() else ''
allsplit['duplicate'] = allsplit.apply(lastname_check, axis=1)
print(allsplit.head(10))

allsplit.to_excel('smart_pubmed_split.xlsx')
top50split.to_excel('smart_pubmed_split_top50.xlsx')