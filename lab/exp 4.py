import pandas as pd

# Sample property_data DataFrame
data = {
    "property_id": [1, 2, 3, 4, 5],
    "location": ["Hyderabad", "Mumbai", "Hyderabad", "Chennai", "Mumbai"],
    "bedrooms": [3, 5, 4, 6, 2],
    "area_sqft": [1500, 2500, 1800, 3000, 1200],
    "listing_price": [7500000, 15000000, 9000000, 20000000, 6000000]
}

property_data = pd.DataFrame(data)

print("Original Data:")
print(property_data)

# 1️⃣ Average listing price in each location
avg_price_location = property_data.groupby("location")["listing_price"].mean()
print("\nAverage Listing Price by Location:")
print(avg_price_location)

# 2️⃣ Number of properties with more than 4 bedrooms
more_than_4_bed = property_data[property_data["bedrooms"] > 4].shape[0]
print("\nNumber of Properties with more than 4 bedrooms:", more_than_4_bed)

# 3️⃣ Property with the largest area
largest_area_property = property_data.loc[property_data["area_sqft"].idxmax()]
print("\nProperty with Largest Area:")
print(largest_area_property)
