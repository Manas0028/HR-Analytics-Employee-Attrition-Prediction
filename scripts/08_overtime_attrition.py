import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("Data/WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Set Theme
sns.set_theme(style="whitegrid")

# Create Figure
plt.figure(figsize=(7,5))

# Overtime vs Attrition
sns.countplot(data=df, x="OverTime", hue="Attrition")

# Title and Labels
plt.title("Overtime vs Employee Attrition")
plt.xlabel("OverTime")
plt.ylabel("Number of Employees")

plt.legend(title="Attrition")

# Show Chart
plt.show()