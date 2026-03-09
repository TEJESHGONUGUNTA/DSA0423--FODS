import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

# Create dataset
data = {
    'Age': [45, 50, 36, 29, 60, 40, 55, 33, 48, 62],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'BloodPressure': [130, 120, 110, 115, 140, 125, 135, 118, 128, 145],
    'Cholesterol': [200, 180, 170, 160, 220, 190, 210, 175, 195, 230],
    'Outcome': ['Good', 'Bad', 'Good', 'Good', 'Bad', 'Good', 'Bad', 'Good', 'Good', 'Bad']
}

df = pd.DataFrame(data)

# Convert categorical data to numeric
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])
df['Outcome'] = le.fit_transform(df['Outcome'])

# Features and target
X = df[['Age','Gender','BloodPressure','Cholesterol']]
y = df['Outcome']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# KNN Model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Prediction
y_pred = knn.predict(X_test)

# Evaluation
print("Predicted values:", y_pred)
print("Actual values:", y_test.values)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))

print("\nClassification Report:\n", classification_report(y_test, y_pred))
