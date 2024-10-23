import pandas as pd

customer = pd.read_csv('customer_data.csv')
customer.head()
import matplotlib.pyplot as plt

point = customer.iloc[:,3:5].values
x = point[:,0]
y = point[:,1]
plt.scatter(x,y,s=50,alpha=0.7)
plt.xlabel('Annual income (k$)')
plt.ylabel('Spending Score')
plt.show()

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=6,random_state=0)
kmeans.fit(point)
predicted_cluster_indexes = kmeans.predict(point)

plt.scatter(x,y,c=predicted_cluster_indexes,s=50,alpha=0.7,cmap='viridis')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score')
plt.show()

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=7,random_state=0)
kmeans.fit(point)
predicted_cluster_indexes = kmeans.predict(point)
plt.scatter(x,y,c=predicted_cluster_indexes,s=50,alpha=0.7,cmap='viridis')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score')
plt.title('Cluster centers')
plt.show()