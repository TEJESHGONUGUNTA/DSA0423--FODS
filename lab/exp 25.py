import numpy as np
import pandas as pd

# Population dataset
data = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

df = pd.DataFrame(data, columns=["Values"])

# Mean estimation
mean_estimate = np.mean(df["Values"])

# Variance estimation
variance_estimate = np.var(df["Values"])

# Random sampling
sample = df["Values"].sample(n=5)

print("Population Data:")
print(df)

print("\nSample Data:")
print(sample)

print("\nMean Estimate:", mean_estimate)
print("Variance Estimate:", variance_estimate)
