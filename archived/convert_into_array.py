import numpy as np
data1 = [[1, 2, 3], [4, 5, 6]]
data2 = [[1, 2, 3], [4, 5, '6']]
data3 = [[1, 2, 3], [4, 5]]
arr1 = np.array(data1, dtype=np.int32)
print("arr1:\n", arr1)
arr2 = np.array(data2, dtype=np.int32)
print("arr2:\n", arr2)
arr3 = np.array(data3, dtype=np.int32)
print("arr3:\n", arr3)
