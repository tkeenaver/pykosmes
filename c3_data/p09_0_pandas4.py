import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/weather_u.csv')
df['일시'] = pd.to_datetime(df['일시'])
df.set_index('일시', inplace=True)
plt.rc('font', family='Hancom Gothic')
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['최대풍속'], label='최대풍속', marker='o')
plt.title('최대풍속 시계열 그래프')
plt.xlabel('일시')
plt.ylabel('최대풍속 (m/s)')
plt.legend()
plt.show()


# 타이타닉 데이터셋 읽기
df = pd.read_csv('data/titanic.csv')
print(df.head())
print(df.tail())
# Pclass 열을 기준으로 그룹화하여 Survived 열의 평균값을 계산
print(df.groupby('Pclass')['Survived'].mean())