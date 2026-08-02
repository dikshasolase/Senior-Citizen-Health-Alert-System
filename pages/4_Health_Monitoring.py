import streamlit as st
import sqlite3
from datetime import datetime

from model.health_prediction import predict_health



# Page Configuration

st.set_page_config(
    page_title="Health Monitoring",
    page_icon="❤️",
    layout="wide"
)



# Authentication Check

if "login" not in st.session_state or st.session_state.login == False:

    st.warning("Please Login First")

    st.stop()



# Create Health Database Table

def create_health_table():

    conn = sqlite3.connect("patients.db")

    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS health_records(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        patient_id INTEGER,

        patient_name TEXT,

        heart_rate INTEGER,

        blood_pressure TEXT,

        temperature REAL,

        oxygen_level INTEGER,

        health_status TEXT,

        date_time TEXT

    )
    """)


    conn.commit()

    conn.close()



create_health_table()



# Save Health Data Function

def save_health_data(
    patient_id,
    patient_name,
    heart_rate,
    blood_pressure,
    temperature,
    oxygen_level,
    status
):


    conn = sqlite3.connect("patients.db")

    cursor = conn.cursor()


    cursor.execute(
    """
    INSERT INTO health_records(

        patient_id,
        patient_name,
        heart_rate,
        blood_pressure,
        temperature,
        oxygen_level,
        health_status,
        date_time

    )

    VALUES(?,?,?,?,?,?,?,?)

    """,

    (
        patient_id,
        patient_name,
        heart_rate,
        blood_pressure,
        temperature,
        oxygen_level,
        status,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    )


    conn.commit()

    conn.close()



# ---------------- Page UI ----------------


st.title("❤️ Health Monitoring")


st.success(
    f"Patient: {st.session_state.patient_name}"
)


st.divider()



col1, col2 = st.columns(2)



with col1:

    age = st.number_input(
        "👴 Age",
        min_value=50,
        max_value=120,
        value=65
    )


    heart_rate = st.number_input(
        "❤️ Heart Rate (BPM)",
        min_value=30,
        max_value=200,
        value=80
    )


    temperature = st.number_input(
        "🌡 Temperature (°C)",
        min_value=30.0,
        max_value=45.0,
        value=36.5
    )



with col2:


    blood_pressure = st.text_input(
        "🩸 Blood Pressure",
        placeholder="120/80"
    )


    oxygen_level = st.number_input(
        "🫁 Oxygen Level SpO2 (%)",
        min_value=50,
        max_value=100,
        value=98
    )
    
    
    blood_sugar = st.number_input(
    "🩸 Blood Sugar Level",
    min_value=50,
    max_value=400,
    value=110
)


st.divider()



# ---------------- ML Prediction ----------------


if st.button(
    "Save Health Record"
):


    # Calling Machine Learning Model

    status = predict_health(

        age,

        heart_rate,

        int(blood_pressure.split("/")[0]),

        oxygen_level,

        temperature,

        blood_sugar

    )



    save_health_data(

        st.session_state.patient_id,

        st.session_state.patient_name,

        heart_rate,

        blood_pressure,

        temperature,

        oxygen_level,

        status

    )



    st.success(
        "✅ Health Data Saved Successfully"
    )



    if "High Risk" in status:


        st.error(
            f"🤖 AI Prediction: {status}"
        )


    else:


        st.success(
            f"🤖 AI Prediction: {status}"
        )