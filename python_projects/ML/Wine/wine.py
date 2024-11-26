import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


# get data from wine.data
df = pd.read_csv('wine.data', header=None)

print(df.describe())



# df.columns = ['Class', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavanoids',
#               'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue', 'OD280/OD315 of diluted wines',
#               'Proline']
#
# # sns.pairplot(df[['Flavanoids', 'Color intensity', 'Alcohol', 'OD280/OD315 of diluted wines']], palette='viridis')
# # plt.show()
#
# scaler = StandardScaler()
# scaled_data = scaler.fit_transform(df)
#
# # Apply K-Means Clustering
# kmeans = KMeans(n_clusters=3, random_state=0)  # Set n_clusters to the number of clusters you expect
# clusters = kmeans.fit_predict(scaled_data)
#
# # Add the cluster labels to the DataFrame
# df['Cluster'] = clusters
#
#
# df.to_csv('wine_clusters.csv', index=False)
#
# # Plot pairplot and use cluster labels to color the data points
# sns.pairplot(df, hue='Cluster', palette='viridis')
# plt.show()
