import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Create dataset
data = {
    'CustomerID':[1,2,3,4,5,6,7,8,9,10],
    'AmountSpent':[200,500,150,800,120,700,300,650,400,100],
    'VisitFrequency':[5,12,3,15,2,14,7,13,9,1]
}

df = pd.DataFrame(data)

# Select features
X = df[['AmountSpent','VisitFrequency']]

# Apply K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

# Display clustered data
print(df)

# Plot clusters
plt.scatter(df['AmountSpent'], df['VisitFrequency'], c=df['Cluster'])
plt.xlabel("Amount Spent")
plt.ylabel("Visit Frequency")
plt.title("Customer Segmentation using K-Means")
plt.show()
