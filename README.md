# ✈️ AI Travel Itinerary Generator

An intelligent travel planning application that generates personalized tourist itineraries based on the user's destination, budget, available time, and trip duration.

## 🌍 Project Overview

AI Travel Itinerary Generator helps users plan their trips by recommending suitable tourist destinations and organizing them into a day-wise travel itinerary.

The application considers user preferences and travel constraints to make trip planning easier and more convenient.

## ✨ Features

- **Destination-Based Recommendations:** Enter a destination state to discover tourist attractions.
- **Budget-Based Planning:** Generate recommendations according to the available budget.
- **Time-Based Selection:** Consider available visiting hours per day.
- **Day-Wise Itinerary:** Organize selected tourist places across multiple days.
- **Tourist Place Information:** View city, category, Google rating, entrance fee, visit duration, best time to visit, and significance.
- **Interactive Web Interface:** User-friendly black and blue themed frontend.

## 🛠️ Technologies Used

- Python
- Flask
- Pandas
- HTML
- CSS
- Machine Learning / Data Preprocessing

## 📂 Project Structure

```text
AI_Travel_Itinerary/
│
├── app.py
├── eda.py
├── preprocess.py
├── preprocess_ml.py
├── feature_scaling.py
├── feature_selection.py
├── recommendation.py
├── itinerary_generator.py
│
├── dataset/
│   ├── Top Indian Places to Visit.csv
│   └── cleaned_travel_data.csv
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/SebaVarshini/AI_Travel_Itinerary.git
```

### 2. Navigate to the Project Folder

```bash
cd AI_Travel_Itinerary
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install flask pandas numpy scikit-learn
```

### 6. Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## 🚀 How It Works

1. Enter the destination state.
2. Provide the total travel budget.
3. Enter available visiting hours per day.
4. Select the number of travel days.
5. Generate the personalized itinerary.
6. Explore recommended tourist destinations and day-wise travel details.

## 🎯 Project Objective

To simplify travel planning by combining data processing, intelligent destination recommendations, and an interactive web application.

## 👩‍💻 Developer

**SebaVarshini**

GitHub: https://github.com/SebaVarshini

---

*Explore Smarter, Travel Better!* 🌍