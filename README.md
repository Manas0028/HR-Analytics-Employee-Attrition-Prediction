# HR Analytics - Employee Attrition Prediction

## 📌 Project Overview

This project analyzes employee attrition using Python, Exploratory Data Analysis (EDA), and Machine Learning. The objective is to identify the factors that contribute to employee attrition and build predictive models that help HR teams make data-driven decisions.

---

## 🎯 Objectives

- Analyze employee attrition patterns
- Perform Exploratory Data Analysis (EDA)
- Identify important factors affecting attrition
- Build machine learning models to predict employee attrition
- Compare different machine learning algorithms

---

## 📂 Dataset

**Dataset:** IBM HR Analytics Employee Attrition Dataset

- Total Records: **1470**
- Total Features: **35**

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib

---

## 📊 Exploratory Data Analysis

The following analyses were performed:

- Employee Attrition Distribution
- Department-wise Employee Distribution
- Department-wise Attrition
- Gender Distribution
- Gender vs Attrition
- Overtime vs Attrition
- Age Distribution
- Monthly Income Distribution
- Monthly Income vs Attrition
- Correlation Heatmap

---

## 🤖 Machine Learning Models

### Logistic Regression

- Accuracy: **86.05%**

### Random Forest Classifier

- Accuracy: **86.73%**

Random Forest performed slightly better than Logistic Regression.

---

## 📈 Feature Importance

The Random Forest model identified the following features as the most influential:

- Monthly Income
- Age
- OverTime
- Total Working Years
- Job Level

---

## 💡 Key Business Insights

- Employees working overtime showed higher attrition.
- Monthly Income significantly influences employee retention.
- Research & Development is the largest department.
- Mid-career employees form the majority of the workforce.
- Random Forest achieved better performance than Logistic Regression.

---

## 📁 Project Structure

```
HR_Analytics_Project/
│
├── Data/
├── scripts/
├── hr_attrition_model.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Future Improvements

- Handle class imbalance using SMOTE
- Hyperparameter tuning
- Try XGBoost and LightGBM
- Deploy using Streamlit or Flask

---

## 👨‍💻 Author

**Manas Aswal**

GitHub: https://github.com/Manas0028