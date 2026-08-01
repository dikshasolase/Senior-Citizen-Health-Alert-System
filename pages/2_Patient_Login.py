import streamlit as st
import sqlite3
import bcrypt



# Page Configuration

st.set_page_config(
    page_title="Patient Login",
    page_icon="👤",
    layout="centered"
)



# Get User From Database

def get_patient(email):

    conn = sqlite3.connect("patients.db")

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT *
        FROM patients
        WHERE email=?
        """,
        (email,)
    )


    user = cursor.fetchone()


    conn.close()


    return user




# Password Verification

def verify_password(password, encrypted_password):

    return bcrypt.checkpw(
        password.encode(),
        encrypted_password.encode()
    )




# Create Session

if "login" not in st.session_state:

    st.session_state.login = False



# Page Design

st.title("👤 Patient Login")


st.write(
"Login to access Senior Citizen Health Alert System"
)


st.divider()



email = st.text_input(
"📧 Email Address"
)



password = st.text_input(
"🔒 Password",
type="password"
)




# Login Button

if st.button("Login"):


    if email and password:


        # Find patient

        patient = get_patient(email)



        if patient:


            # Check Password

            password_match = verify_password(

                password,

                patient[5]

            )



            if password_match:



                # Authorization Session

                st.session_state.login = True

                st.session_state.patient_id = patient[0]

                st.session_state.patient_name = patient[1]

                st.session_state.patient_email = patient[4]



                st.success(
                "✅ Login Successful"
                )



                st.write(
                f"Welcome {patient[1]}"
                )



                # Move to next module

                st.switch_page(
                    "pages/3_Patient_Dashboard.py"
                )



            else:

                st.error(
                "❌ Incorrect Password"
                )



        else:

            st.error(
            "❌ Email not registered"
            )



    else:

        st.warning(
        "Please enter email and password"
        )




st.divider()



# Registration Redirect

if st.button("📝 Create New Account"):


    st.switch_page(
        "pages/1_Patient_Registration.py"
    )