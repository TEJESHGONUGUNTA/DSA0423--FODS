import pandas as pd
import matplotlib.pyplot as plt

# Creating dataset inside program
data = {
    "shoe_size": [6,7,8,9,10,8,7,9,10,6],
    "quantity": [10,15,20,18,12,5,7,6,8,4]
}

df = pd.DataFrame(data)

# Frequency distribution
freq = df.groupby("shoe_size")["quantity"].sum()

print("Frequency Distribution of Shoe Sizes:")
print(freq)

# Bar chart
freq.plot(kind="bar")

plt.xlabel("Shoe Size")
plt.ylabel("Quantity Sold")
plt.title("Frequency Distribution of Shoe Sizes")
plt.show()
