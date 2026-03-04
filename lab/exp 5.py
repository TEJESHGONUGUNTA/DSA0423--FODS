import numpy as np

# 4x4 matrix (Rows = Students, Columns = Subjects)
# Order: Math, Science, English, History
student_scores = np.array([
    [85, 78, 92, 88],
    [76, 85, 80, 90],
    [90, 88, 84, 86],
    [70, 75, 78, 72]
])

print("Student Scores Matrix:")
print(student_scores)

# 1️⃣ Calculate average score for each subject (column-wise mean)
subject_averages = np.mean(student_scores, axis=0)

print("\nAverage Score for Each Subject:")
print("Math:", subject_averages[0])
print("Science:", subject_averages[1])
print("English:", subject_averages[2])
print("History:", subject_averages[3])

# 2️⃣ Find subject with highest average
subjects = ["Math", "Science", "English", "History"]
highest_avg_index = np.argmax(subject_averages)

print("\nSubject with Highest Average Score:")
print(subjects[highest_avg_index])
