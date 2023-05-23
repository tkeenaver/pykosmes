import pandas as pd 

df_my_index = pd.read_csv('data/countries.csv', index_col = 0)
print(df_my_index[ ['area', 'population'] ])