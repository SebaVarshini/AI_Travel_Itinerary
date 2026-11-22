import pandas as pd

df = pd.read_csv("dataset/cleaned_travel_data.csv")

tamil_nadu = df[
    df["State"].astype(str).str.strip().str.lower() == "tamil nadu"
]

print("\nTOTAL TAMIL NADU PLACES:", len(tamil_nadu))

print("\nTamil Nadu Cities:")
print(tamil_nadu["City"].value_counts())

print("\nTamil Nadu Places:")
print(
    tamil_nadu[
        ["Name", "City", "Type", "Entrance Fee in INR",
         "time needed to visit in hrs"]
    ].to_string(index=False)
)
