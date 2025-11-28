# ☕ Coffee Shop Daily Revenue Predictor

[![Project Status](https://img.shields.io/badge/Status-Complete-brightgreen)]()
[![Tech Stack](https://img.shields.io/badge/ML%20Stack-Streamlit%20|%20Scikit--learn%20|%20Pandas-orange)]()

## 💡 Project Overview
This project delivers a **Machine Learning solution** to accurately estimate the daily revenue of a coffee shop. By using a **Random Forest Regressor**, this application provides a data-driven tool for business owners to make informed decisions regarding operational planning, staffing, and marketing strategies.

### Key Components
1.  **`app.py`**: A fully interactive web application built using **Streamlit**, allowing users to adjust input parameters and view real-time revenue predictions.
2.  **`Model_Building.ipynb`**: A comprehensive Jupyter Notebook detailing the entire ML workflow, including **Exploratory Data Analysis (EDA)**, feature engineering, model training (with hyperparameter tuning), and evaluation.

## 🚀 Key Features & Functionality
* **Predictive Model:** Utilizes a **Random Forest Regressor**, known for handling complex, non-linear dependencies in regression tasks.
* **Feature Importance:** Predictions are based on critical input features like **Number of Customers Per Day**, **Average Order Value**, **Operating Hours**, **Marketing Spend**, and **Location Foot Traffic**.
* **Model Persistence:** The trained model is saved as **`model.pkl`**, enabling fast loading and instant predictions within the web application.

## 🛠️ Technical Stack
* **Language:** Python 3.x
* **ML Libraries:** Scikit-learn, NumPy, Pandas
* **Web Framework:** Streamlit
* **Data Serialization:** Pickle

## 📂 Repository Structure
Project files are organized for clarity: