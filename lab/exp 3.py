import pandas as pd

# Sample sales_data DataFrame
data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Laptop", "Mobile"],
    "Price": [50000, 20000, 15000, 52000, 21000],
    "Quantity": [2, 3, 4, 1, 2]
}

sales_data = pd.DataFrame(data)

print("Original Data:")
print(sales_data)

# Calculate Total Sales (Price * Quantity)
sales_data["Total Sales"] = sales_data["Price"] * sales_data["Quantity"]

print("\nData with Total Sales Column:")
print(sales_data)

# If you want total sales for each product
product_total_sales = sales_data.groupby("Product")["Total Sales"].sum()

print("\nTotal Sales for Each Product:")
print(product_total_sales)
