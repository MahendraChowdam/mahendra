import pandas as pd
import numpy as np

# Given data
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 90},
    {"name": "Eva", "score": 88}
]

# Convert to Pandas DataFrame
df = pd.DataFrame(students)
print("DataFrame:")
print(df)
print()

# Convert score column to NumPy array
scores = df["score"].values

# Calculate statistics using NumPy
mean_score = np.mean(scores)
median_score = np.median(scores)
std_dev = np.std(scores)

print("Mean score:", mean_score)
print("Median score:", median_score)
print("Standard deviation:", std_dev)
print()

# Add above_average column
df["above_average"] = df["score"] > mean_score

print("Final DataFrame with above_average column:")
print(df)
