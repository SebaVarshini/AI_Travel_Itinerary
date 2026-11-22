import pandas as pd

# Load dataset
df = pd.read_csv("dataset/Top Indian Places to Visit.csv")

print("Original Shape:", df.shape)

# 1. Remove unnecessary column
df = df.drop("Unnamed: 0", axis=1)

# 2. Remove duplicate rows
df = df.drop_duplicates()

# 3. Handle missing values in Weekly Off
df["Weekly Off"] = df["Weekly Off"].fillna("Not Specified")

# 4. Remove extra spaces from text columns
text_columns = df.select_dtypes(include="object").columns

for column in text_columns:
    df[column] = df[column].str.strip()

# 5.Establishment Year has many missing values
# It is not essential for itinerary generation, so remove it
df = df.drop("Establishment Year", axis=1)


# 6. Check missing values after cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# 7. Check duplicates after cleaning
print("\nDuplicate Rows After Cleaning:", df.duplicated().sum())

# 8. Final shape
print("\nFinal Shape:", df.shape)
df.to_csv("dataset/cleaned_travel_data.csv", index=False)

print("\nCleaned dataset saved successfully!")