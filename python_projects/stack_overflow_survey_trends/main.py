import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.model_selection import train_test_split


# pd.set_option('display.max_columns', None)
df = pd.read_csv('developer_dataset.csv')
print(df.columns)
print(df.count())
print(df.describe())

print('% of missing')
print(df.isnull().mean() * 100 )

df.drop(['NEWJobHunt', 'NEWJobHuntResearch', 'NEWLearn'], axis=1, inplace=True)

df[['RespondentID', 'Country']].groupby('Country').count()
missing_data = df[['Employment', 'DevType']].isnull().groupby(df['Country']).sum().reset_index()

df.to_csv('test.csv', index=False)

# A = sns.catplot(data=missing_data, x='Country', y='Employment', kind='bar', height=5, aspect=2, palette='tab20')
# B = sns.catplot(data=missing_data, x='Country', y='DevType', kind='bar', height=5, aspect=3, palette='tab20')


df.dropna(subset=['Employment','DevType'], inplace=True, how='any')

devdf = df[['Country','DevType']]
devdf.loc[devdf['DevType'].str.contains('back-end'), 'BackEnd'] = True
devdf.loc[devdf['DevType'].str.contains('front-end'), 'FrontEnd'] = True
devdf.loc[devdf['DevType'].str.contains('full-stack'), 'FullStack'] = True
devdf.loc[devdf['DevType'].str.contains('mobile'), 'Mobile'] = True
devdf.loc[devdf['DevType'].str.contains('administrator'), 'Admin'] = True

devdf = devdf.melt(id_vars=['Country'], value_vars=['BackEnd','FrontEnd','FullStack','Mobile','Admin'],
                   var_name='DevCat', value_name='DevFlag')
devdf.dropna(how='any', inplace=True)
# devFig = sns.catplot(x="Country", col="DevCat", data=devdf, kind="count", height=6, aspect=1.5)

# missingUndergrad = df['UndergradMajor'].isnull().groupby(df['Year']).sum().reset_index()
# sns.catplot(x="Year", y="UndergradMajor", data=missingUndergrad, kind="bar", height=4, aspect=1)

df = df[df['Country'] == 'Canada']
df['YearsCodePro'] = pd.to_numeric(df['YearsCodePro'], errors='coerce')
df['ConvertedComp'] = pd.to_numeric(df['ConvertedComp'], errors='coerce')
df = df.dropna(subset=['YearsCodePro', 'ConvertedComp'])
# sns.scatterplot(x='YearsCodePro', y='ConvertedComp', data=df)

# sns.regplot(x='YearsCodePro', y='ConvertedComp', data=df, scatter=False, color='red')


imputedf = df[['YearsCodePro','ConvertedComp']]
traindf, testdf = train_test_split(imputedf, train_size=0.1)

imp = IterativeImputer(max_iter=20, random_state=0)
imp.fit(imputedf)

compdf = pd.DataFrame(np.round(imp.transform(imputedf),0), columns=['YearsCodePro','ConvertedComp'])
compPlotdf = compdf.loc[compdf['ConvertedComp'] <= 150000]
compPlotdf['CodeYearBins'] = pd.qcut(compPlotdf['YearsCodePro'], q=5)

sns.boxplot(x="CodeYearBins", y="ConvertedComp", data=compPlotdf)

plt.show()
