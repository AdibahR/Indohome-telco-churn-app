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
| Interpretation      | Log Odds Coefficients (not SHAP/LIME)   |

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

## 📂 Project Structure
.
├── app/                                # Source code untuk Streamlit App
│   ├── app.py                          # Entry point utama aplikasi web
│   ├── utils.py                        # Fungsi utilitas seperti interpretasi koefisien
│   └── chapter1_summary.md            # Ringkasan pemahaman bisnis dari Chapter 1
│
├── deployment/                         # Output hasil deployment dan konfigurasi
│   ├── final_model_pipeline.pkl        # Pipeline model produksi (preprocessing + ADASYN + LogisticRegression)
│   ├── final_feature_list.json         # Daftar fitur input model
│   ├── threshold.json                  # Nilai threshold optimal (0.43)
│   ├── pipeline_version.txt            # Metadata versi pipeline
│   ├── X_train_df.csv                  # Data training terproses (untuk interpretasi)
│   └── telco_customer_data.csv         # Dataset asli untuk batch prediction dan dashboard
│
├── Dataset_Telco Customer Churn.csv    # Dataset original Telco Customer Churn (as-is)
├── df_analisis.csv                     # Dataset hasil eksplorasi dan analytics
├── df_model.csv                        # Dataset siap modeling (feature engineered)
│
├── Logo.png                            # Logo yang digunakan dalam UI Streamlit
├── Telco Customer Churn.ipynb          # Notebook utama eksplorasi dan modelling
├── requirements.txt                    # Dependencies Python untuk menjalankan aplikasi
└── README.md                           # Dokumentasi proyek

---

## 📈 Business Impact

Using this ML system, IndoHome:

- Reduces marketing cost by >55%
- Saves more than Rp1.8 Miliar compared to mass-promotion strategies
- Targets only at-risk customers with higher precision


