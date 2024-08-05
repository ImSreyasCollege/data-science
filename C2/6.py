print("Name   : sreyas")
print("Reg.no : SJC23MCA-2053")
print("Roll.no : 53")
print("Batch : MCA 2023-25\n")

import numpy as np

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [10, 11, 12, 13],
    [14, 15, 16, 17]
])

print("original array : ", arr)
print("elements excluding 1st row : ", arr[1:])
print("elements excluding last col : ", arr[:, :-1])
print("elements of first and second column in the 2nd and 3rd row : ", arr[1:3, 0:2])
print("elements of 2nd and 3rd column : ", arr[:, 1:3])
print("2nd and 3rd elements of the 1st row : ", arr[0, 1:3])
print("elements from indices 4 to 10 in desc order : ", arr[0])
