# Model Documentation

## 🧠 Model Overview

### Model Type
**Logistic Regression with ADASYN Resampling**

### Problem Type
Binary Classification - Customer Churn Prediction

### Business Objective
Identify customers at high risk of churning to enable proactive retention strategies.

## 📊 Model Performance

### Key Metrics
| Metric | Value | Business Impact |
|--------|-------|----------------|
| **F2-Score** | 0.7253 | Optimized for recall-focused business needs |
| **Recall (Churn)** | 0.83 | 83% of churning customers identified |
| **Precision (Churn)** | 0.48 | 48% accuracy in churn predictions |
| **Optimal Threshold** | 0.43 | Business-optimized decision boundary |

### Model Justification
- **Interpretability**: Logistic regression provides clear feature coefficients
- **Performance**: Achieves business-required recall rates
- **Efficiency**: Lightweight model suitable for production deployment
- **Stability**: Consistent performance across cross-validation folds

## 🔧 Technical Implementation

### Data Preprocessing Pipeline
1. **Missing Value Treatment**: Median imputation for numerical, mode for categorical
2. **Feature Engineering**: 
   - TenureGroup: Categorical tenure segments
   - ServiceCount: Total number of services subscribed
   - PriceVariation: Derived pricing features
3. **Encoding**: OneHotEncoder for categorical variables
4. **Scaling**: StandardScaler for numerical features
5. **Class Balancing**: ADASYN for minority class oversampling

### Model Pipeline
```python
Pipeline([
    ('preprocessor', ColumnTransformer([
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])),
    ('resampler', ADASYN(random_state=42)),
    ('classifier', LogisticRegression(random_state=42))
])
```

### Hyperparameters
- **C (Regularization)**: 1.0
- **Solver**: liblinear
- **Random State**: 42
- **Max Iterations**: 1000

## 📈 Feature Importance

### Top 10 Most Important Features
1. **Contract_Month-to-month**: Strong positive correlation with churn
2. **TotalCharges**: Higher charges increase churn probability
3. **InternetService_Fiber optic**: Fiber customers more likely to churn
4. **PaymentMethod_Electronic check**: Payment method impacts retention
5. **tenure**: Longer tenure reduces churn probability
6. **MonthlyCharges**: Monthly cost sensitivity
7. **PaperlessBilling_Yes**: Billing preference correlation
8. **OnlineSecurity_No**: Service usage patterns
9. **TechSupport_No**: Support service importance
10. **StreamingTV_Yes**: Entertainment service correlation

### Feature Coefficients Interpretation
- **Positive coefficients**: Increase churn probability
- **Negative coefficients**: Decrease churn probability
- **Magnitude**: Strength of feature impact

## 🎯 Business Rules & Thresholds

### Threshold Selection
- **Chosen Threshold**: 0.43
- **Optimization Metric**: F2-Score
- **Business Rationale**: Prioritizes recall over precision to minimize missed churners

### Risk Segmentation
| Probability Range | Risk Level | Recommended Action |
|------------------|------------|-------------------|
| 0.70 - 1.00 | **High Risk** | Immediate intervention |
| 0.43 - 0.69 | **Medium Risk** | Targeted retention campaigns |
| 0.00 - 0.42 | **Low Risk** | Standard customer care |

## 🔄 Model Validation

### Cross-Validation Results
- **5-Fold CV Mean F2-Score**: 0.718 ± 0.023
- **Stability**: Consistent performance across folds
- **Generalization**: No significant overfitting detected

### Holdout Test Performance
- **Test Set Size**: 20% of total data
- **Test F2-Score**: 0.7253
- **Validation**: Performance aligned with cross-validation results

## 🚀 Production Deployment

### Model Serialization
- **Format**: Pickle (joblib)
- **File**: `deployment/final_model_pipeline.pkl`
- **Size**: Optimized for web deployment

### Feature Configuration
- **File**: `deployment/final_feature_list.json`
- **Purpose**: Ensures consistent feature ordering
- **Format**: JSON array of feature names

### Threshold Configuration
- **File**: `deployment/threshold.json`
- **Purpose**: Configurable decision threshold
- **Format**: JSON object with threshold value

## 📋 Model Limitations & Assumptions

### Limitations
1. **Data Recency**: Model trained on historical data
2. **Feature Drift**: May require retraining with changing customer behavior
3. **External Factors**: Doesn't account for market conditions or competitor actions
4. **Class Imbalance**: Original dataset heavily skewed toward non-churn

### Assumptions
- Customer behavior patterns remain consistent
- Feature relationships are stable over time
- Missing data patterns are random
- Business context remains similar

## 🔧 Monitoring & Maintenance

### Performance Monitoring
- **Metric Tracking**: Monitor recall, precision, and F2-score
- **Data Drift Detection**: Track feature distribution changes
- **Prediction Distribution**: Monitor output probability distribution

### Retraining Triggers
- **Performance Degradation**: F2-score drops below 0.65
- **Data Drift**: Significant feature distribution changes
- **Business Changes**: New products/services or pricing models
- **Time-Based**: Quarterly retraining schedule

### Model Updates
- **Version Control**: Tag model versions with performance metrics
- **A/B Testing**: Compare new model versions against current production
- **Rollback Strategy**: Maintain previous model version for quick rollback

## 📊 Business Impact Simulation

### Cost-Benefit Analysis
- **Intervention Cost**: Estimated based on retention campaign costs
- **Customer Value**: Lifetime value calculation
- **ROI**: Positive return on investment at current performance levels

### Scenario Analysis
- **Conservative**: 60% intervention success rate
- **Optimistic**: 80% intervention success rate
- **Pessimistic**: 40% intervention success rate

All scenarios show positive business impact with current model performance.
