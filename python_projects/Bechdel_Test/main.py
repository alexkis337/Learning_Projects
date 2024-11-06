import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('bechdelExpanded.csv')

df['total_score'] = df.bechdel + df.peirce + df.landau + df.feldman + df.villareal + df.hagen + df.ko + df.villarobos +\
                 df.waithe + df.koeze_dottle + df.uphold + df.white + df['rees-davies']

df_sorted = df.sort_values('total_score', ascending=False).reset_index(drop=True)
isolated_df = df_sorted[['movie', 'bechdel', 'waithe', 'ko', 'total_score']]


#print(df.head(5))
#print(isolated_df.head(15))


df2plot = isolated_df[['movie', 'total_score']]
df2plot.set_index('movie')

#print(type(ax))

plt.figure(figsize=(15, 10))
ax = plt.subplot()
plt.plot(df2plot.index, df2plot.total_score)
ax.set_xticks(df2plot.index)
ax.set_xticklabels(df2plot.movie, rotation=90)


plt.show( )














