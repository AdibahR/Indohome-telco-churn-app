# 📡 IndoHome Customer Churn Prediction App

A web application to predict the risk of customer churn for **IndoHome**, built with **Streamlit** and powered by **Machine Learning**.

This project implements an end-to-end predictive pipeline that combines data preprocessing, churn modeling, business impact simulation, and interpretability to support **data-driven marketing strategies**.

---

## 🚀 Features

- 🎯 Individual churn prediction
- 📊 Batch prediction with CSV upload
- ⚖️ Threshold tuning with business trade-off simulation
- 📈 Dashboard with analytical insights
- 🔍 Model interpretability using Logistic Regression coefficients
- 🧠 Built using: `scikit-learn`, `imbalanced-learn`, `streamlit`, `plotly`, and more

---

## 🧩 Model Details

| Component           | Description                             |
|---------------------|-----------------------------------------|
| Model               | Logistic Regression + ADASYN            |
| Evaluation Metric   | F2-Score (recall-focused)               |
| Optimal Threshold   | 0.43 (business-optimized)               |
| Interpretation      | Log Odds Coefficients                   |

---

## 🛠️ How to Run Locally

1. **Clone the repository**  
```bash
git clone https://github.com/AdibahR/indohome-telco-churn-app.git
cd indohome-telco-churn-app

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # on Linux/Mac
venv\Scripts\activate     # on Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the app**
```bash
streamlit run app/app.py
```

---

## 📈 Business Impact

Using this ML system, IndoHome:

- Reduces marketing cost by >55%
- Saves more than Rp1.8 Miliar compared to mass-promotion strategies
- Targets only at-risk customers with higher precision

<!-- Force redeploy -->
<!-- force redeploy to reset environment -->
