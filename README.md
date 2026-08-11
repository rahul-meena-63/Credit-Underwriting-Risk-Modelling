# 🏦 Credit Underwriting & Risk Modelling Engine

![License](https://img.shields.io/badge/License-MIT-yellow)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Model](https://img.shields.io/badge/Model-XGBoost-orange)

An end-to-end machine learning pipeline that helps banks categorize loan applicants by risk priority, using credit scores, loan history, EMI records, salary, and education data — built and validated on real-world scale data.

> 🚀 **Data Scale & Impact:** Trained on **30 Million+ records** and **85+ features** from internal and CIBIL data, aimed at helping reduce the bank's GNPA/NNPA.

---

## ✨ Features

- 🎯 **Smart Risk Categorization:** Segments loan applicants into 4 clear priority categories (P1, P2, P3, P4)
- 📊 **Deep Feature Analysis:** Evaluates 85+ features using statistical feature selection (VIF, ANOVA, Chi-Square) to isolate the strongest predictors
- 🧠 **Powerful ML Engine:** Multi-class classification via XGBoost, Random Forest, and Decision Tree, with XGBoost tuned to **90% accuracy**
- 🌐 **Interactive Web App:** Streamlit frontend for real-time and batch (CSV upload) credit risk predictions
- ☁️ **Cloud Ready:** Deployed and accessible live, no local setup required to try it

---

## 💻 Tech Stack

| Layer | Technology |
|---|---|
| Frontend / UI | Streamlit |
| ML Model | XGBoost, Random Forest, Decision Tree |
| Statistical Analysis | VIF, ANOVA, Chi-Square |
| Data Tools | Python, Pandas, NumPy, Scikit-Learn |
| Deployment | Streamlit Community Cloud |

---

## 📈 Model Performance

| Model | Accuracy |
|---|---|
| XGBoost (tuned) | **90%** |
| Random Forest | **79%** |
| Decision Tree | **71%**|

---

## 🧹 Data Preprocessing & Feature Engineering

- Cleaned and processed 30M+ records across 85+ features from internal and CIBIL sources
- Removed multicollinearity using **VIF (Variance Inflation Factor)**
- Selected statistically significant features using **ANOVA** (continuous variables) and **Chi-Square** (categorical variables)
- Engineered features to better capture applicant risk profile before model training

---

## 🚀 Getting Started

### ✅ Prerequisites
- Python 3.9 or higher ([Download](https://python.org))

### ⚙️ Local Setup

```bash
# Clone the repository
git clone https://github.com/rahul-meena-63/Credit-Underwriting-Risk-Modelling.git

# Navigate to the project directory
cd Credit-Underwriting-Risk-Modelling

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

### 🔗 Live Demo

[Launch the Credit Risk Web App Here](https://credit-risk-modelling-predictor-l6vb6mcaejpknq8hndzuwy.streamlit.app/)

---

## 📁 Project Structure

```
Credit-Underwriting-Risk-Modelling/
├── app.py                  # Streamlit web app
├── data/                   # Sample/processed data
├── notebooks/               # EDA and model development notebooks
├── models/                  # Trained model files
├── requirements.txt
└── README.md
```
