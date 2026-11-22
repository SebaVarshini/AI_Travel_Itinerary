import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_travel_data.csv")

# -------------------------------
# 1. Tourist Places by State
# -------------------------------

state_counts = df["State"].value_counts()

print("Top 10 States:")
print(state_counts.head(10))

plt.figure(figsize=(10, 6))
state_counts.head(10).plot(kind="bar")
plt.title("Top 10 States by Number of Tourist Places")
plt.xlabel("State")
plt.ylabel("Number of Places")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# -------------------------------
# 2. Tourist Places by Type
# -------------------------------

type_counts = df["Type"].value_counts()

print("\nTop Tourist Place Types:")
print(type_counts.head(10))

plt.figure(figsize=(10, 6))
type_counts.head(10).plot(kind="bar")
plt.title("Most Common Tourist Place Types")
plt.xlabel("Type")
plt.ylabel("Number of Places")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# -------------------------------
# 3. Rating Distribution
# -------------------------------

plt.figure(figsize=(8, 5))
df["Google review rating"].plot(kind="hist", bins=10)
plt.title("Distribution of Google Review Ratings")
plt.xlabel("Google Review Rating")
plt.ylabel("Number of Places")
plt.tight_layout()
plt.show()


# -------------------------------
# 4. Entrance Fee Distribution
# -------------------------------

plt.figure(figsize=(8, 5))
df["Entrance Fee in INR"].plot(kind="hist", bins=10)
plt.title("Distribution of Entrance Fees")
plt.xlabel("Entrance Fee (INR)")
plt.ylabel("Number of Places")
plt.tight_layout()
plt.show()