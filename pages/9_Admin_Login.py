import streamlit as st

from database import admin_login


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Admin Login",
    page_icon="🔐",
    layout="centered"
)



st.title("🔐 Admin Login")

st.write(
    "Login to access the Admin Dashboard"
)



# ---------------- LOGIN FORM ----------------


username = st.text_input(
    "Username"
)


password = st.text_input(
    "Password",
    type="password"
)



if st.button("Login"):


    admin = admin_login(
        username,
        password
    )



    if admin:


        st.session_state.admin_login = True


        st.success(
            "Login Successful"
        )



        st.switch_page(
            "pages/10_Admin_Dashboard.py"
        )



    else:


        st.error(
            "Invalid Username or Password"
        )