import pandas as pd
import matplotlib.pyplot as plt

# Create dataset
data = {
    "Name": ["Messi","Ronaldo","Neymar","Modric","DeBruyne","VanDijk","Salah"],
    "Age": [36,38,32,37,33,34,31],
    "Position": ["Forward","Forward","Forward","Midfielder","Midfielder","Defender","Forward"],
    "Goals": [30,28,22,10,15,5,25],
    "Salary": [500000,480000,450000,300000,350000,280000,420000]
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("players.csv", index=False)

# Read CSV
df = pd.read_csv("players.csv")

# Top 5 goals
print("Top 5 Goal Scorers")
print(df.sort_values("Goals", ascending=False).head(5)[["Name","Goals"]])

# Top 5 salaries
print("\nTop 5 Highest Salaries")
print(df.sort_values("Salary", ascending=False).head(5)[["Name","Salary"]])

# Average age
avg_age = df["Age"].mean()
print("\nAverage Age:", avg_age)

# Players above average age
print("\nPlayers Above Average Age")
print(df[df["Age"] > avg_age]["Name"])

# Bar chart for positions
df["Position"].value_counts().plot(kind="bar")
plt.title("Players by Position")
plt.xlabel("Position")
plt.ylabel("Count")
plt.show()
