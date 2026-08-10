# 🏦 Credit Underwriting & Risk Modelling Engine

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A robust machine learning platform designed to help the banking sector categorize customers based on loan priority by analyzing comprehensive profiles including credit scores, previous loans, EMI payment records, salary, and education.

> 🚀 **Data Scale & Impact:** Built and trained by analyzing massive real-world data—over **30 Million+ data points** across **78+ distinct features**.

## ✨ Features

* 🎯 **Smart Customer Categorization:** Automatically segments loan applicants into clear risk/priority categories (P1, P2, P3, P4).
* 📊 **Deep Feature Analysis:** Evaluates a highly dimensional dataset (78+ features) to capture deep financial and demographic patterns.
* 🧠 **Powerful ML Engine:** Powered by an XGBoost Classifier for highly accurate, tree-based predictive modeling.
* 🌐 **Interactive Web App:** User-friendly frontend for seamless batch predictions via CSV upload.
* ☁️ **Cloud Ready:** Fully configured and deployed for live access.

## 💻 Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Frontend / UI** | Streamlit |
| **ML Model** | XGBoost Classifier |
| **Data Tools** | Python, Pandas, NumPy, Matplotlib, Scikit-learn |
| **Deployment** | Streamlit Community Cloud |

## 🛠 Getting Started

### ✅ Prerequisites
* Python 3.9 or higher (Download: [python.org](https://www.python.org/))

### ⚙️ Local Setup

```bash
# Clone the repository
git clone [https://github.com/rahul-meena-63/Credit-Underwriting-Risk-Modelling.git](https://github.com/rahul-meena-63/Credit-Underwriting-Risk-Modelling.git)

# Navigate to the project directory
cd Credit-Underwriting-Risk-Modelling

# Install dependencies
pip install -r requirements.txt

# Run the Application
streamlit run app.py
