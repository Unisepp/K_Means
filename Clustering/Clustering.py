"""

@author: UNISEPP
"""

# Clustering Exercise : K-Means - DBSCAN

# importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN

# understanding the data
data = pd.read_csv('Mall_Customers.csv')
print(data.head())
print(data.info())
print(data.describe())

# preparing data
data.rename(columns = {'Annual Income (k$)' : 'AnnualIncome' , 'Spending Score (1-100)' : 'SpendingPercentage' }, inplace = True)
X= data.loc[: , ['AnnualIncome' , 'SpendingPercentage']].values

# finding the optimal number of k
wcss = []
for i in range(1, 9):
    kmeans = KMeans(n_clusters = i, init = 'k-means++' , random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 9), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
# the best k is 5

# fitting K_Means to the data set 
kmeans = KMeans(n_clusters=5, init ='k-means++' , random_state = 42)
y_kmeans = kmeans.fit_predict(X)

# visualizing K_Means
color = ['red' , 'blue' , 'green' , 'cyan' , 'magenta']
for i in range (5):
    plt.scatter(X[y_kmeans == i,0] , X[y_kmeans == i , 1]  ,s = 50, c = color[i] , label = {'cluster'+str(i+1)})
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 100, c = 'yellow', label = 'Centroids')
plt.title('Clusters of customers_KMeans')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()

# fitting DBSCAN to the data set 
dbscan = DBSCAN(eps = 5 , min_samples= 5)
y_dbscan = dbscan.fit_predict(X)
print(np.unique(y_dbscan)) # -1 is for the noise


# visualizing DBSCAN
color = ['red' , 'blue' , 'green' , 'cyan' , 'magenta','black']
for i in range (-1,6):
    plt.scatter(X[y_dbscan == i,0] , X[y_dbscan == i , 1]  , c = color[i]) 
plt.title('Clusters of customers_DBSCAN')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()
# Black dots are considerd as noise because they have less density and they are far away