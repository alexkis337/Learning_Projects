import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

# data explained
#    1. name	Name of the country concerned
#    2. landmass	1=N.America, 2=S.America, 3=Europe, 4=Africa, 5=Asia, 6=Oceania
#    3. zone	Geographic quadrant, based on Greenwich and the Equator
#                 1=NE, 2=SE, 3=SW, 4=NW
#    4. area	in thousands of square km
#    5. population	in round millions
#    6. language 1=English, 2=Spanish, 3=French, 4=German, 5=Slavic, 6=Other
#                Indo-European, 7=Chinese, 8=Arabic,
#                9=Japanese/Turkish/Finnish/Magyar, 10=Others
#    7. religion 0=Catholic, 1=Other Christian, 2=Muslim, 3=Buddhist, 4=Hindu,
#                5=Ethnic, 6=Marxist, 7=Others
#    8. bars     Number of vertical bars in the flag
#    9. stripes  Number of horizontal stripes in the flag
#   10. colours  Number of different colours in the flag
#   11. red      0 if red absent, 1 if red present in the flag
#   12. green    same for green
#   13. blue     same for blue
#   14. gold     same for gold (also yellow)
#   15. white    same for white
#   16. black    same for black
#   17. orange   same for orange (also brown)
#   18. mainhue  predominant colour in the flag (tie-breaks decided by taking
#                the topmost hue, if that fails then the most central hue,
#                and if that fails the leftmost hue)
#   19. circles  Number of circles in the flag
#   20. crosses  Number of (upright) crosses
#   21. saltires Number of diagonal crosses
#   22. quarters Number of quartered sections
#   23. sunstars Number of sun or star symbols
#   24. crescent 1 if a crescent moon symbol present, else 0
#   25. triangle 1 if any triangles present, 0 otherwise
#   26. icon     1 if an inanimate image present (e.g., a boat), otherwise 0
#   27. animate  1 if an animate image (e.g., an eagle, a tree, a human hand)
#                present, 0 otherwise
#   28. text     1 if any letters or writing on the flag (e.g., a motto or
#                slogan), 0 otherwise
#   29. topleft  colour in the top-left corner (moving right to decide
#                tie-breaks)
#   30. botright Colour in the bottom-left corner (moving left to decide
#                tie-breaks)

column_names = ['name', 'landmass', 'zone', 'area', 'population', 'language', 'religion', 'bars', 'stripes',
                   'colours', 'red', 'green', 'blue', 'gold', 'white', 'black', 'orange', 'mainhue', 'circles',
                   'crosses', 'saltires', 'quarters', 'sunstars', 'crescent', 'triangle', 'icon', 'animate',
                   'text', 'topleft', 'botright']
flags = pd.read_csv('flag.data', names=column_names)

var = ['red', 'green', 'blue', 'gold', 'white', 'black', 'orange', 'mainhue', 'bars', 'stripes', 'circles', 'crosses',
        'saltires', 'quarters', 'sunstars', 'triangle', 'animate']

# print(flags.head())
# print(flags['landmass'].value_counts())

flags_eu_oc = flags[flags['landmass'].isin([3, 6])]
labels = flags["landmass"].isin([3, 6])

# print(flags[var].dtypes) # mainhue is object
data = pd.get_dummies(flags[var])
# print(data)

# print(len(data))
# print(labels)
# print(len(flags_eu_oc))

# print(flags_eu_oc.head())
# print(labels)

train_data, test_data, train_labels, test_labels = train_test_split(data, labels, random_state=1, test_size=.4)

depths = range(1, 21)
acc_depth = []

for i in depths:
    dt = DecisionTreeClassifier(max_depth=i, random_state=1)
    dt.fit(train_data, train_labels)
    acc_depth.append(dt.score(test_data, test_labels))

# max at depth=6

# plt.figure()
# plt.plot(depths, acc_depth)
# plt.xlabel('max_depth')
# plt.ylabel('accuracy')

best_depth = np.argmax(acc_depth)

dt = DecisionTreeClassifier(max_depth=best_depth, random_state=1)
dt.fit(train_data, train_labels)

# train_data[['mainhue_black', 'mainhue_blue', 'mainhue_brown', 'mainhue_gold', 'mainhue_green',
# 'mainhue_orange','mainhue_red', 'mainhue_white']] = train_data[['mainhue_black', 'mainhue_blue', 'mainhue_brown',
# 'mainhue_gold', 'mainhue_green', 'mainhue_orange','mainhue_red', 'mainhue_white']].astype(int)

print(train_labels.unique())  # ensuring we have 2 labels


plt.figure(figsize=(20, 10))  # You can adjust the values as needed
plt.title("first tree")
tree.plot_tree(dt, feature_names=train_data.columns, class_names=['Europe', 'Oceania'], filled=True)
ёё
path = dt.cost_complexity_pruning_path(train_data, train_labels) # getting limits for ccp
ccp_alphas = path.ccp_alphas
print('ccp_alphas', ccp_alphas)

ccp_range = np.logspace(-3, np.log10(np.max(ccp_alphas)), num=20)
print(ccp_range)

acc_pruned = []
for i in ccp_range:
    dt_prune = DecisionTreeClassifier(max_depth=best_depth, ccp_alpha=i, random_state=1)
    dt_prune.fit(train_data, train_labels)
    acc_pruned.append(dt_prune.score(test_data, test_labels))

plt.figure()
plt.plot(ccp_range, acc_pruned)

print('acc_pruned', acc_pruned)
best_ccp = ccp_range[np.argmax(acc_pruned)]
print(best_ccp)


dt_final = DecisionTreeClassifier(max_depth=best_depth, random_state=1, ccp_alpha=best_ccp)
dt_final.fit(train_data, train_labels)

plt.figure(figsize=(20, 10))  # You can adjust the values as needed
plt.title("final tree")
tree.plot_tree(dt_final, feature_names=train_data.columns, class_names=['Europe', 'Oceania'], filled=True)
plt.show()





