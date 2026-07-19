import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("Data/WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Chart Style
sns.set_theme(style="whitegrid")

# Create Figure
plt.figure(figsize=(8,5))

# Histogram
sns.histplot(data=df, x="Age", bins=15, kde=True)

plt.title("Age Distribution of Employees")
plt.xlabel("Age")
plt.ylabel("Number of Employees")

plt.show()