import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


observations = pd.read_csv('observations.csv')
species = pd.read_csv('species_info.csv')

# plotting the sum of observations per park from observations and splitting by conservation_status
obs_by_park = observations.groupby('park_name').observations.sum().reset_index()
obs_by_park = obs_by_park.sort_values(by='observations', ascending=False).reset_index(drop=True)
obs_by_park['observations'] = obs_by_park['observations'].astype(float)

plt.figure(figsize=(16, 8))
sns.barplot(data=obs_by_park, x='park_name', y='observations', palette='tab20')
# addding a regression line
sns.regplot(data=obs_by_park, x=list(range(len(obs_by_park))), y='observations', scatter=False, color='red')

plt.title('Observations per Park')
plt.xlabel('Park')
plt.ylabel('Observations')

# splitting each bar by conservation_status
obs_by_park_and_status = observations.merge(species, on='scientific_name')
obs_by_park_and_status = obs_by_park_and_status.groupby(['park_name', 'conservation_status']).observations.sum().reset_index()
obs_by_park_and_status = obs_by_park_and_status[obs_by_park_and_status['conservation_status'] != 'Species of Concern']
obs_by_park_and_status = obs_by_park_and_status.sort_values(by='observations', ascending=False).reset_index(drop=True)
obs_by_park_and_status['observations'] = obs_by_park_and_status['observations'].astype(float)

plt.figure(figsize=(16, 8))


sns.barplot(data=obs_by_park_and_status, x='park_name', y='observations', hue='conservation_status', palette='tab20')
# sns.regplot(x=list(range(len(obs_by_park_and_status))), y='observations', data=obs_by_park_and_status, scatter=False, color='red')

plt.title('Observations per Park by Conservation Status')
plt.xlabel('Park')
plt.ylabel('Observations')
plt.legend(title='Conservation Status')

plt.show()

print(obs_by_park_and_status)
print(obs_by_park)
