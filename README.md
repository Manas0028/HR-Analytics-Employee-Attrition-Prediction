# 📊 HR Analytics – Employee Attrition Prediction

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-yellow?style=for-the-badge)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-green?style=for-the-badge)
![GitHub](https://img.shields.io/badge/GitHub-Portfolio-black?style=for-the-badge&logo=github)

</p>

---

# 📌 Project Overview

Employee attrition is one of the biggest challenges faced by organizations. This project analyzes the IBM HR Analytics dataset to understand employee behavior and predict attrition using Machine Learning.

The project includes:

- Exploratory Data Analysis (EDA)
- Data Preprocessing
- Feature Engineering
- Logistic Regression
- Random Forest Classification
- Feature Importance Analysis
- Model Saving using Joblib

---

# 🎯 Objectives

- Analyze employee attrition trends
- Visualize HR data
- Build predictive models
- Compare machine learning algorithms
- Identify important factors affecting employee attrition

---

# 📂 Project Structure

```text
HR-Analytics-Employee-Attrition-Prediction
│
├── Data/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
│
├── Images/
│   ├── age_distribution.png
│   ├── correlation_heatmap.png
│   ├── department_distribution.png
│   ├── feature_importance.png
│   ├── gender_distribution.png
│   ├── income_vs_attrition.png
│   ├── monthly_income_distribution.png
│   └── overtime_attrition.png
│
├── scripts/
├── hr_attrition_model.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📊 Dataset

- **Dataset:** IBM HR Analytics Employee Attrition
- **Rows:** 1470
- **Columns:** 35
- **Target Variable:** Attrition

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- VS Code
- Git
- GitHub

---

# 📈 Exploratory Data Analysis

## Department-wise Employee Distribution

![Department Distribution](Images/department_distribution.png)

---

## Gender Distribution

![Gender Distribution](Images/gender_distribution.png)

---

## Overtime vs Attrition

![Overtime Attrition](Images/overtime_attrition.png)

---

## Age Distribution

![Age Distribution](Images/age_distribution.png)

---

## Monthly Income Distribution

![Monthly Income Distribution](Images/monthly_income_distribution.png)

---

## Income vs Attrition

![Income vs Attrition](Images/income_vs_attrition.png)

---

## Correlation Heatmap

![Correlation Heatmap](Images/correlation_heatmap.png)

---

# 🤖 Machine Learning Models

| Model | Accuracy |
|--------|---------:|
| Logistic Regression | **86.05%** |
| Random Forest | **86.73%** |

🏆 **Best Model:** Random Forest

---

# ⭐ Feature Importance

![Feature Importance](Images/feature_importance.png)

Important features identified by the model:

- Monthly Income
- Overtime
- Age
- Total Working Years
- Job Level
- Job Satisfaction
- Environment Satisfaction

---

# 💡 Business Insights

- Employees working overtime have a higher probability of leaving.
- Employees with lower monthly income show higher attrition.
- Younger employees tend to leave more frequently.
- Job satisfaction and work-life balance significantly affect retention.
- HR departments can use predictive analytics to reduce employee turnover.

---

# 🚀 How to Run

Clone the repository

```bash
git clone https://github.com/Manas0028/HR-Analytics-Employee-Attrition-Prediction.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python scripts/hr_analytics.py
```

Run Machine Learning Models

```bash
python scripts/15_logistic_regression.py
python scripts/16_random_forest.py
python scripts/17_feature_importance.py
python scripts/18_save_model.py
```

---

# 📌 Project Highlights

- ✔ Data Cleaning
- ✔ Data Visualization
- ✔ Machine Learning
- ✔ Feature Engineering
- ✔ Logistic Regression
- ✔ Random Forest
- ✔ Model Evaluation
- ✔ Feature Importance
- ✔ Saved ML Model

---

# 🔮 Future Enhancements

- Hyperparameter Tuning
- XGBoost Model
- Streamlit Dashboard
- Flask API
- Power BI Dashboard
- Real-time Prediction System

---

# 👨‍💻 Author

## Manas Aswal

**B.Tech – Information Technology**

**Aspiring Data Analyst**

### Connect with Me

- GitHub: https://github.com/Manas0028
- LinkedIn: *(https://www.linkedin.com/in/manas-aswal-704876288)*

---

## ⭐ If you like this project, don't forget to Star this repository!