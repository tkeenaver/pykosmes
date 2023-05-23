import pandas as pd
import matplotlib.pyplot as plt

print("="*50)
countries_df = pd.read_csv('data/countries.csv', index_col = 0)
sorted = countries_df.sort_values('population')
print(sorted)
print("="*50)
################################

countries_df = pd.read_csv('data/countries.csv', index_col = 0)
countries_df.sort_values('population', inplace = True)
print(countries_df)
print("="*50)

#################################

countries = pd.read_csv('data/countries.csv', index_col = 0, encoding='CP949')
countries.sort_values(['population', 'area'], ascending = False, inplace = True)
print(countries)
print("="*50)
