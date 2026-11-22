import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_travel_data.csv")

# Numerical columns
numerical_columns = [
    "time needed to visit in hrs",
    "Google review rating",
    "Entrance Fee in INR",
    "Number of google review in lakhs"
]

# Create scaler
scaler = StandardScaler()

# Scale numerical data
scaled_data = scaler.fit_transform(df[numerical_columns])

# Convert to DataFrame
scaled_df = pd.DataFrame(
    scaled_data,
    columns=numerical_columns
)

print("Original Numerical Data:")
print(df[numerical_columns].head())

print("\nScaled Numerical Data:")
print(scaled_df.head())