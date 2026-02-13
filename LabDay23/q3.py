import pandas as pd
import numpy as np
import os

print("Current working directory:")
print(os.getcwd())

df = pd.read_csv("sales.csv")

df["Total"] = df["Quantity"] * df["Price"]

total_sales = np.sum(df["Total"])
average_sales = np.mean(df["Total"])
std_dev = np.std(df["Total"])

best_product = df.groupby("Product")["Quantity"].sum().idxmax()

print("\nData:")
print(df)

print("\nTotal Sales:", total_sales)
print("Average Daily Sales:", average_sales)
print("Standard Deviation:", std_dev)
print("Best Selling Product:", best_product)