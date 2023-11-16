import requests
import numpy as np
import pandas as pd
from loc_address import get_coordinates, get_location

pd.options.display.max_columns = 5
# pd.set_option('max_columns', None)


df = pd.read_excel('C:/Users/Oleksandr/Desktop/final.xlsx')
df['hco_coord'] = df['organisation_name'].apply(lambda x: get_coordinates(x))
df['address_coord'] = df['address'].apply(lambda x: get_coordinates(x))

df.to_excel('C:/Users/Oleksandr/Desktop/final_coords.xlsx')
print(df.head())

