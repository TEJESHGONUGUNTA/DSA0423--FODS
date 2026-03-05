# Program to find top 5 most sold products

import pandas as pd

# Sample sales data
data = {
    'Product': ['Laptop', 'Mobile', 'Headphones', 'Keyboard', 'Mouse', 'Monitor', 'Tablet'],
    'Quantity': [50, 120, 80, 40, 60, 30, 70]
}

# Create DataFrame
sales_data = pd.DataFrame(data)

# Sort products by quantity sold (descending)
top_products = sales_data.sort_values(by='Quantity', ascending=False)

# Get top 5 products
top_5 = top_products.head(5)

# Display result
print("Top 5 Most Sold Products:")
print(top_5)
