import pandas as pd

# Sample Data (Creating order_data DataFrame)
data = {
    "customer_id": [101, 102, 101, 103, 102, 104],
    "order_date": ["2026-01-01", "2026-01-02", "2026-01-03", 
                   "2026-01-04", "2026-01-05", "2026-01-06"],
    "product_name": ["Laptop", "Mobile", "Tablet", 
                     "Laptop", "Mobile", "Headphones"],
    "order_quantity": [1, 2, 1, 3, 1, 4]
}

order_data = pd.DataFrame(data)

# Convert order_date to datetime format
order_data["order_date"] = pd.to_datetime(order_data["order_date"])

print("Original Data:")
print(order_data)

# 1️⃣ Total quantity of all products sold
total_quantity = order_data["order_quantity"].sum()
print("\nTotal Quantity Sold:", total_quantity)

# 2️⃣ Total number of orders
total_orders = order_data.shape[0]
print("Total Number of Orders:", total_orders)

# 3️⃣ Total quantity sold for each product
product_wise_sales = order_data.groupby("product_name")["order_quantity"].sum()
print("\nProduct-wise Sales:")
print(product_wise_sales)

# 4️⃣ Orders placed by each customer
customer_orders = order_data.groupby("customer_id")["order_quantity"].sum()
print("\nCustomer-wise Total Quantity:")
print(customer_orders)

# 5️⃣ Find the most ordered product
most_ordered_product = product_wise_sales.idxmax()
print("\nMost Ordered Product:", most_ordered_product)
