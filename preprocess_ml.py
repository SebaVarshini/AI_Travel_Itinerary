import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_travel_data.csv")

print("Dataset Shape:", df.shape)

# Categorical columns
categorical_columns = [
    "Zone",
    "State",
    "City",
    "Type",
    "Airport with 50km Radius",
    "Weekly Off",
    "DSLR Allowed",
    "Best Time to visit"
]

# One-Hot Encoding
encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)

encoded_data = encoder.fit_transform(df[categorical_columns])

# Convert encoded data into DataFrame
encoded_df = pd.DataFrame(
    encoded_data,
    columns=encoder.get_feature_names_out(categorical_columns)
)

# Combine numerical columns with encoded columns
numerical_columns = [
    "time needed to visit in hrs",
    "Google review rating",
    "Entrance Fee in INR",
    "Number of google review in lakhs"
]

final_df = pd.concat(
    [df[numerical_columns], encoded_df],
    axis=1
)

print("\nOriginal categorical columns:", len(categorical_columns))
print("Encoded columns:", encoded_df.shape[1])
print("Final preprocessed shape:", final_df.shape)

print("\nSample of preprocessed data:")
print(final_df.head())