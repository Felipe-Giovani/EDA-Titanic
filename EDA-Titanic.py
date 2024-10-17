import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the data set
df = pd.read_csv("data/titanic.csv")

# Clean the data - Drop the rows with missing values for simplicity
df.dropna(inplace=True)

# Set a Style for the plots
sns.set(style="whitegrid")

# Survival by class
plt.figure(figsize=(8, 6))
sns.barplot(x="Pclass", y="Survived", data=df, palette="Blues_d")
plt.title("Survival Rate by Passenger Class", fontsize=16)
plt.xlabel("Passenger Class", fontsize=12)
plt.ylabel("Survival Rate", fontsize=12)
plt.xticks([0, 1, 2], ["1st Class", "2nd Class", "3rd Class"], fontsize=10)
plt.tight_layout()
plt.show()

# Distribution of Age
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], bins=20, kde=True, color='green')

# Calculate mean age using numpy and add to the plot
mean_age = np.mean(df['Age'])
plt.axvline(mean_age, color='red', linestyle='--', label=f'mean_age: {mean_age:.2f}')

plt.title("Age Distribuition of Titanic Passengers", fontsize=16)
plt.xlabel("Age", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.legend()
plt.tight_layout()
plt.show()

# Survival Rate by Gender
plt.figure(figsize=(8, 6))
sns.barplot(x="Sex", y="Survived", data=df, palette="Set2")
plt.title("Survival Rate by Gender", fontsize=16)
plt.xlabel("Gender", fontsize=12)
plt.ylabel("Survival Rate", fontsize=12)
plt.xticks([0, 1], ["Female", "Male"], fontsize=10)
plt.tight_layout()
plt.show()






