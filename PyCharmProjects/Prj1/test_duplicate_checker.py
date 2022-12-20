import pandas as pd

all = pd.read_csv('test_pubmed.csv')
all.to_excel('test_pubmed.xlsx')
to_check = 70 #enter nubmer HCPs to check
topHCP = all[:to_check]
duplicate_check = all[to_check:]

all_split = all['author'].str.split(expand=True)
all_split['lastnames'] = all_split[all_split.columns[1:]].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)
all_split = all_split.drop([1, 2, 3, 4], axis=1)
#print(all_split.head(10))

topHCP_split = topHCP['author'].str.split(expand=True)
topHCP_split['lastnames'] = topHCP_split[topHCP_split.columns[1:]].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)
topHCP_split = topHCP_split.drop([1, 2, 3], axis=1)
#print(topHCP_split.head(10))

duplicate_check_split = duplicate_check['author'].str.split(expand=True)
duplicate_check_split['lastnames'] = duplicate_check_split[duplicate_check_split.columns[1:]].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)
duplicate_check_split = duplicate_check_split.drop([1, 2, 3, 4], axis=1)
print(duplicate_check_split.head(10))

print(topHCP_split['lastnames'].tolist())

lastname_check = lambda row: 'duplicate' if row['lastnames'] in duplicate_check_split['lastnames'].tolist() else ''
topHCP_split['duplicate'] = all_split.apply(lastname_check, axis=1)
print(topHCP_split.head(10))

all_split.to_excel('test_pubmed_split.xlsx')
topHCP_split.to_excel('test_pubmed_split_top50.xlsx')