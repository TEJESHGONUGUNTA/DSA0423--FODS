import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Dataset
data = {
    "age":[25,35,45,20,30,50],
    "income":[30000,50000,70000,20000,40000,80000],
    "browsing_duration":[5,10,15,3,8,20],
    "device_type":["mobile","desktop","desktop","mobile","tablet","desktop"],
    "purchase":["No","Yes","Yes","No","Yes","Yes"]
}

df = pd.DataFrame(data)

# Encode categorical data
le_device = LabelEncoder()
le_purchase = LabelEncoder()

df["device_type"] = le_device.fit_transform(df["device_type"])
y = le_purchase.fit_transform(df["purchase"])

# Features and target
X = df[["age","income","browsing_duration","device_type"]]

# Train model
model = DecisionTreeClassifier()
model.fit(X,y)

# New customer data
new_customer = pd.DataFrame({
    "age":[28],
    "income":[45000],
    "browsing_duration":[7],
    "device_type":[le_device.transform(["mobile"])[0]]
})

# Prediction
prediction = model.predict(new_customer)

print("Purchase Prediction:", le_purchase.inverse_transform(prediction))
