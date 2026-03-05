# Program to create Line Plot and Bar Plot for Monthly Sales Data

import matplotlib.pyplot as plt

# Monthly sales data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [200, 250, 300, 280, 350, 400]

# Line Plot
plt.figure(1)
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales Data - Line Plot")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

# Bar Plot
plt.figure(2)
plt.bar(months, sales)
plt.title("Monthly Sales Data - Bar Plot")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()
