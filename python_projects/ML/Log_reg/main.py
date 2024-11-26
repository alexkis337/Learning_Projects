import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score, roc_curve, roc_auc_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

col_names = ['age', 'workclass', 'fnlwgt','education', 'education-num', 'marital-status',
             'occupation', 'relationship', 'race', 'sex',
             'capital-gain','capital-loss', 'hours-per-week','native-country', 'income']
df = pd.read_csv('adult.data',header=None, names=col_names)


#Clean columns by stripping extra whitespace for columns of type "object"
for c in df.select_dtypes(include=['object']).columns:
    df[c] = df[c].str.strip()
print(df.head())

# check Class Imbalance
print(df['income'].value_counts())

# create feature dataframe X with feature columns
feature_cols = ['age', 'capital-gain', 'capital-loss', 'hours-per-week', 'sex', 'race', 'education']
X = pd.get_dummies(df[['age', 'capital-gain', 'capital-loss', 'hours-per-week', 'sex', 'race', 'education']],
                   drop_first=True)

print(X.columns)

# heatmap of X data to see feature correlation
plt.figure(figsize=(10, 8))  # Set the figure size
sns.heatmap(X.corr(), annot=True, cmap='coolwarm')

plt.title("Heatmap of Feature Correlations")

# output variable with 0 if <50K and 1 if >=50K
y = df['income'].apply(lambda x: 0 if x == '<=50K' else 1)


# Split data and fit LR model with
log_reg = LogisticRegression(C=0.05, penalty='l1', solver='liblinear')
x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=1, test_size=0.2)

log_reg.fit(x_train, y_train)
y_pred = log_reg.predict(x_test)

# print model params
print('Model Parameters, Intercept: ', log_reg.intercept_)
print('Model Parameters, Coeff: ', log_reg.coef_)


# evaluate the predictions of the model on the test set,  confusion matrix and accuracy score.
conf_matrix = confusion_matrix(y_test, y_pred)
print('Confusion Matrix on test set: \n', conf_matrix)
print('Accuracy Score on test set: ', log_reg.score(x_test, y_test))

# new df of the model coefficients and var names; sort values based on coefficient
df_coef = pd.DataFrame(zip(feature_cols, log_reg.coef_[0])).sort_values(by=1, ascending=True)
print('---------------------------------------------------------------------------')

df_coef = df_coef[df_coef[1] != 0].sort_values(by=1, ascending=True)
print(df_coef.head())

# barplot of the coefficients
plt.figure(figsize=(10, 8))
sns.barplot(x=df_coef[0], y=df_coef[1], data=df_coef)

# roc/auc
y_pred_prob = log_reg.predict_proba(x_test)[:, 1]
print('---------------------------------------------------------------------------')
print(y_test)
print(y_pred_prob)
print('---------------------------------------------------------------------------')

fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)

# AUC score
auc_score = roc_auc_score(y_test, y_pred_prob)
print(f"AUC Score: {auc_score:.4f}")

# ROC curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='blue', label=f"ROC curve (AUC = {auc_score:.4f})")
plt.plot([0, 1], [0, 1], color='red', linestyle='--')
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend(loc="lower right")
plt.show()

