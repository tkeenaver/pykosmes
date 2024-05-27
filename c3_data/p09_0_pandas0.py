import pandas as pd

s = pd.Series([1, 3, 5, 7, 9])
print(s)

data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'city': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print(df)

df = pd.read_csv('data/weather_u.csv')
print(df.head())

df.to_csv('output/weather_u_copy.csv', index=False)
