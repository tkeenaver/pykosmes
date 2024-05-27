import numpy as np

arr4 = np.array([1, 2, 3])
arr5 = np.array([4, 5, 6])
result = arr4 + arr5

arr6 = np.array([1, 2, 3])
arr7 = np.array([[1], [2], [3]])
result2 = arr6 + arr7

print(f'{result=}')
print(f'{result2=}')

# 단순 선형 회귀
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
#y = np.array([2.1, 4.1, 5.9, 8.1, 9.9])
w = np.sum(X * y) / np.sum(X**2)
b = np.mean(y - w * X)
print(f"Weight: {w}, Bias: {b}")