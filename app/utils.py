import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def get_feature_importance(model, feature_names):
    """
    Get global feature importance from logistic regression coefficients.
    Returns DataFrame with feature names, coefficients, and odds ratios.
    """
    try:
        # Get coefficients and convert to numeric
        coef = model.named_steps['model'].coef_[0].astype(np.float64)
        
        # Create DataFrame with feature importance metrics
        importance_df = pd.DataFrame({
            'Feature': feature_names,
            'Coefficient': coef,
            'Odds_Ratio': np.exp(coef)
        })
        
        # Calculate absolute values for sorting
        abs_coef = importance_df['Coefficient'].abs()
        
        # Sort by absolute coefficient value
        importance_df = importance_df.loc[abs_coef.sort_values(ascending=False).index]
        
        # Round numeric columns
        importance_df['Coefficient'] = importance_df['Coefficient'].round(4)
        importance_df['Odds_Ratio'] = importance_df['Odds_Ratio'].round(4)
        
        return importance_df
        
    except Exception as e:
        print(f"Error in get_feature_importance: {str(e)}")
        return pd.DataFrame(columns=['Feature', 'Coefficient', 'Odds_Ratio'])

def plot_feature_importance(importance_df, top_n=10):
    """
    Create horizontal barplot of feature importance.
    Shows top_n features sorted by absolute coefficient value.
    """
    try:
        # Get top N features
        plot_df = importance_df.head(top_n).copy()
        
        # Convert coefficient to numeric if not already
        plot_df['Coefficient'] = pd.to_numeric(plot_df['Coefficient'], errors='coerce')
        
        # Sort for plotting (actual values, not absolute)
        plot_df = plot_df.sort_values('Coefficient')
        
        # Create figure
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Create bars
        bars = ax.barh(plot_df['Feature'], plot_df['Coefficient'])
        
        # Color bars based on coefficient value
        for bar in bars:
            if bar.get_width() < 0:
                bar.set_color('#2166AC')  # Blue for negative
            else:
                bar.set_color('#B2182B')  # Red for positive
        
        # Add vertical line at x=0
        ax.axvline(x=0, color='black', linestyle='-', linewidth=0.5)
        
        # Customize plot
        ax.set_title('Top Feature Importance (Log-odds Coefficients)', pad=20)
        ax.set_xlabel('Coefficient Value')
        
        # Remove top and right spines
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        plt.tight_layout()
        return fig
        
    except Exception as e:
        print(f"Error in plot_feature_importance: {str(e)}")
        # Return empty figure if error occurs
        return plt.figure()

def get_feature_contributions(input_df, model, feature_names):
    """
    Calculate individual feature contributions for a single prediction.
    Returns DataFrame with feature contributions sorted by absolute impact.
    """
    try:
        # Get model coefficients and ensure numeric
        coef = model.named_steps['model'].coef_[0].astype(np.float64)
        
        # Transform input data
        X_transformed = model.named_steps['preprocessor'].transform(input_df)
        
        # Handle both sparse and dense matrices
        if hasattr(X_transformed, 'toarray'):
            X_transformed = X_transformed.toarray()
        
        # Ensure numeric type
        X_transformed = X_transformed.astype(np.float64)
        
        # Calculate contributions (input × coefficient)
        contributions = X_transformed[0] * coef
        
        # Create DataFrame
        contrib_df = pd.DataFrame({
            'Feature': pd.Series(feature_names),  # Ensure string type for features
            'Value': pd.Series(X_transformed[0], dtype=np.float64),
            'Coefficient': pd.Series(coef, dtype=np.float64),
            'Contribution': pd.Series(contributions, dtype=np.float64)
        })
        
        # Calculate absolute values for sorting
        contrib_df['Abs_Contribution'] = contrib_df['Contribution'].abs()
        
        # Sort by absolute contribution
        contrib_df = contrib_df.sort_values('Abs_Contribution', ascending=False)
        
        # Format numeric columns
        contrib_df['Value'] = contrib_df['Value'].round(4)
        contrib_df['Coefficient'] = contrib_df['Coefficient'].round(4)
        contrib_df['Contribution'] = contrib_df['Contribution'].round(4)
        
        # Select and reorder columns
        contrib_df = contrib_df[['Feature', 'Value', 'Coefficient', 'Contribution']]
        
        return contrib_df
        
    except Exception as e:
        print(f"Error in get_feature_contributions: {str(e)}")
        # Return empty DataFrame with correct columns if error occurs
        return pd.DataFrame(columns=['Feature', 'Value', 'Coefficient', 'Contribution']) 