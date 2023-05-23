import pandas as pd 

df_my_index = pd.read_csv('data/countries.csv', index_col = 0)
df_no_index = pd.read_csv('data/countries.csv')
print(df_my_index['population'])
print(df_no_index['population'])