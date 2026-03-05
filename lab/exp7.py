# Program to find average sale price of houses with more than 4 bedrooms

import numpy as np

# Example house dataset
# Columns: Bedrooms, Square Footage, Sale Price
house_data = np.array([
    [3, 1500, 200000],
    [5, 2500, 350000],
    [4, 1800, 270000],
    [6, 3200, 500000],
    [2, 1200, 150000],
    [5, 2800, 420000]
])

# Select houses with more than 4 bedrooms
filtered_houses = house_data[house_data[:,0] > 4]

# Get the sale prices of those houses
sale_prices = filtered_houses[:,2]

# Calculate average sale price
average_price = np.mean(sale_prices)

# Display results
print("Houses with more than 4 bedrooms:")
print(filtered_houses)

print("Average Sale Price:", average_price)
