import streamlit as st
import sqlite3
import bcrypt


# Page Configuration

st.set_page_config(
    page_title="Patient Registration",
    page_icon="📝",
    layout="centered"
)



# Database Connection

def create_table():

    conn = sqlite3.connect("patients.db")

    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        mobile TEXT,
        email TEXT UNIQUE,
        password TEXT

    )
    """)


    conn.commit()
    conn.close()



create_table()



# Insert Patient Data

def register_patient(name, age, mobile, email, password):


    conn = sqlite3.connect("patients.db")

    cursor = conn.cursor()


    try:

        cursor.execute(
        """
        INSERT INTO patients
        (name, age, mobile, email, password)

        VALUES(?,?,?,?,?)

        """,
        (
            name,
            age,
            mobile,
            email,
            password
        )
        )


        conn.commit()

        return True



    except:

        return False



    finally:

        conn.close()



# Page Design


st.title("📝 Patient Registration")


st.write(
"Create your account for Senior Health Alert System"
)



st.divider()



name = st.text_input(
"👤 Full Name"
)



age = st.number_input(
"🎂 Age",
min_value=1,
max_value=120
)



mobile = st.text_input(
"📱 Mobile Number"
)



email = st.text_input(
"📧 Email"
)



password = st.text_input(
"🔒 Create Password",
type="password"
)



if st.button("Register"):


    if name and email and password:


        # Encrypt Password

        encrypted_password = bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        ).decode()



        result = register_patient(

            name,
            age,
            mobile,
            email,
            encrypted_password

        )



        if result:

            st.success(
            "✅ Registration Successful"
            )


            st.info(
            "Please login using your email and password"
            )



        else:

            st.error(
            "❌ Email already registered"
            )


    else:

        st.warning(
        "Please fill all required fields"
        )



st.divider()



# Login Button

if st.button("👤 Already Registered? Login"):


    st.switch_page(
        "pages/2_Patient_Login.py"
    )