import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor,RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, mean_squared_error, r2_score

# Set experiment name
mlflow.set_experiment("Real Estate Investment")

# Load data
df = pd.read_csv("data/india_housing_prices.csv")

# Example target creation (you can refine later)
df["Good_Investment"] = (df["Price_per_SqFt"] < df["Price_per_SqFt"].median()).astype(int)
df["Future_Price"] = df["Price_in_Lakhs"] * (1.08 ** 5)
