# 💳 Online Payments Fraud Detection with Machine Learning

This project uses machine learning techniques to detect fraudulent transactions in online payments. The dataset simulates real-world payment data, making it a valuable tool for developing fraud detection systems used by banks and financial services.

---

## 📌 Problem Statement

While online payments have brought great convenience, they’ve also increased the number of fraud cases. Detecting such fraud is essential to protect both users and businesses. In this project, we train a classification model to distinguish between fraudulent and legitimate transactions.

---

## 📊 Dataset Overview

Dataset Source: [Kaggle - Fraud Detection](https://www.kaggle.com/datasets)

Each row in the dataset represents an individual transaction with the following features:

| Column Name       | Description                                                       |
|-------------------|-------------------------------------------------------------------|
| `step`            | Unit of time (1 step = 1 hour)                                    |
| `type`            | Type of transaction (e.g., CASH_OUT, PAYMENT, TRANSFER)           |
| `amount`          | Transaction amount                                                 |
| `nameOrig`        | Customer initiating the transaction                                |
| `oldbalanceOrg`   | Origin account balance before transaction                          |
| `newbalanceOrig`  | Origin account balance after transaction                           |
| `nameDest`        | Recipient account                                                  |
| `oldbalanceDest`  | Recipient balance before transaction                               |
| `newbalanceDest`  | Recipient balance after transaction                                |
| `isFraud`         | **Target variable**: 1 if fraud, 0 otherwise                       |

---

## 🧠 Techniques Used

- Data Cleaning & Preprocessing
- Feature Engineering
- Imbalanced Data Handling (SMOTE)
- Model Training with:
  - Logistic Regression
  - Random Forest
  - XGBoost
- Model Evaluation (Accuracy, Precision, Recall, F1-Score, ROC AUC)

---

## 🏆 Results

| Model              | Accuracy  |
|--------------------|-----------|
| XGBoost            | 99.74%    |
| Logistic Regression| 89.60%    |
| Random Forest      | 86.61%    |

---

