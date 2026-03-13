import pandas as pd
import matplotlib.pyplot as plt

# Sample car dataset
data = {
    'Mileage': [18,15,20,22,17,19,16,21],
    'Horsepower': [130,165,150,140,170,160,155,145],
    'Weight': [3500,3700,3200,3000,3600,3300,3400,3100],
    'Price': [20000,25000,22000,21000,26000,24000,23000,21500]
}

df = pd.DataFrame(data)

# Multivariate Scatter Plot
plt.scatter(df['Mileage'], df['Price'])
plt.xlabel("Mileage")
plt.ylabel("Price")
plt.title("Mileage vs Price Scatter Plot")
plt.show()

# Scatter Plot Matrix
pd.plotting.scatter_matrix(df, figsize=(8,8))
plt.show()
