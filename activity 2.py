import pandas as pd
import numpy as np

# -------------------------------
# STEP 1: Generate Large Dataset
# -------------------------------

np.random.seed(100)

students = [f"Student_{i}" for i in range(1, 301)]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

data = []

for student in students:
    for day in days:
        sleep_hours = np.random.normal(loc=7, scale=1.5)
        sleep_hours = round(max(4, min(10, sleep_hours)), 2)
        data.append([student, day, sleep_hours])

sleep_df = pd.DataFrame(data, columns=["Student", "Day", "Sleep_Hours"])

print("\n===== DATA SAMPLE =====")
print(sleep_df.head())

# -------------------------------
# STEP 2: Average Sleep Per Student
# -------------------------------

avg_sleep = sleep_df.groupby("Student")["Sleep_Hours"].mean()

print("\n===== AVERAGE SLEEP (FIRST 10 STUDENTS) =====")
print(avg_sleep.head(10))

# -------------------------------
# STEP 3: Overall Statistics
# -------------------------------

overall_avg = sleep_df["Sleep_Hours"].mean()
max_sleep = sleep_df["Sleep_Hours"].max()
min_sleep = sleep_df["Sleep_Hours"].min()

print("\n===== OVERALL STATISTICS =====")
print("Overall Average Sleep:", round(overall_avg,2))
print("Maximum Sleep Recorded:", max_sleep)
print("Minimum Sleep Recorded:", min_sleep)

# -------------------------------
# STEP 4: Best & Worst Sleeper
# -------------------------------

best_sleeper = avg_sleep.idxmax()
worst_sleeper = avg_sleep.idxmin()

print("\nBest Sleeper:", best_sleeper, "with", round(avg_sleep.max(),2), "hours average")
print("Worst Sleeper:", worst_sleeper, "with", round(avg_sleep.min(),2), "hours average")

# -------------------------------
# STEP 5: Save Dataset
# -------------------------------

sleep_df.to_csv("smartwatch_large_dataset.csv", index=False)

print("\nSleep dataset saved successfully!")
