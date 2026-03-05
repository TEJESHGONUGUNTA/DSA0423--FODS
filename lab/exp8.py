# Program to calculate average product price using NumPy

import numpy as np

# Example sales data (product prices)
sales_data = np.array([120, 250, 300, 150, 200, 180, 220])

# Calculate average price
average_price = np.mean(sales_data)

# Display results
print("Product Prices:", sales_data)
print("Average Price of Products:", average_price)
