import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Sample clinical trial data
# Control group (placebo)
control = np.array([50, 52, 48, 49, 51, 47, 50, 53])

# Treatment group (new drug)
treatment = np.array([55, 58, 54, 57, 56, 59, 60, 57])

# Perform independent t-test
t_stat, p_value = stats.ttest_ind(control, treatment)

print("T-statistic:", t_stat)
print("P-value:", p_value)

# Check significance
alpha = 0.05
if p_value < alpha:
    print("Result: Significant difference between treatment and control group")
else:
    print("Result: No significant difference")

# Visualization
groups = ["Control", "Treatment"]
means = [np.mean(control), np.mean(treatment)]

plt.bar(groups, means)
plt.title("Effect of Treatment vs Placebo")
plt.xlabel("Groups")
plt.ylabel("Average Response")
plt.show()
