# Deployment Guide

## 🚀 Streamlit Cloud Deployment

### Live Application
- **URL**: [IndoHome Churn Prediction App](https://indohome-telco-churn-app-jaqqq4c38dcepxzzitrbzc.streamlit.app)
- **Status**: Production Ready
- **Platform**: Streamlit Cloud
- **Runtime**: Python 3.10.x

### Deployment Configuration

#### Required Files
- `requirements.txt` - Python dependencies
- `runtime.txt` - Python version specification
- `app/app.py` - Main Streamlit application
- `deployment/` - Model files and configurations

#### Environment Variables
No environment variables required for current deployment.

### Local Development Setup

#### Prerequisites
- Python 3.10+
- Git
- Virtual environment (recommended)

#### Installation Steps
1. Clone repository:
   ```bash
   git clone https://github.com/AdibahR/Indohome-telco-churn-app.git
   cd Indohome-telco-churn-app
   ```

2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run application:
   ```bash
   streamlit run app/app.py
   ```

### Deployment Architecture

```
GitHub Repository
        ↓
Streamlit Cloud (Auto-deployment)
        ↓
Production Application
```

### Key Features
- ✅ Automatic deployment from main branch
- ✅ Zero-downtime deployments
- ✅ Built-in monitoring and logging
- ✅ HTTPS enabled by default
- ✅ Global CDN distribution

### Troubleshooting

#### Common Issues
1. **Dependencies not installing**: Check requirements.txt format
2. **App not loading**: Verify app/app.py path
3. **Model loading errors**: Ensure deployment/ folder is present

#### Monitoring
- Application logs available in Streamlit Cloud dashboard
- Performance metrics tracked automatically
- Error notifications via email (configured in Streamlit Cloud)

### Future Deployment Options

#### Alternative Platforms
- **Heroku**: For custom domain requirements
- **AWS EC2**: For enterprise deployment
- **Docker**: For containerized deployment
- **Google Cloud Run**: For serverless deployment

#### Scaling Considerations
- Current setup handles moderate traffic
- For high-traffic scenarios, consider load balancing
- Database integration may require additional infrastructure
