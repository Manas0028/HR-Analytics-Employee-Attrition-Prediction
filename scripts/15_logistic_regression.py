import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

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
# Train Model
# ==========================
model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

# ==========================
# Prediction
# ==========================
y_pred = model.predict(X_test)

# ==========================
# Model Evaluation
# ==========================
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))