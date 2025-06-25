# 📊 Customer Churn Prediction using Azure ML

This project predicts customer churn using supervised machine learning and deploys the model using Microsoft Azure services. It simulates an end-to-end enterprise-level data science pipeline from data preparation to cloud deployment and inference via REST API.

## 🚀 Features

- Real-world inspired customer churn dataset
- Data preprocessing and feature engineering
- Random Forest classifier training with evaluation metrics
- Model deployment using Azure Machine Learning Studio
- REST API endpoint for real-time predictions
- Optional integration with Power BI for reporting

## 🧠 Technologies Used

- Python, Pandas, NumPy, Scikit-learn
- Azure Machine Learning Studio
- Azure Blob Storage, Azure App Service
- Jupyter Notebook
- REST API using `requests` module
- Power BI (optional)

## 📁 Project Structure

```
customer-churn-azureml/
├── data/
│   └── customer_churn.csv
├── scripts/
│   └── churn_predict.py
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_model_training.ipynb
│   └── 03_model_deployment.ipynb
├── app/
│   └── api_predict.py
├── azure/
│   └── pipeline_config.yml
└── README.md
```

## 🔧 Setup Instructions

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run `churn_predict.py` to train and evaluate the model
4. Use `api_predict.py` to test Azure ML web service endpoint
5. Modify and use Azure Studio or SDK to train & deploy from notebooks

## 📌 Use Case

This project is ideal for industries like telecom, SaaS, and financial services where customer retention is critical. By identifying high-risk churn profiles, businesses can proactively engage with users and reduce attrition.

## 📬 Contact

For queries or collaboration: [architnath.0924@gmail.com](mailto:architnath.0924@gmail.com)
