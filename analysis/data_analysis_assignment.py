# Data Analysis and Visualization Assignment

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
try:
    # Load the Iris dataset from seaborn (can be replaced with any CSV)
    df = sns.load_dataset('iris')
except Exception as e:
    print(f"Error loading dataset: {e}")
    exit()

# Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Explore the structure
print("\nData types:")
print(df.dtypes)
print("\nMissing values per column:")
print(df.isnull().sum())

# Clean the dataset (drop rows with missing values)
df_clean = df.dropna()
print(f"\nRows after dropping missing values: {len(df_clean)}")

# Task 2: Basic Data Analysis
print("\nBasic statistics:")
print(df_clean.describe())

# Group by species and compute mean of numerical columns
grouped = df_clean.groupby('species').mean(numeric_only=True)
print("\nMean values by species:")
print(grouped)

# Task 3: Data Visualization

# 1. Line chart: mean sepal length per species (as a trend example)
plt.figure(figsize=(8, 5))
grouped['sepal_length'].plot(marker='o')
plt.title('Mean Sepal Length per Species')
plt.xlabel('Species')
plt.ylabel('Mean Sepal Length (cm)')
plt.grid(True)
plt.show()

# 2. Bar chart: average petal length per species
plt.figure(figsize=(8, 5))
sns.barplot(x='species', y='petal_length', data=df_clean, ci=None)
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.show()

# 3. Histogram: distribution of sepal width
plt.figure(figsize=(8, 5))
plt.hist(df_clean['sepal_width'], bins=15, color='skyblue', edgecolor='black')
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter plot: sepal length vs. petal length
plt.figure(figsize=(8, 5))
sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=df_clean)
plt.title('Sepal Length vs. Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()

# Findings/Observations
print("\nObservations:")
print("- The Iris dataset contains 3 species with distinct petal and sepal measurements.")
print("- Setosa species generally have smaller petal lengths compared to Versicolor and Virginica.")
print("- There is a positive correlation between sepal length and petal length.")
print("- The distribution of sepal width is slightly skewed to the right.")
