# KNN

import pandas as pd
from math import floor, sqrt

dataset = pd.read_csv("iris.csv")

x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
classifier = KNeighborsClassifier(n_neighbors=10)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)

print("Accuracy : ", accuracy_score(y_test, y_pred))

# for i, j in zip(y_test, y_pred):
#   if i != j:
#     print("original : " + i + ", predicted : " + j )

