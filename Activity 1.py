import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

# -------------------------------
# STEP 1: Generate Large Dataset
# -------------------------------

np.random.seed(42)

dishes_clean = ["Chicken Burger", "Veggie Wrap", "Pasta Salad"]
dishes_dirty = [
    "Chiken Burger",
    "chicken burger",
    "veggie wrap",
    "Veggie wrap",
    "pasta salad",
    "Chicken burger"
]

all_choices = dishes_clean + dishes_dirty

data = {
    "Student_ID": range(1, 1001),
    "Dish": np.random.choice(all_choices, 1000)
}

df = pd.DataFrame(data)

print("Raw Data Sample:")
print(df.head())

# --------------------------------
# STEP 2: Data Cleaning
# --------------------------------

df["Dish"] = df["Dish"].str.lower()

df["Dish"] = df["Dish"].replace({
    "chiken burger": "chicken burger"
})

df["Dish"] = df["Dish"].str.title()

print("\nCleaned Data Sample:")
print(df.head())

# --------------------------------
# STEP 3: Analysis
# --------------------------------

counts = df["Dish"].value_counts()

print("\nDish Preferences:")
print(counts)

# --------------------------------
# STEP 4: Save Cleaned Data
# --------------------------------

df.to_csv("cleaned_cafeteria_data.csv", index=False)

# --------------------------------
# STEP 5: Visualization
# --------------------------------

plt.figure()
counts.plot(kind="bar")
plt.title("Cafeteria Dish Preferences (1000 Students)")
plt.xlabel("Dish")
plt.ylabel("Number of Students")
plt.show()
