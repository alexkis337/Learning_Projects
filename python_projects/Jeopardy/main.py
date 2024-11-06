import pandas as pd


pd.set_option('display.max_columns', None)
df = pd.read_csv('jeopardy.csv')
df = df.rename(str.strip, axis='columns')
df['Value'] = df['Value'].apply(lambda row: row.replace('$', ''))
df['Value'] = df['Value'].apply(lambda row: row.replace(',', ''))
df['Value'] = df['Value'].apply(lambda row: float(row.replace('None', '0')))
#print(df)
df.to_csv('out.csv')
#df['Value'].apply(lambda row: float(row.replace(',', '')))


question_list = ['King', 'England']
func = lambda row: all(row.lower().find(word.lower()) > -1 for word in question_list)
df['checked'] = df['Question'].apply(func)
king_questions = df[df['checked'] == True]
mean = df['Value']
df['mean'] = df['Value'].apply(lambda row: 'higher' if(row > mean) else 'lower')

something = king_questions['Value'].mean()
print(something)
print(df)

#print(type(king_questions))

#print(df)

#print(func('King'))
#print(func('am King'))
#print(func('the king'))
#print(func('englandia'))
#print(func('England'))