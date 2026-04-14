import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor,RandomForestClassifier
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
import joblib
from sklearn.model_selection import train_test_split
import os
import joblib

# Create the directory if it doesn't exist
os.makedirs("models", exist_ok=True)



df = pd.read_csv("data/india_housing_prices.csv")

df = df.drop(columns=["Locality","Amenities","Year_Built"])

# Ordinal encoding (safe)
df["Furnished_Status"] = df["Furnished_Status"].map({
    "Unfurnished": 0,
    "Semi-Furnished": 1,
    "Furnished": 2
})

df["Public_Transport_Accessibility"] = df["Public_Transport_Accessibility"].map({
    "Low":0,
    "Medium":1,
    "High":2
})

df["Parking_Space"] = df["Parking_Space"].map({
    "No":0,
    "Yes":1
})

df["Security"] = df["Security"].map({
    "No":0,
    "Yes":1
})

df["Availability_Status"] = df["Availability_Status"].map({
    "Ready to Move":1,
    "Under Construction":0
})

df["Future_Price"] = df["Price_in_Lakhs"] * (1.08 ** 5)



X = df.drop(columns=["Future_Price"])
y_reg = df["Future_Price"]

X_train, X_test, y_train_reg, y_test_reg = train_test_split(X, y_reg, test_size=0.2, random_state=42)

city_median = X_train.groupby("City")["Price_per_SqFt"].median()

X_train["Investment_Score"] = (
    (X_train["Price_per_SqFt"] < X_train["City"].map(city_median)).astype(int) +
    (X_train["BHK"] >= 3).astype(int)
)

X_test["Investment_Score"] = (
    (X_test["Price_per_SqFt"] < X_test["City"].map(city_median)).astype(int) +
    (X_test["BHK"] >= 3).astype(int)
)

y_train_clf = (X_train["Investment_Score"] >= 2).astype(int)
y_test_clf = (X_test["Investment_Score"] >= 2).astype(int)


state_freq = X_train["State"].value_counts(normalize=True)
city_freq = X_train["City"].value_counts(normalize=True)

X_train["State_encoded"] = X_train["State"].map(state_freq)
X_test["State_encoded"] = X_test["State"].map(state_freq)

X_train["City_encoded"] = X_train["City"].map(city_freq)
X_test["City_encoded"] = X_test["City"].map(city_freq)

X_train.drop(columns=["State","City"], inplace=True)
X_test.drop(columns=["State","City"], inplace=True)







categorical_cols = ["Facing", "Owner_Type", "Property_Type"]
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(drop="first", handle_unknown="ignore"), categorical_cols)
    ],
    remainder="passthrough"
)


# Set experiment name
mlflow.set_experiment("Real Estate Investment")




# Start the parent run to group everything
with mlflow.start_run(run_name="RF_Both_Models"):
    
    # --- REGRESSOR SUB-RUN ---
    with mlflow.start_run(run_name="RF_Regressor_Task", nested=True):
        reg_pipeline = Pipeline([
            ("preprocessing", preprocessor),
            ("model", RandomForestRegressor(n_estimators=100, random_state=42))
        ])
        reg_pipeline.fit(X_train, y_train_reg)
        
        y_pred_reg = reg_pipeline.predict(X_test)
        mse = mean_squared_error(y_test_reg, y_pred_reg)

        # Logging inside the nested run
        mlflow.log_param("model_type", "RandomForestRegressor")
        mlflow.log_param("n_estimators", 100)
        mlflow.log_metric("mse", mse)
        mlflow.sklearn.log_model(reg_pipeline, artifact_path="regressor_model")

    # --- CLASSIFIER SUB-RUN ---
    with mlflow.start_run(run_name="RF_Classifier_Task", nested=True):
        clf_pipeline = Pipeline([
            ("preprocessing", preprocessor),
            ("model", RandomForestClassifier(n_estimators=100, random_state=42))
        ])
        clf_pipeline.fit(X_train, y_train_clf)

        y_pred_clf = clf_pipeline.predict(X_test)
        acc = accuracy_score(y_test_clf, y_pred_clf)

        # Logging inside the nested run
        mlflow.log_param("model_type", "RandomForestClassifier")
        mlflow.log_param("n_estimators", 100)
        mlflow.log_metric("accuracy", acc)
        mlflow.sklearn.log_model(clf_pipeline, artifact_path="classifier_model")


joblib.dump(reg_pipeline, "models/regressor.pkl")
joblib.dump(clf_pipeline, "models/classifier.pkl")