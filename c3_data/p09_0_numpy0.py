import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

total = np.sum(arr1)
mean = np.mean(arr1)
product = np.prod(arr1)

print(f'{total=}')
print(f'{mean=}')
print(f'{product=}')

arr3 = arr2.reshape((3, 2))
print(f'{arr2=}')
print(f'{arr3=}')

element = arr2[0, 1]
sub_array = arr2[:, 1]
print(f'{element=}')
print(f'{sub_array=}')