import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('./nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]


knicks_10_pts = nba_2010['pts'][nba_2010['fran_id'] == 'Knicks']
nets_10_pts = nba_2010['pts'][nba_2010['fran_id'] == 'Nets']
diff_means = np.mean(knicks_10_pts) - np.mean(nets_10_pts)
# print(diff_means)

knicks_10_pts_14 = nba_2014['pts'][nba_2014['fran_id'] == 'Knicks']
nets_10_pts_14 = nba_2014['pts'][nba_2014['fran_id'] == 'Nets']
diff_means_14 = np.mean(knicks_10_pts_14) - np.mean(nets_10_pts_14)
# print(diff_means_14)

# fig10 = plt.figure()
# plt.hist(knicks_10_pts, color='red', alpha=0.8, label='Knicks_10')
# plt.hist(nets_10_pts, alpha=0.8, label='Nets_10')
# plt.legend()

# fig14 = plt.figure()
# plt.hist(knicks_10_pts_14, color='red', alpha=0.8, label='Knicks_14')
# plt.hist(nets_10_pts_14, alpha=0.8, label='Nets_14')
# plt.legend()

# sns.boxplot(data=nba_2010, x='fran_id', y='pts')
# plt.show()

spurs = nba_2010[nba_2010['fran_id'] == 'Spurs']

location_result_freq = pd.crosstab(nba_2010.game_result, nba_2010.game_location)

location_result_freq_spurs = pd.crosstab(spurs['game_result'], spurs['game_location'])
location_result_proportions_spurs = location_result_freq_spurs/len(spurs)
chi2, pval, dof, expected = chi2_contingency(location_result_freq_spurs)

# print(location_result_freq_spurs)
# print(location_result_proportions_spurs)
# print(expected)
# print(chi2)

point_diff_forecast_cov = np.cov(nba_2010.forecast, nba_2010.point_diff)
x, point_diff_forecast_corr = pearsonr(nba_2010.forecast, nba_2010.point_diff)
print(point_diff_forecast_corr)
print(point_diff_forecast_cov)

plt.scatter('forecast', 'point_diff', data=nba_2010)
plt.xlabel('Forecasted Win Prob.')
plt.ylabel('Point Differential')

coefficients = np.polyfit(nba_2010.forecast, nba_2010.point_diff, 1)
polynomial = np.poly1d(coefficients)
plt.plot(nba_2010.forecast, polynomial(nba_2010.forecast), 'r-')


plt.show()

# Creating crosstab for each team
# or team in nba_2010.fran_id.unique():
#    crosstab = pd.crosstab(nba_2010[nba_2010['fran_id'] == team]['game_result'],
#                           nba_2010[nba_2010['fran_id'] == team]['game_location'])
#    print(team, '\n', crosstab)

#print(location_result_freq)
#print(location_result_freq_spurs)

#location_result_freq.transpose().plot.bar(stacked=True, color=['tomato', 'lightseagreen'], figsize=(10,8))
#plt.legend()
#plt.show()

# print(knicks_10_pts)
# print(nba_2014.head())
