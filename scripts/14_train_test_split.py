import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Load Dataset
df = pd.read_csv("Data/WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Encode categorical columns
le = LabelEncoder()

for column in df.select_dtypes(include=["object", "string"]).columns:
    df[column] = le.fit_transform(df[column])

# Features (X)
X = df.drop("Attrition", axis=1)

# Target (y)
y = df["Attrition"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("Training Data Shape:", X_train.shape)
print("Testing Data Shape :", X_test.shape)