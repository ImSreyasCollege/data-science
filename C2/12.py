print("Name   : sreyas")
print("Reg.no : SJC23MCA-2053")
print("Roll.no : 53")
print("Batch : MCA 2023-25\n")

import numpy as np;
X = np.array([[1, 2],[3, 4]])
Y = np.random.rand(*X.shape)
result = X * 2 + 2 * Y
print(result)