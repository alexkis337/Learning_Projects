import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

data = pd.read_csv('insurance.csv')

def age_group(age):
    if age <= 25:
        return '18-25'
    elif age <= 34:
        return '26-34'
    elif age <= 45:
        return '35-45'
    elif age <= 60:
        return '46-60'
    else:
        return '60+'


data['age_group'] = data['age'].apply(age_group)
data['charges'] = data['charges'].apply(lambda x: 0 if x < 0 else x)
print(data.sort_values(by='age', ascending=True).head(15))
print(data.median())

#plt.plot(data['age'].tolist(), data.charges.tolist())
sns.barplot(data=data, x='age', y='charges')
#sns.kdeplot(data=data.sort_values(by='age'), x='age', y='charges') #hue='sex'
#plt.show()

#37