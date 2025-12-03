
# --------------------------------------------
# Weather Data Visualizer – Mini Project
# --------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Task 1: Load the Dataset
# -------------------------------

df = pd.read_csv("weather.csv")   # <-- Replace with your actual file
print("\n--- DATA HEAD ---")
print(df.head())

print("\n--- INFO ---")
print(df.info())

print("\n--- DESCRIBE ---")
print(df.describe())

# -------------------------------
# Task 2: Data Cleaning
# -------------------------------

# Convert date column
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Drop rows with invalid dates
df = df.dropna(subset=['date'])

# Remove unwanted columns (example)
columns_needed = ['date', 'temperature', 'humidity', 'rainfall']
df = df[columns_needed]

# Fill missing values
df['temperature'] = df['temperature'].fillna(df['temperature'].mean())
df['humidity'] = df['humidity'].fillna(df['humidity'].mean())
df['rainfall'] = df['rainfall'].fillna(0)

# -------------------------------
# Task 3: Statistical Analysis
# -------------------------------

daily_mean = df['temperature'].mean()
daily_max = df['temperature'].max()
daily_min = df['temperature'].min()
daily_std = np.std(df['temperature'])

print("\n--- TEMPERATURE STATS ---")
print("Mean:", daily_mean)
print("Max :", daily_max)
print("Min :", daily_min)
print("Std :", daily_std)

# Monthly grouping
df['month'] = df['date'].dt.month
monthly_stats = df.groupby('month')[['temperature', 'rainfall', 'humidity']].mean()

print("\n--- MONTHLY STATS ---")
print(monthly_stats)

# -------------------------------
# Task 4: Visualizations
# -------------------------------

# Line chart – daily temperature
plt.figure(figsize=(10,5))
plt.plot(df['date'], df['temperature'])
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Daily Temperature Trend")
plt.savefig("daily_temperature.png")
plt.show()

# Bar chart – monthly rainfall
plt.figure(figsize=(10,5))
plt.bar(monthly_stats.index, monthly_stats['rainfall'])
plt.xlabel("Month")
plt.ylabel("Rainfall")
plt.title("Monthly Rainfall")
plt.savefig("monthly_rainfall.png")
plt.show()

# Scatter – humidity vs temperature
plt.figure(figsize=(8,5))
plt.scatter(df['temperature'], df['humidity'])
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.title("Humidity vs Temperature")
plt.savefig("humidity_vs_temp.png")
plt.show()

# Combined figure
plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.plot(df['date'], df['temperature'])
plt.title("Temperature Trend")

plt.subplot(1,2,2)
plt.scatter(df['temperature'], df['humidity'])
plt.title("Humidity vs Temperature")

plt.tight_layout()
plt.savefig("combined_plots.png")
plt.show()

# -------------------------------
# Task 5: Grouping & Aggregation
# -------------------------------

season_mapping = {
    12:"Winter", 1:"Winter", 2:"Winter",
    3:"Spring", 4:"Spring", 5:"Spring",
    6:"Summer", 7:"Summer", 8:"Summer",
    9:"Autumn", 10:"Autumn", 11:"Autumn"
}

df['season'] = df['month'].map(season_mapping)

seasonal_stats = df.groupby('season')[['temperature', 'rainfall', 'humidity']].mean()

print("\n--- SEASONAL STATS ---")
print(seasonal_stats)

# -------------------------------
# Task 6: Export
# -------------------------------

df.to_csv("cleaned_weather_data.csv", index=False)
monthly_stats.to_csv("monthly_summary.csv")

print("\nAll plots saved & cleaned data exported successfully!")
