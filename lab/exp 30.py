import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("D:/FODS/shoe_sales.csv")

freq = data.groupby("shoe_size")["quantity"].sum()

print("Frequency Distribution of Shoe Sizes")
print(freq)

freq.plot(kind="bar")

plt.xlabel("Shoe Size")
plt.ylabel("Quantity Sold")
plt.title("Frequency Distribution of Shoe Sizes")
plt.show()
