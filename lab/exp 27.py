import numpy as np
from scipy import stats

# Sample revenue data from 100 customers
revenue = np.random.randint(100, 1000, 100)

# Confidence level
confidence_level = 0.95

# Sample mean
mean_revenue = np.mean(revenue)

# Standard error
std_error = stats.sem(revenue)

# Confidence interval
confidence_interval = stats.t.interval(confidence_level, len(revenue)-1, 
                                       loc=mean_revenue, scale=std_error)

print("Sample Mean Revenue:", mean_revenue)
print("95% Confidence Interval:", confidence_interval)
