import pandas as pd

# Product sales dataset
data = {
    "product": ["Shoes", "Shirt", "Shoes", "Watch", "Shirt", "Shoes", "Bag", "Watch", "Shoes"],
}

df = pd.DataFrame(data)

# Frequency distribution
freq = df["product"].value_counts()

print("Frequency Distribution of Products:")
print(freq)

# Most popular product
popular = freq.idxmax()

print("\nMost Popular Product:", popular)
