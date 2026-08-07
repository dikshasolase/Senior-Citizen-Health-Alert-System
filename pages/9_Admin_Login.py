import streamlit as st
import sqlite3

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Admin Login",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Admin Login")
st.write("Login to access the Admin Dashboard")

# ---------------- DATABASE ----------------

conn = sqlite3.connect("patients.db", check_same_thread=False)
cursor = conn.cursor()

# ---------------- LOGIN FORM ----------------

username = admin
password = admin123

if st.button("Login"):

    cursor.execute(
        "SELECT * FROM admin WHERE username=? AND password=?",
        (username, password)
    )

    admin = cursor.fetchone()

    if admin:

        st.session_state.admin_login = True
        st.success("Login Successful")

        st.switch_page("pages/10_Admin_Dashboard.py")

    else:

        st.error("Invalid Username or Password")
