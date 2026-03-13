import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Sample dataset
data = {
    "income":[30000,50000,70000,40000,60000,80000],
    "credit_score":[600,650,720,630,690,750],
    "debt_to_income":[35,30,20,40,25,18],
    "employment_duration":[2,5,8,3,6,10],
    "risk":["High","High","Low","High","Low","Low"]
}

df = pd.DataFrame(data)

# Encode target variable
le = LabelEncoder()
df["risk"] = le.fit_transform(df["risk"])

# Features and target
X = df[["income","credit_score","debt_to_income","employment_duration"]]
y = df["risk"]

# CART model
model = DecisionTreeClassifier(criterion="gini")
model.fit(X,y)

# New applicant data
new_applicant = pd.DataFrame({
    "income":[55000],
    "credit_score":[680],
    "debt_to_income":[28],
    "employment_duration":[4]
})

# Prediction
prediction = model.predict(new_applicant)

print("Predicted Credit Risk:", le.inverse_transform(prediction))
