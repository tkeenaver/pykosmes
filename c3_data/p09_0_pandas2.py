import pandas as pd
import numpy as np

# 예제 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', np.nan],
        'age': [25, 30, np.nan, 22, 28],
        'salary': [50000, 60000, 70000, np.nan, 56000]}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# 1. dropna: 결측값이 있는 행 제거
df_cleaned = df.dropna()

print("\nDataFrame after dropna:")
print(df_cleaned)

# 2. fillna: 결측값을 특정 값으로 대체
df_filled = df.fillna({'age': df['age'].mean(), 'salary': df['salary'].mean()})

print("\nDataFrame after fillna:")
print(df_filled)

# 3. astype: 데이터 타입 변환
df_filled['age'] = df_filled['age'].astype(int)

print("\nDataFrame after astype (age to int):")
print(df_filled)

# 4. sort_values: 특정 열을 기준으로 데이터 정렬
df_sorted = df_filled.sort_values(by='salary', ascending=False)

print("\nDataFrame after sort_values (by salary):")
print(df_sorted)
