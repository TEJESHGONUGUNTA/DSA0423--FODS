# Program to plot Temperature (Line Plot) and Rainfall (Scatter Plot)

import matplotlib.pyplot as plt

# Months of the year
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

# Monthly temperature data (°C)
temperature = [22, 24, 27, 30, 33, 35, 34, 33, 31, 29, 26, 23]

# Monthly rainfall data (mm)
rainfall = [10, 20, 30, 40, 60, 120, 200, 180, 140, 80, 30, 15]

# Line Plot for Temperature
plt.figure(1)
plt.plot(months, temperature, marker='o')
plt.title("Monthly Temperature - Line Plot")
plt.xlabel("Months")
plt.ylabel("Temperature (°C)")
plt.show()

# Scatter Plot for Rainfall
plt.figure(2)
plt.scatter(months, rainfall)
plt.title("Monthly Rainfall - Scatter Plot")
plt.xlabel("Months")
plt.ylabel("Rainfall (mm)")
plt.show()
