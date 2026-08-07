import streamlit as st
import bcrypt

from database import login_patient



# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Patient Login",
    page_icon="🔐"
)



# ---------------- TITLE ----------------

st.title("🔐 Patient Login")



# ---------------- LOGIN FORM ----------------

email = st.text_input(
    "📧 Email"
)


password = st.text_input(
    "🔒 Password",
    type="password"
)




# ---------------- LOGIN BUTTON ----------------

if st.button("Login"):


    user = login_patient(
        email,
        password
    )



    if user:



        # Password stored in database

        saved_password = user[5]



        if bcrypt.checkpw(
            password.encode(),
            saved_password.encode()
        ):



            # Session Data

            st.session_state.login = True

            st.session_state.patient_id = user[0]

            st.session_state.patient_name = user[1]

            st.session_state.patient_age = user[2]

            st.session_state.patient_phone = user[3]

            st.session_state.patient_email = user[4]



            st.success(
                "✅ Login Successful"
            )



            st.switch_page(
                "pages/3_Patient_Dashboard.py"
            )



        else:


            st.error(
                "❌ Wrong Password"
            )



    else:


        st.error(
            "❌ Email not registered"
        )