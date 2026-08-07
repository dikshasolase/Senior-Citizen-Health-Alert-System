import streamlit as st
import sqlite3
import pandas as pd


# ---------------- LOGIN CHECK ----------------

if "admin_login" not in st.session_state or not st.session_state.admin_login:

    st.warning("Please Login First")
    st.stop()



# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Admin Dashboard",
    page_icon="👨‍💼",
    layout="wide"
)



st.title("👨‍💼 Admin Dashboard")



# ---------------- DATABASE ----------------

conn = sqlite3.connect(
    "patients.db",
    check_same_thread=False
)

cursor = conn.cursor()



# ---------------- TOTAL PATIENTS ----------------

cursor.execute(
    "SELECT COUNT(*) FROM patients"
)

total_patients = cursor.fetchone()[0]



# ---------------- HEALTH RECORDS ----------------

try:

    cursor.execute(
        "SELECT COUNT(*) FROM health_records"
    )

    total_records = cursor.fetchone()[0]


except:

    total_records = 0





# ---------------- HIGH RISK ----------------

try:

    cursor.execute("""
    SELECT COUNT(*)
    FROM health_records
    WHERE health_status='⚠️ High Health Risk'
    """)


    high_risk = cursor.fetchone()[0]


except:

    high_risk = 0





# ---------------- METRICS ----------------

col1, col2, col3 = st.columns(3)



with col1:

    st.metric(
        "Total Patients",
        total_patients
    )



with col2:

    st.metric(
        "Health Records",
        total_records
    )



with col3:

    st.metric(
        "High Risk Cases",
        high_risk
    )



st.divider()




# ---------------- PATIENT LIST ----------------

st.subheader("📋 Registered Patients")



query = """

SELECT

id,

full_name,

age,

phone,

email,

registration_date

FROM patients

"""


df = pd.read_sql_query(
    query,
    conn
)




if len(df) > 0:


    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )


else:


    st.info(
        "No patients registered."
    )





# ---------------- VIEW PATIENT ----------------


st.subheader(
    "👁 View Patient Details"
)



if len(df) > 0:


    patient_ids = df["id"].tolist()



    selected_id = st.selectbox(
        "Select Patient ID",
        patient_ids
    )



    cursor.execute(
        """
        SELECT *
        FROM patients
        WHERE id=?
        """,
        (selected_id,)
    )


    patient = cursor.fetchone()



    if patient:



        st.success(
            "Patient Information"
        )



        col1, col2 = st.columns(2)



        with col1:


            st.write(
                f"**Name:** {patient[1]}"
            )


            st.write(
                f"**Age:** {patient[2]}"
            )


            st.write(
                f"**Phone:** {patient[3]}"
            )



        with col2:


            st.write(
                f"**Email:** {patient[4]}"
            )


            st.write(
                f"**Registration Date:** {patient[7]}"
            )




        st.divider()



        # ---------------- HEALTH RECORDS ----------------


        st.subheader(
            "❤️ Health Monitoring Records"
        )



        try:


            health_query = """

            SELECT

            date_time,

            heart_rate,

            blood_pressure,

            oxygen_level,

            temperature,

            blood_sugar,

            health_status


            FROM health_records


            WHERE patient_id=?


            ORDER BY date_time DESC


            """



            health_df = pd.read_sql_query(

                health_query,

                conn,

                params=(selected_id,)

            )




            if len(health_df) > 0:


                st.dataframe(

                    health_df,

                    use_container_width=True,

                    hide_index=True

                )


            else:


                st.info(
                    "No health records found for this patient."
                )



        except Exception as e:


            st.error(
                f"Health Record Error: {e}"
            )




else:

    st.info(
        "No patient available."
    )



# Close Database

conn.close()