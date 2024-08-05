print("Name   : sreyas")
print("Reg.no : SJC23MCA-2053")
print("Roll.no : 53")
print("Batch : MCA 2023-25\n")

import numpy as np

arr = np.arange(2, 31, 2)
slice_arr = arr[2:9:2]
last_3 = arr[-3:]
alternate_ele = arr[::2]
last_3_alternate = arr[-3*2::2]

print("original array : ", arr)
print("sliced array : ", slice_arr)
print("last 3 elements in array : ", last_3)
print("alternate elements : ", alternate_ele)
print("last 3 alternate elements : ", last_3_alternate)
