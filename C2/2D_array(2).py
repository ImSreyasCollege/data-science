print("Name   : sreyas")
print("Reg.no : SJC23MCA-2053")
print("Roll.no : 53")
print("Batch : MCA 2023-25\n")

from numpy import array

arr = array([
    [
        1 + 2j,
        3 - 2j,
        7 - 9j,
    ],
    [
        4 + 3j,
        8 + 1j,
        5 + 5j
    ]
], dtype=complex)

print("array is : ", arr)

# tuple destructuring (arr.shape returns a tuple with a size of 2)
(rows, cols) = arr.shape
print("number of rows : ", rows)
print("number of cols : ", cols)

dim = arr.ndim
print("array dimension : ", dim)

reshaped_arr = arr.reshape(3, 2)
print("reshaped array : ", reshaped_arr)