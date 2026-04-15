## Real Estate Investment Analysis & Prediction

A machine learning project that predicts future property prices and evaluates whether a property is a good investment using structured housing data.

----

## Project Overview

This project focuses on:
	•	📈 Predicting future property prices (Regression)
	•	💡 Classifying whether a property is a good investment (Classification)
	•	🔍 Performing feature engineering & encoding
	•	📊 Tracking experiments using MLflow
	•	🌐 Deploying a local web app using Streamlit

----

## Features
	•	Dual-model system:
	•	Regression Model → Predicts future price
	•	Classification Model → Investment decision
	•	Advanced feature engineering:
	•	Frequency encoding (State, City)
	•	Custom Investment_Score
	•	Clean preprocessing pipeline using ColumnTransformer
	•	Experiment tracking with MLflow
	•	Interactive UI with Streamlit

----

## Machine Learning Pipeline

Data Processing
	•	Removed irrelevant columns (Locality, Amenities, Year_Built, ID)
	•	Applied:
	•	Ordinal encoding (Furnished, Transport, etc.)
	•	Frequency encoding (State, City)
	•	Feature engineering (Investment_Score)

Model Training
	•	Models used:
	•	RandomForestRegressor
	•	RandomForestClassifier
	•	Pipeline includes:
	•	ColumnTransformer (OneHotEncoding)
	•	Model

----

## 📊 MLflow Tracking
	•	Logs:
	•	Model parameters
	•	Metrics (MSE, Accuracy)
	•	Trained models
	•	Uses nested runs for:
	•	Regression
	•	Classification

----

## Run MLflow UI

mlflow ui

##🌐 Streamlit App (Local Deployment)

Run the app:

streamlit run pipeline.py

----

### Features:
	•	Input property details
	•	Predict:
	•	💰 Future Price
	•	✅ Investment Decision

----

## Project Structure

Real-Estate-Investment/
│
├── data/
│   ├── india_housing_prices.csv
│   ├── final_clean_dataset.csv
│
├── models/
│   ├── regressor.pkl
│   ├── classifier.pkl
│   ├── state_freq.pkl
│   ├── city_freq.pkl
│   ├── city_median.pkl
│
├── app.py                # Streamlit app
├── pipeline.py          # Training + MLflow
├── requirements.txt
└── README.md

----

## Installation

git clone <https://github.com/vijais0604-cloud/Real_Estate_Investment_Advisor>
cd Real-Estate-Investment

python -m venv .venv
source .venv/bin/activate  # macOS/Linux

pip install -r requirements.txt

----

## Run Training

python src/training.py

----

## Models

Models are saved using joblib:
	•	regressor.pkl
	•	classifier.pkl

Preprocessing artifacts:
	•	state_freq.pkl
	•	city_freq.pkl
	•	city_median.pkl

----

## Dataset

Synthetic/structured dataset of Indian housing properties
	•	Features include:
	•	Property details
	•	Location info
	•	Amenities & infrastructure
	•	Engineered features:
	•	Future_Price
	•	Investment_Score

## Author

Vijai S    