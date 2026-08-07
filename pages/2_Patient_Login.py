import streamlit as st
import bcrypt

from database import login_patient, reset_password


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Patient Login",
    page_icon="🔐",
    layout="centered"
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
st.divider()

st.subheader("🔑 Forgot Password")

reset_email = st.text_input(
    "Registered Email",
    key="reset_email"
)

new_password = st.text_input(
    "New Password",
    type="password",
    key="new_password"
)

confirm_password = st.text_input(
    "Confirm Password",
    type="password",
    key="confirm_password"
)

if st.button("Reset Password"):

    if not reset_email or not new_password or not confirm_password:

        st.warning("Please fill all fields.")

    elif new_password != confirm_password:

        st.error("Passwords do not match.")

    else:

        encrypted_password = bcrypt.hashpw(
            new_password.encode(),
            bcrypt.gensalt()
        ).decode()

        if reset_password(reset_email, encrypted_password):

            st.success("✅ Password updated successfully.")

        else:

            st.error("❌ Email not found.")