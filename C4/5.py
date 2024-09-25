import numpy as np
import pandas as pd
import sklearn as sk
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

student = pd.read_csv("student_scores.csv")
print(student.head())
student.describe()
student.info()


x_axis = student.iloc[:,0]
y_axis = student.iloc[:,1]

plt.scatter(x_axis, y_axis)
plt.xlabel("no.of hours")
plt.ylabel("scores")
plt.show()

x = student.iloc[:, :-1]
y = student.iloc[:, 1]

print("x values", x)
print("y values", y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

print(x_train)

regression = LinearRegression()
regression.fit(x_train, y_train)
print("intercept : ", regression.intercept_)
print("co-efficient : ", regression.coef_)
y_pred = regression.predict(x_test)
for (i, j) in zip(y_test, y_pred):
    if(i!=j):
        print("actual value : ", i, "\npredicted value : ", j)

print("mislabeld : ", (y_test != y_pred).sum())

from sklearn.metrics import mean_squared_error, mean_absolute_error

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print("mean absolute error : ", mae)
print("mean square error : ", mse)
print("root mean square error : ", rmse)
