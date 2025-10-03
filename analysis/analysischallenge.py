# 🔹 Challenge: Perform basic data analysis on a CSV file and generate insights!

import pandas as pd

# Create a sample sales_data.csv if it doesn't exist
import os
if not os.path.exists("sales_data.csv"):
    sample_data = """Date,Product,Quantity Sold,Revenue ($)
2023-10-01,Widget,10,200
2023-10-01,Gadget,5,150
2023-10-02,Widget,8,160
2023-10-02,Gadget,12,360
2023-10-03,Widget,15,300
2023-10-03,Gadget,7,210
"""
    with open("sales_data.csv", "w") as f:
        f.write(sample_data)

# Load the CSV file using pandas
df = pd.read_csv("sales_data.csv")

# Calculate the total revenue
total_revenue = df["Revenue ($)"].sum()

# Find the best-selling product (based on Quantity Sold)
best_selling = df.groupby("Product")["Quantity Sold"].sum().idxmax()

# Identify the day with the highest sales (by Revenue)
best_day = df.groupby("Date")["Revenue ($)"].sum().idxmax()

# Prepare insights
insights = (
    f"Sales Data Analysis Summary\n"
    f"--------------------------\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Best-Selling Product: {best_selling}\n"
    f"Day with Highest Sales: {best_day}\n"
)

# Save the results to sales_summary.txt
with open("sales_summary.txt", "w") as f:
    f.write(insights)

# Print the insights in a user-friendly format
print(insights)

