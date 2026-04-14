import streamlit as st
import pandas as pd
import joblib

# Load models
reg_model = joblib.load("models/regressor.pkl")
clf_model = joblib.load("models/classifier.pkl")

# Load encoders
state_freq = joblib.load("models/state_freq.pkl")
city_freq = joblib.load("models/city_freq.pkl")
city_median = joblib.load("models/city_median.pkl")

st.title("🏠 Real Estate Investment Predictor")

# ================= INPUTS =================

state = st.text_input("State")
city = st.text_input("City")

bhk = st.number_input("BHK", 1, 10)
size = st.number_input("Size in SqFt")
price = st.number_input("Current Price (Lakhs)")
price_per_sqft = st.number_input("Price per SqFt")

furnished = st.selectbox("Furnished Status", ["Unfurnished", "Semi-Furnished", "Furnished"])
floor_no = st.number_input("Floor No")
total_floors = st.number_input("Total Floors")
age = st.number_input("Age of Property")

schools = st.number_input("Nearby Schools")
hospitals = st.number_input("Nearby Hospitals")

transport = st.selectbox("Public Transport", ["Low", "Medium", "High"])
parking = st.selectbox("Parking", ["No", "Yes"])
security = st.selectbox("Security", ["No", "Yes"])

facing = st.selectbox("Facing", ["North", "South", "East", "West"])
owner = st.selectbox("Owner Type", ["Dealer", "Individual"])
availability = st.selectbox("Availability", ["Ready to Move", "Under Construction"])

property_type = st.selectbox("Property Type", ["Apartment", "Villa", "Plot", "House"])

# ================= ENCODING =================

furnished_map = {"Unfurnished":0,"Semi-Furnished":1,"Furnished":2}
transport_map = {"Low":0,"Medium":1,"High":2}
yes_no_map = {"No":0,"Yes":1}
availability_map = {"Ready to Move":1,"Under Construction":0}

# ================= CREATE DATAFRAME =================

input_data = pd.DataFrame({
    "Property_Type": property_type,
    "BHK": bhk,
    "Size_in_SqFt": size,
    "Price_in_Lakhs": price,
    "Price_per_SqFt": price_per_sqft,
    "Furnished_Status": furnished_map[furnished],
    "Floor_No": floor_no,
    "Total_Floors": total_floors,
    "Age_of_Property": age,
    "Nearby_Schools": schools,
    "Nearby_Hospitals": hospitals,
    "Public_Transport_Accessibility": transport_map[transport],
    "Parking_Space": yes_no_map[parking],
    "Security": yes_no_map[security],
    "Facing": facing,
    "Owner_Type": owner,
    "Availability_Status": availability_map[availability],
})

# ================= FEATURE ENGINEERING =================

# Frequency encoding
input_data["State_encoded"] = input_data.index.map(lambda x: state_freq.get(state, 0))
input_data["City_encoded"] = input_data.index.map(lambda x: city_freq.get(city, 0))

# Investment Score
input_data["Investment_Score"] = (
    (input_data["Price_per_SqFt"] < city_median.get(city, input_data["Price_per_SqFt"].iloc[0])) * 1 +
    (input_data["BHK"] >= 3) * 1
)

# ================= PREDICTION =================

if st.button("Predict"):

    future_price = reg_model.predict(input_data)[0]
    investment = clf_model.predict(input_data)[0]

    st.subheader(f"💰 Predicted Future Price: ₹{future_price:.2f} Lakhs")

    if investment == 1:
        st.success("✅ Good Investment")
    else:
        st.error("❌ Not a Good Investment")