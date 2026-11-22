import pandas as pd

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_travel_data.csv")

# User input
city = input("Enter your destination city: ")
budget = float(input("Enter your total budget (INR): "))
available_hours = float(input("Enter available hours per day: "))

# Find places in the selected city
places = df[
    (df["City"].str.lower() == city.lower()) &
    (df["time needed to visit in hrs"] <= available_hours) &
    (df["Entrance Fee in INR"] <= budget)
]

# Sort by rating
places = places.sort_values(
    by="Google review rating",
    ascending=False
).head(5)

# Generate itinerary
if places.empty:

    print("\nSorry! No suitable places found.")

else:

    print("\n" + "=" * 50)
    print("        AI TRAVEL ITINERARY")
    print("=" * 50)

    print(f"\nDestination: {city}")
    print(f"Budget: ₹{budget:.0f}")
    print(f"Available time: {available_hours} hours/day")

    print("\nRecommended Places:\n")

    for i, (_, place) in enumerate(places.iterrows(), start=1):

        print(f"📍 Place {i}: {place['Name']}")
        print(f"   Type: {place['Type']}")
        print(f"   ⭐ Rating: {place['Google review rating']}")
        print(f"   💰 Entrance Fee: ₹{place['Entrance Fee in INR']}")
        print(f"   ⏱️ Visit Time: {place['time needed to visit in hrs']} hours")
        print(f"   🕐 Best Time: {place['Best Time to visit']}")
        print(f"   Significance: {place['Significance']}")
        print()

    print("=" * 50)
    print("Enjoy your trip! ✈️")
    print("=" * 50)