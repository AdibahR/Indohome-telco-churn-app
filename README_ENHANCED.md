# 🏠 IndoHome Customer Churn Analytics
## End-to-End Machine Learning Project for Telecommunications Customer Retention

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://indohome-telco-churn-app-jaqqq4c38dcepxzzitrbzc.streamlit.app)
[![Tableau Dashboard](https://img.shields.io/badge/Tableau-Dashboard-blue)](https://public.tableau.com/views/IndoHomeChurnAnalysisDashboard/Dashboard1-ExecutiveOverview?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-green)](https://github.com/AdibahR/Indohome-telco-churn-app)

---

## 🎯 Executive Summary

This project develops a comprehensive **customer churn prediction system** for IndoHome telecommunications, combining advanced machine learning, interactive dashboards, and a production-ready web application. By leveraging data science to identify at-risk customers, this solution enables **data-driven retention strategies** that can reduce marketing costs by 55% and save over **Rp1.8 Billion** compared to mass-promotion approaches.

### 🚀 **Live Demos**
- **🌐 [Streamlit Web Application](https://indohome-telco-churn-app-jaqqq4c38dcepxzzitrbzc.streamlit.app)** - Interactive prediction tool
- **📊 [Tableau Dashboard](https://public.tableau.com/views/IndoHomeChurnAnalysisDashboard/Dashboard1-ExecutiveOverview?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)** - Executive insights and analytics

---

## 📊 Key Project Highlights

| Metric | Value | Impact |
|--------|-------|---------|
| **Model Performance** | F2-Score: 0.7253 | 83% churn detection rate |
| **Business Impact** | 55% cost reduction | Rp1.8B+ savings potential |
| **Technical Stack** | Python, Streamlit, Tableau | Production-ready deployment |
| **Data Coverage** | 7,043 customers | 21 feature analysis |

---

## 🚀 Features

- 🎯 **Individual churn prediction** with detailed risk assessment
- 📊 **Batch prediction** with CSV upload for multiple customers
- ⚖️ **Threshold tuning** with business trade-off simulation
- 📈 **Dashboard** with analytical insights and model interpretability
- 🔍 **Feature importance** analysis for actionable business insights
- 🧠 **Built using**: `scikit-learn`, `imbalanced-learn`, `streamlit`, `plotly`, and more

---

## 🧩 Model Details

| Component | Description |
|-----------|-------------|
| **Model** | Logistic Regression + ADASYN |
| **Evaluation Metric** | F2-Score (recall-focused) |
| **Optimal Threshold** | 0.43 (business-optimized) |
| **Interpretation** | Log Odds Coefficients |
| **Performance** | 83% recall, 48% precision |

---

## 🏗️ Repository Structure

```
📁 IndoHome-Customer-Churn-Analytics/
├── 📊 Telco Customer Churn.ipynb          # Complete analysis & modeling (377 cells)
├── 📱 app/
│   ├── app.py                              # Streamlit application
│   └── utils.py                           # Helper functions
├── 🎯 deployment/
│   ├── final_model_pipeline.pkl           # Trained model
│   ├── final_feature_list.json           # Feature configuration
│   └── threshold.json                     # Optimal threshold
├── 📈 Dataset_Telco Customer Churn.csv    # Original dataset
├── 📋 df_analisis.csv                     # Processed analysis data
├── 📋 df_model.csv                        # Model-ready data
├── 🖼️ Logo.png                           # IndoHome branding
├── 📋 requirements.txt                     # Python dependencies
├── ⚙️ runtime.txt                         # Python runtime version
└── 📝 README.md                           # This documentation
```

---

## 🚀 Quick Start

### **🌐 Access Live Application**
1. **Streamlit App**: [Click here to access](https://indohome-telco-churn-app-jaqqq4c38dcepxzzitrbzc.streamlit.app)
2. **Tableau Dashboard**: [View analytics](https://public.tableau.com/views/IndoHomeChurnAnalysisDashboard/Dashboard1-ExecutiveOverview)

### **💻 Run Locally**

1. **Clone Repository**
   ```bash
   git clone https://github.com/AdibahR/Indohome-telco-churn-app.git
   cd Indohome-telco-churn-app
   ```

2. **Setup Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Application**
   ```bash
   streamlit run app/app.py
   ```

5. **Explore Notebook**
   ```bash
   jupyter notebook "Telco Customer Churn.ipynb"
   ```

---

## 📊 Business Impact Analysis

### **💰 Financial Benefits**
Using this ML system, IndoHome can achieve:

- **55%+ reduction** in marketing costs
- **Rp1.8+ Billion savings** vs mass-promotion strategies  
- **83% churn detection rate** for proactive retention
- **Targeted interventions** for high-risk customer segments

### **📈 Strategic Advantages**
- **Data-driven decisions**: Replace intuition with insights
- **Proactive retention**: Identify at-risk customers before churn
- **Resource optimization**: Focus efforts on high-impact customers
- **Competitive edge**: Advanced analytics for market leadership

---

## 🧪 Model Performance & Methodology

### **📊 Model Evaluation**
| Metric | Value | Business Significance |
|--------|-------|---------------------|
| **F2-Score** | 0.7253 | Balanced performance with recall focus |
| **Recall (Churn)** | 0.83 | 83% of churning customers identified |
| **Precision (Churn)** | 0.48 | 48% prediction accuracy for churn cases |
| **Optimal Threshold** | 0.43 | Business-optimized decision boundary |

### **🔬 Technical Methodology**

#### **Data Science Pipeline**
1. **Exploratory Data Analysis**: Comprehensive feature analysis and customer behavior insights
2. **Feature Engineering**: Created TenureGroup, ServiceCount, and PriceVariation features
3. **Data Preprocessing**: Handled missing values, categorical encoding, feature scaling
4. **Model Selection**: Logistic Regression chosen for interpretability and performance
5. **Class Balancing**: ADASYN resampling to address class imbalance
6. **Hyperparameter Tuning**: Grid search with 5-fold cross-validation
7. **Threshold Optimization**: Business-oriented F2-score maximization

---

## 🛠️ Technologies & Tools

### **🐍 Core Technologies**
- **Python 3.10+**: Primary development language
- **Scikit-learn**: Machine learning and model development
- **Pandas & NumPy**: Data manipulation and analysis
- **Streamlit**: Web application framework
- **Tableau**: Business intelligence and visualization

### **📦 Key Libraries**
```python
streamlit==1.45.1          # Web application framework
scikit-learn==1.6.1        # Machine learning toolkit
pandas==2.3.0              # Data manipulation
numpy==2.2.6               # Numerical computing
imbalanced-learn==0.13.0   # Class balancing techniques
plotly==6.1.2              # Interactive visualizations
joblib==1.5.1              # Model serialization
```

---

## 📈 Business Recommendations

### **🎯 Immediate Actions**
1. **Deploy Model**: Integrate with CRM for automated churn scoring
2. **Segment Customers**: Implement risk-based customer categorization
3. **Targeted Campaigns**: Focus retention efforts on high-risk segments
4. **Monitor Performance**: Track model performance and business impact

### **📊 Strategic Initiatives**
1. **Data Integration**: Connect with customer service and billing systems
2. **Real-time Processing**: Implement streaming analytics for immediate insights
3. **A/B Testing**: Validate retention strategies with controlled experiments
4. **Model Evolution**: Continuous learning and model improvement

---

## 📞 Contact & Collaboration

### **👩‍💻 Project Author**
**[Rina Adibah](https://www.linkedin.com/in/rina-adibah/)**  
*Data Science Student - JCDS-2604-019*  
*[Purwadhika Digital Technology School](https://www.purwadhika.com/) - Batch 2604*

### **🤝 Collaboration Opportunities**
- Portfolio reviews and feedback
- Technical discussions and knowledge sharing
- Project collaboration and mentorship
- Industry insights and best practices

---

## 📄 License & Usage

This project is developed for **educational and portfolio purposes**. The dataset used is publicly available from Kaggle. For commercial usage or collaboration opportunities, please contact the project author.

### **⚖️ Important Notes**
- Dataset represents simulated telco data, not actual IndoHome customer data
- Model performance may vary with real-world implementation
- Regular retraining recommended for production deployment
- Business impact estimates based on modeling assumptions

---

## 🎉 Acknowledgments

Special thanks to:
- **[Purwadhika Digital Technology School](https://www.purwadhika.com/)** for comprehensive data science education
- **IBM** for providing the Telco Customer Churn dataset
- **Streamlit Community** for excellent documentation and support
- **Open Source Community** for powerful ML libraries and tools

---

*This project demonstrates end-to-end data science capabilities from analysis to deployment, showcasing technical skills and business acumen in solving real-world telecommunications challenges.*
