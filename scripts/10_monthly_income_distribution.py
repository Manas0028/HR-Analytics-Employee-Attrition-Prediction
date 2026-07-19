import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("Data/WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Set Theme
sns.set_theme(style="whitegrid")

# Create Figure
plt.figure(figsize=(10,5))

# Monthly Income Distribution
sns.histplot(df["MonthlyIncome"], bins=20, kde=True, color="green")

plt.title("Monthly Income Distribution")
plt.xlabel("Monthly Income")
plt.ylabel("Number of Employees")

plt.show()