import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load Dataset
df = pd.read_csv("Data/WA_Fn-UseC_-HR-Employee-Attrition.csv")

print("Original Dataset Shape:", df.shape)

# Create Label Encoder
le = LabelEncoder()

# Convert all object (text) columns into numbers
for column in df.select_dtypes(include="object").columns:
    df[column] = le.fit_transform(df[column])

print("\nDataset after Encoding:\n")
print(df.head())

print("\nData Types:\n")
print(df.dtypes)