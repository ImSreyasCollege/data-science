import pandas
import seaborn
import matplotlib.pyplot as plt

# Reading dataset
dataset = pandas.read_csv("iris.csv")

seaborn.pairplot(dataset, kind="scatter")
plt.savefig("./Outputs/8_1.png")

seaborn.pairplot(dataset, kind="kde")
plt.savefig("./Outputs/8_2.png")

seaborn.pairplot(dataset, kind="hist")
plt.savefig("./Outputs/8_3.png")

seaborn.pairplot(dataset, kind="reg")
plt.savefig("./Outputs/8_4.png")

plt.show()