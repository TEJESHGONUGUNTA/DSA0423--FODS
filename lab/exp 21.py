import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

data = {
    "weight":[150,170,120,140,130,160],
    "color":["red","orange","yellow","red","yellow","orange"],
    "texture":["smooth","rough","smooth","smooth","smooth","rough"],
    "type":["apple","orange","banana","apple","banana","orange"]
}

df = pd.DataFrame(data)

le_color = LabelEncoder()
le_texture = LabelEncoder()
le_type = LabelEncoder()

df["color"] = le_color.fit_transform(df["color"])
df["texture"] = le_texture.fit_transform(df["texture"])
y = le_type.fit_transform(df["type"])

X = df[["weight","color","texture"]]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X,y)

# new fruit as dataframe
new_fruit = pd.DataFrame({
    "weight":[145],
    "color":[le_color.transform(["red"])[0]],
    "texture":[le_texture.transform(["smooth"])[0]]
})

prediction = model.predict(new_fruit)

print("Predicted Fruit:", le_type.inverse_transform(prediction))
