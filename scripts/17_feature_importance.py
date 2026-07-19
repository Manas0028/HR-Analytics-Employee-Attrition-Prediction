import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# ==========================
# Load Dataset
# ==========================
df = pd.read_csv("Data/WA_Fn-UseC_-HR-Employee-Attrition.csv")

# ==========================
# Encode Categorical Columns
# ==========================
le = LabelEncoder()

for column in df.select_dtypes(include=["object", "string"]).columns:
    df[column] = le.fit_transform(df[column])

# ==========================
# Features and Target
# ==========================
X = df.drop("Attrition", axis=1)
y = df["Attrition"]

# ==========================
# Train-Test Split
# ==========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# ==========================
# Train Random Forest
# ==========================
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# ==========================
# Feature Importance
# ==========================
importance = model.feature_importances_

feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": importance
})

# Sort values
feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

print(feature_importance)

# ==========================
# Plot Top 10 Features
# ==========================
plt.figure(figsize=(10,6))

sns.barplot(
    data=feature_importance.head(10),
    x="Importance",
    y="Feature"
)

plt.title("Top 10 Important Features")
plt.xlabel("Importance Score")
plt.ylabel("Feature")

plt.show()