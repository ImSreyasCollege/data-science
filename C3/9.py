import pandas
import matplotlib.pyplot as plt
import seaborn

iris_dataset = pandas.read_csv("iris.csv")

seaborn.displot(iris_dataset['sepal.length'], kde=True, rug=True)
plt.title("Distribution of sepal length")
plt.savefig("./Outputs/9_1.png")
plt.show()

seaborn.histplot(iris_dataset['petal.width'], kde=True, bins=20)
plt.title("Distribution of petal width")
plt.savefig("./Outputs/9_2.png")
plt.show()

seaborn.relplot(x="sepal.length", y="sepal.width", data=iris_dataset, hue="variety", style="variety")
plt.title("sepal length vs sepal width")
plt.savefig("./Outputs/9_3.png")
plt.show()