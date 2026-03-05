# Program to calculate average fuel efficiency and percentage improvement

import numpy as np

# Fuel efficiency of different car models (miles per gallon)
fuel_efficiency = np.array([22, 25, 28, 30, 35])

# Calculate average fuel efficiency
average_efficiency = np.mean(fuel_efficiency)

# Select two car models
model1 = fuel_efficiency[0]
model2 = fuel_efficiency[3]

# Calculate percentage improvement
percentage_improvement = ((model2 - model1) / model1) * 100

# Display results
print("Fuel Efficiency Data:", fuel_efficiency)
print("Average Fuel Efficiency:", average_efficiency, "mpg")
print("Percentage Improvement:", percentage_improvement, "%")
