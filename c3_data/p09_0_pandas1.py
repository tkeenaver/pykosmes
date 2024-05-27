import pandas as pd

data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'city': ['New York', 'Los Angeles', 'Chicago']
        }
df = pd.DataFrame(data, index=['A', 'B', 'C'])

# .loc[] 사용 예제
# 특정 행과 열 선택
print(f"\n{df.loc['A', 'name']=}")  # 출력: Alice
# 행 슬라이싱
print(df.loc['A':'B', :])  # 출력: 'A'부터 'B'까지의 모든 열
# 특정 열 선택
print(df.loc[:, 'age'])  # 출력: 모든 행의 'age' 열
# 조건에 따른 행 선택
print(df.loc[df['age'] > 30, :])  # 출력: 'age'가 30보다 큰 행들

# .iloc[] 사용 예제
# 특정 행과 열 선택
print(f"\n{df.iloc[0, 0]=}")  # 출력: Alice (첫 번째 행, 첫 번째 열)
# 행 슬라이싱
print(df.iloc[0:2, :])  # 출력: 첫 번째 행부터 두 번째 행까지의 모든 열
# 특정 열 선택
print(df.iloc[:, 1])  # 출력: 모든 행의 두 번째 열('age')
# 조건에 따른 행 선택
# .iloc[]는 불리언 조건을 직접 사용하지 않습니다.
condition = df['age'] > 30
print(df.iloc[condition.values, :])  # 출력: 'age'가 30보다 큰 행들

df = pd.read_csv('data/weather_u.csv')
pd.set_option('display.unicode.east_asian_width', True)
print('\n최대풍속 > 25.0 m/s 인 날들:')
print(df[df['최대풍속'] > 25.0])
print('\n평균풍속 > 12.0 m/s 인 날들:')
print(df[df['평균풍속'] > 12.0])
print('\n최대풍속 > 25.0 m/s 이면서 평균풍속 > 12.0 m/s 인 날들:')
print(df[(df['최대풍속'] > 25.0) & (df['평균풍속'] > 12.0)])