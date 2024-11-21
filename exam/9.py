import pandas as pd

dataset = pd.read_csv("car.csv")

col_names = ["Buying", "maint", "doors", "Persons", "Lug_boot", "safety", "class"]
dataset.columns = col_names

for col in col_names:
  dataset[col], _ = pd.factorize(dataset[col])

x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

classifier = DecisionTreeClassifier()
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)

misclassified = y_test != y_pred
print(accuracy_score(y_test, y_pred))
print("Misclassified : ", misclassified.sum())
print(pd.DataFrame({
  "Actual": y_test[misclassified],
  "predicted": y_pred[misclassified],
}))


