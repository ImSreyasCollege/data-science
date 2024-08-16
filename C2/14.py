print("Name   : sreyas")
print("Reg.no : SJC23MCA-2053")
print("Roll.no : 53")
print("Batch : MCA 2023-25\n")

import numpy as np
# Define matrices A, B, and C
A = np.array([[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])
B = np.array([[9, 8, 7],
[6, 5, 4],
[3, 2, 1]])
C = np.array([[10, 5, 9],
[20, 15, 19],
[30, 2, 29]])

# Perform matrix multiplication: (A * B) * C
result = np.dot(np.dot(A, B), C)
# Display the result
print("Matrix A:")
print(A)
print("Matrix B:")
print(B)
print("Matrix C:")
print(C)
print("Result of (A * B) * C:")
print(result)