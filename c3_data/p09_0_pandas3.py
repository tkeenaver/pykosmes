import pandas as pd

# 예제 데이터프레임 생성
data = {'category': ['A', 'B', 'A', 'B', 'A'],
        'value': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# category 열을 기준으로 그룹화
grouped = df.groupby('category')

# 그룹화된 데이터에 집계 함수 적용
grouped_sum = grouped.sum()
grouped_mean = grouped.mean()
grouped_count = grouped.count()
grouped_max = grouped.max()
grouped_min = grouped.min()

# 여러 집계 함수를 동시에 적용
grouped_agg = grouped.agg(['sum', 'mean', 'count'])

# 출력
print("Sum:\n", grouped_sum)
print("\nMean:\n", grouped_mean)
print("\nCount:\n", grouped_count)
print("\nMax:\n", grouped_max)
print("\nMin:\n", grouped_min)
print("\nAgg:\n", grouped_agg)
