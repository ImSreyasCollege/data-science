import pandas as pd

dataset = pd.read_csv("iris.csv")

x = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score, confusion_matrix

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

classifier = BernoulliNB()
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)

print(confusion_matrix(y_test, y_pred))
print(accuracy_score(y_test, y_pred))
print((y_test != y_pred).sum())
print(pd.DataFrame({
  "Actual value : ": y_test, 
  "Predicted value : ": y_pred, 
}))
