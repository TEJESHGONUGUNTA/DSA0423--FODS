import pandas as pd
import numpy as np

# Step 1: Create Sales Dataset
data = {
    'Product': ['Laptop','Mobile','Tablet','Laptop','Mobile','Tablet','Laptop','Mobile','Tablet','Laptop'],
    'Category': ['Electronics','Electronics','Electronics','Electronics','Electronics','Electronics','Electronics','Electronics','Electronics','Electronics'],
    'Price': [50000,20000,15000,52000,21000,np.nan,51000,22000,16000,53000],
    'Quantity': [5,10,7,6,8,5,np.nan,9,6,7],
    'Region': ['South','North','East','West','South','North','East','West','South','North']
}

df = pd.DataFrame(data)

print("Original Dataset\n")
print(df)

# Step 2: Handle Missing Values
df['Price'].fillna(df['Price'].mean(), inplace=True)
df['Quantity'].fillna(df['Quantity'].median(), inplace=True)

print("\nDataset After Handling Missing Values\n")
print(df)

# Step 3: Create New Feature - Total Sales
df['Total_Sales'] = df['Price'] * df['Quantity']

print("\nDataset with Total Sales Column\n")
print(df)

# Step 4: Grouping and Aggregation
sales_by_product = df.groupby('Product')['Total_Sales'].sum()

print("\nTotal Sales by Product\n")
print(sales_by_product)

# Step 5: Filtering High Sales
high_sales = df[df['Total_Sales'] > 200000]

print("\nHigh Sales Records (Sales > 200000)\n")
print(high_sales)

# Step 6: Pivot Table Analysis
pivot_table = pd.pivot_table(df,
                             values='Total_Sales',
                             index='Region',
                             columns='Product',
                             aggfunc='sum')

print("\nPivot Table (Sales by Region and Product)\n")
print(pivot_table)

# Step 7: Business Insight
max_product = sales_by_product.idxmax()

print("\nBusiness Insight:")
print("Product with highest sales:", max_product)
