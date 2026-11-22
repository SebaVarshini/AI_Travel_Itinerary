import pandas as pd

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_travel_data.csv")

# Select useful features for travel recommendation
selected_features = [
    "City",
    "Type",
    "time needed to visit in hrs",
    "Google review rating",
    "Entrance Fee in INR",
    "Significance",
    "Best Time to visit"
]

selected_df = df[selected_features]

print("Selected Features:")
print(selected_df.columns.tolist())

print("\nSelected Dataset Shape:")
print(selected_df.shape)

print("\nSample Data:")
print(selected_df.head())