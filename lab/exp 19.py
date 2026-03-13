import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Sample dataset
data = {
    'Customer_ID':[1,2,3,4,5,6],
    'Amount_Spent':[200,500,150,800,300,700],
    'Items_Purchased':[2,5,1,7,3,6]
}

df = pd.DataFrame(data)

# Features
X = df[['Amount_Spent','Items_Purchased']]

# Apply K-Means
kmeans = KMeans(n_clusters=2)
df['Cluster'] = kmeans.fit_predict(X)

print(df)

# Visualization
plt.scatter(df['Amount_Spent'], df['Items_Purchased'], c=df['Cluster'])
plt.xlabel("Amount Spent")
plt.ylabel("Items Purchased")
plt.title("Customer Segmentation")
plt.show()
