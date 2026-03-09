import pandas as pd
import numpy as np

# Sample dataset (daily temperatures example)
data = {
    'City': ['Chennai','Chennai','Chennai','Delhi','Delhi','Delhi','Mumbai','Mumbai','Mumbai'],
    'Temperature': [32,34,33,25,28,30,29,30,31]
}

df = pd.DataFrame(data)

# 1. Mean temperature for each city
mean_temp = df.groupby('City')['Temperature'].mean()
print("Mean Temperature for each city:")
print(mean_temp)

# 2. Standard deviation of temperature for each city
std_temp = df.groupby('City')['Temperature'].std()
print("\nStandard Deviation for each city:")
print(std_temp)

# 3. City with highest temperature range
temp_range = df.groupby('City')['Temperature'].max() - df.groupby('City')['Temperature'].min()
city_highest_range = temp_range.idxmax()
print("\nCity with highest temperature range:", city_highest_range)

# 4. City with most consistent temperature (lowest std deviation)
city_consistent = std_temp.idxmin()
print("\nCity with most consistent temperature:", city_consistent)
