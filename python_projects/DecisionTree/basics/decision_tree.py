import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
# from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# GRE Scores ( out of 340 )
# TOEFL Scores ( out of 120 )
# University Rating ( out of 5 )
# Statement of Purpose and Letter of Recommendation Strength ( out of 5 ) - these are 2 different
# Undergraduate GPA ( out of 10 )
# Research Experience ( either 0 or 1 )
# Chance of Admit ( ranging from 0 to 1 )

# 'serial_no.', 'gre_score', 'toefl_score', 'university_rating', 'sop', 'lor', 'cgpa', 'research', 'chance_of_admit'

df = pd.read_csv('Admission_Predict_Ver1.1.csv')
pd.set_option('display.max_columns', None)

df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()

# print(df.columns)
# print(df.head())

X = df.loc[:, 'gre_score' : 'research']
y = df['chance_of_admit'] >= 0.8

# print(X.head)
# print(y.head)

x_train, x_test, y_train, y_test = train_test_split(X,y, random_state=0, test_size=0.2)
dt = tree.DecisionTreeClassifier(max_depth=2, ccp_alpha=0.01,criterion='gini')
dt.fit(x_train, y_train)

y_pred = dt.predict(x_test)
print(f'dt_score = {dt.score(x_test, y_test)}')
print(f' accuracy_score = {accuracy_score(y_test, y_pred)}')

tree.plot_tree(dt, feature_names = x_train.columns,
               max_depth=11, class_names = ['unlikely admit', 'likely admit'],
               label='root', filled=True)
print(tree.export_text(dt, feature_names = X.columns.tolist()))

# calculating Gini
def gini(data):
    data = pd.Series(data)
    return 1 - sum(data.value_counts(normalize=True) ** 2)

gi = gini(y_train)
print(f'Gini impurity at root: {round(gi, 3)}')

def info_gain(left, right, current_impurity):
    # weight for gini score of the left branch, so right is 1 - w
    w = float(len(left)) / (len(left) + len(right))
    return current_impurity - w * gini(left) - (1 - w) * gini(right)


# here we iterate over all the values from cgpa col to understand which value results in most of info gain
info_gain_list = []
for i in x_train.cgpa.unique():
    left = y_train[x_train.cgpa <= i]
    right = y_train[x_train.cgpa > i]
    info_gain_list.append([i, info_gain(left, right, gi)])

ig_table = pd.DataFrame(info_gain_list, columns=['split_value', 'info_gain']).sort_values('info_gain', ascending=False)
print(ig_table.head(10))

plt.figure()
plt.plot(ig_table['split_value'], ig_table['info_gain'],'o')
plt.plot(ig_table['split_value'].iloc[0], ig_table['info_gain'].iloc[0],'r*')
plt.xlabel('cgpa split value')
plt.ylabel('info gain')

plt.show()


