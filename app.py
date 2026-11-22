from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_travel_data.csv")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():

    # Get user inputs
    state = request.form["state"].strip()
    budget = float(request.form["budget"])
    hours = float(request.form["hours"])
    days = int(request.form["days"])

    # Filter places by state
    places = df[
        df["State"].str.lower() == state.lower()
    ].copy()

    # Remove duplicate tourist places
    places = places.drop_duplicates(subset=["Name"])

    # Filter places that can fit within daily available time
    places = places[
        places["time needed to visit in hrs"] <= hours
    ]

    # Sort by Google rating
    places = places.sort_values(
        by="Google review rating",
        ascending=False
    )

    # Create day-wise itinerary
    itinerary = []
    selected_places = []

    remaining_budget = budget

    for day in range(1, days + 1):

        day_places = []
        day_hours = 0
        day_fee = 0

        for _, place in places.iterrows():

            # Skip already selected places
            if place["Name"] in selected_places:
                continue

            visit_time = float(place["time needed to visit in hrs"])
            entrance_fee = float(place["Entrance Fee in INR"])

            # Check daily time limit
            if day_hours + visit_time > hours:
                continue

            # Check total budget
            if day_fee + entrance_fee > remaining_budget:
                continue

            # Add place to the day
            day_places.append({
                "Name": place["Name"],
                "City": place["City"],
                "Type": place["Type"],
                "Google review rating": place["Google review rating"],
                "Entrance Fee in INR": place["Entrance Fee in INR"],
                "time needed to visit in hrs": place["time needed to visit in hrs"],
                "Significance": place["Significance"],
                "Best Time to visit": place["Best Time to visit"]
            })

            selected_places.append(place["Name"])

            day_hours += visit_time
            day_fee += entrance_fee

        # Add the day only if places were found
        if day_places:

            itinerary.append({
                "day": day,
                "places": day_places,
                "day_hours": round(day_hours, 1),
                "day_fee": round(day_fee, 2)
            })

            remaining_budget -= day_fee

    # Calculate total entrance fee
    total_fee = sum(
        place["Entrance Fee in INR"]
        for place in [
            p
            for day in itinerary
            for p in day["places"]
        ]
    )

    # Number of places
    total_places = sum(
        len(day["places"])
        for day in itinerary
    )

    return render_template(
        "result.html",
        state=state,
        budget=budget,
        hours=hours,
        days=days,
        itinerary=itinerary,
        total_fee=total_fee,
        total_places=total_places
    )


if __name__ == "__main__":
    app.run(debug=True)