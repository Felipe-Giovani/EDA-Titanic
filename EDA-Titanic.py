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

# Example analysis: Survivel by class
plt.figure(figsize=(8, 6))
sns.barplot(x="Pclass", y="Survived", data=df, palette="Blues_d")
plt.title("Survival Rate by Passenger Class", fontsize=16)
plt.xlabel("Passenger Class", fontsize=12)
plt.ylabel("Survival Rate", fontsize=12)
plt.xticks([0, 1, 2], ["1st Class", "2nd Class", "3rd Class"], fontsize=10)
plt.tight_layout()
plt.show()

# Example analysis: Distribution of Age
sns.histplot(df['Age'], bins=20, kde=True)
plt.title("Age Distribution of Passengers")
plt.show()