import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Cek TIPE Array
print(type(arr))

# Print Array
print(arr)

# Index pada Array
print(arr[1:6]) # (2, 3, 4, 5, 6)
print(arr[2:3]) # (3)

# Dimensi pada Array
# 1 Dimensi :
arr_1d = np.array([1, 3, 5, 7])
print(arr_1d)

# 2 Dimensi
arr_2d = np.array([[1, 3, 5, 7], [2, 4, 6, 8]])
print(arr_2d)

# 3 Dimensi
print("Array 3D:")
arr_3d = np.array([ [[1, 3], [5, 7]], [[2, 4], [6, 8]], [[10, 11], [12, 13]] ])

# list = [1, 2, 3, 4, 5, 6]
# print(type(list))
# print(list)