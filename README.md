# 🚀 Online Payment Fraud Detection

This project implements a machine learning pipeline to detect fraudulent online financial transactions. It includes data cleaning, preprocessing, model training, and evaluation using multiple classifiers.

---

## 📄 Dataset Description

This dataset contains simulated online payment transactions. It includes various features that help identify potentially fraudulent activity.

### 🔑 Key Features:

- `step`: Unit of time (in hours) since the first transaction in the dataset.
- `type`: Type of transaction (e.g., *CASH_OUT*, *TRANSFER*, etc.).
- `amount`: Amount of money transferred in the transaction.
- `nameOrig`: Customer who started the transaction.
- `oldbalanceOrg`: Initial balance of the sender before the transaction.
- `newbalanceOrg`: New balance of the sender after the transaction.
- `nameDest`: Recipient of the transaction.
- `oldbalanceDest`: Initial balance of the recipient before the transaction.
- `newbalanceDest`: New balance of the recipient after the transaction.
- `isFraud`: Target variable, 1 if the transaction is fraudulent, otherwise 0.

**Note:** The dataset is highly imbalanced with very few fraudulent transactions.


---

## 🧹 Data Preprocessing

- Removed rows with missing values in the `isFraud` column.
- Dropped identifier fields like `type`, `nameOrig`, and `nameDest` for modeling.
- Data split into training and test sets (70-30 split).

---

## 🛠️ Models Used

The following models were trained and evaluated using ROC-AUC:

- **Logistic Regression**
- **XGBoost Classifier**
- **Random Forest Classifier**

Each model was trained using the same training set and evaluated using ROC-AUC to measure performance on both training and testing datasets.

---


---

## 📈 Results

Model performance was evaluated using the ROC-AUC score:

- Logistic Regression: Good baseline performance.
- XGBoost: Strong performer, handles imbalance well.
- Random Forest: Fast and interpretable, but slightly lower accuracy.

---



