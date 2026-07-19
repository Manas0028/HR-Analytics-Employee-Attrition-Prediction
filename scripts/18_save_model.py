import joblib
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load Dataset
df = pd.read_csv("Data/WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Encode categorical columns
le = LabelEncoder()

for column in df.select_dtypes(include=["object", "string"]).columns:
    df[column] = le.fit_transform(df[column])

# Features & Target
X = df.drop("Attrition", axis=1)
y = df["Attrition"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# Train Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Save Model
joblib.dump(model, "hr_attrition_model.pkl")

print("Model saved successfully!")