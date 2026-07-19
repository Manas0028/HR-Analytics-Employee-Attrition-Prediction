import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("Data/WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Set Theme
sns.set_theme(style="whitegrid")

# Gender vs Attrition
plt.figure(figsize=(6,5))

sns.countplot(data=df, x="Gender", hue="Attrition")

plt.title("Gender vs Employee Attrition")
plt.xlabel("Gender")
plt.ylabel("Number of Employees")

plt.legend(title="Attrition")

plt.show()