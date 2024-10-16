import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data set

df = pd.read_csv("titanic.csv")

# Clean the data

df.dropna(inplace=True)

# Example analysis: Survivel by class
sns.barplot(x="Pclass", y="Survived", data=df)
plt.title("Survival by Class")
plt.show()

# Example analysis: Distribution of Age
sns.histplot(df['Age'], bins=20, kde=True)
plt.title("Age Distribution of Passengers")
plt.show()