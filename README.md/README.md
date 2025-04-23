# IndoHome Customer Churn Prediction App

A Streamlit web application to predict customer churn and support data-driven retention strategies for IndoHome.

## Features

- **Single Customer Prediction**  
  Input customer data and get churn probability, risk level, and recommended action.

- **Batch Prediction**  
  Upload a CSV file to predict churn risk for multiple customers at once.

- **Model Interpretation**  
  Understand what features drive churn using Logistic Regression coefficients.

- **Customer Segmentation**  
  View churn risk segments (loyal, low risk, medium, high risk) and their business characteristics.

## How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run App

```bash
streamlit run app/app.py
```

### 3. Access in Browser

Streamlit will open the app at [http://localhost:8501](http://localhost:8501)

## Author

Rina Adibah — [LinkedIn](https://www.linkedin.com/in/rina-adibah/)  
Made for final project in Data Science Track
