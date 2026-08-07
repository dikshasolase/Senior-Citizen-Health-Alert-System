import streamlit as st
import bcrypt

from database import register_patient



st.set_page_config(
    page_title="Patient Registration",
    page_icon="📝"
)



st.title("📝 Patient Registration")

st.write(
"Create your account for Senior Citizen Health Alert System"
)



name = st.text_input("👤 Full Name")

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
    "🔒 Password",
    type="password"
)




if st.button("Register"):


    if name and email and password:


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
            "Now login using your email and password"
            )


        else:

            st.error(
            "❌ Email already registered"
            )



    else:

        st.warning(
        "Please fill all fields"
        )




if st.button("Already Registered? Login"):

    st.switch_page(
        "pages/2_Patient_Login.py"
    )