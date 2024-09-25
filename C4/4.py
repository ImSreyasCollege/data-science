import pandas as pd
data = pd.read_csv('car.csv')
print(data.head())
col_names = ['buying','maint','doors','persons','lug_boot','safety','class']
data.columns = col_names
print(col_names)
data['class'],class_names = pd.factorize(data['class'])
data['buying'],_ = pd.factorize(data['buying'])
data['maint'],_ = pd.factorize(data['maint'])
data['doors'],_ = pd.factorize(data['doors'])
data['persons'],_ = pd.factorize(data['persons'])
data['lug_boot'],_ = pd.factorize(data['lug_boot'])
data['safety'],_ = pd.factorize(data['safety'])
print(data.head())
x = data.iloc[:, :-1]
y = data.iloc[:, -1]
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)
from sklearn.tree import DecisionTreeClassifier
tree1 = DecisionTreeClassifier()
tree1.fit(x_train,y_train)
y_pred = tree1.predict(x_test)
#how did our model perform?

count_missclassified = (y_test != y_pred).sum()
print('Misclassified samples count : ',count_missclassified)
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test,y_pred)
print("Accuracy",accuracy)