import streamlit as st
import sqlite3
import pandas as pd



# Page Configuration

st.set_page_config(
    page_title="Health History",
    page_icon="📋",
    layout="wide"
)



# Authentication Check

if "login" not in st.session_state or st.session_state.login == False:

    st.warning("Please Login First")

    st.stop()



# Database Function

def get_health_records(patient_id):

    conn = sqlite3.connect("patients.db")


    query = """
    SELECT 
    heart_rate,
    blood_pressure,
    temperature,
    oxygen_level,
    health_status,
    date_time

    FROM health_records

    WHERE patient_id=?

    """


    data = pd.read_sql_query(
        query,
        conn,
        params=(patient_id,)
    )


    conn.close()


    return data




# Page Title

st.title("📋 Health History")


st.success(
f"Patient: {st.session_state.patient_name}"
)



st.divider()



# Fetch Data

records = get_health_records(
    st.session_state.patient_id
)



if not records.empty:


    st.subheader(
    "Your Health Records"
    )


    st.dataframe(
        records,
        use_container_width=True
    )



else:


    st.info(
    "No health records found"
    )