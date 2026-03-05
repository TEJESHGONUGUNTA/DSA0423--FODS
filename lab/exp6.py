# Program to calculate average velocity of a projectile using NumPy

import numpy as np

# Time intervals (seconds)
time = np.array([0, 1, 2, 3, 4])

# Vertical positions of the projectile (meters)
position = np.array([0, 5, 15, 20, 18])

# Calculate change in position
change_position = position[-1] - position[0]

# Calculate change in time
change_time = time[-1] - time[0]

# Calculate average velocity
average_velocity = change_position / change_time

# Display the result
print("Time values:", time)
print("Position values:", position)
print("Average Velocity of the projectile =", average_velocity, "m/s")
