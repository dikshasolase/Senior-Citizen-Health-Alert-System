import streamlit as st


# Page Configuration

st.set_page_config(
    page_title="Patient Dashboard",
    page_icon="🏥",
    layout="wide"
)



# Authentication Check

if "login" not in st.session_state or st.session_state.login == False:

    st.warning(
        "Please Login First"
    )

    st.stop()



# Patient Information

patient_name = st.session_state.patient_name

patient_email = st.session_state.patient_email



# Header

st.title("🏥 Patient Dashboard")


st.success(
    f"Welcome {patient_name}"
)


st.write(
    "Senior Citizen Health Alert System"
)



st.divider()



# Patient Profile Section

st.subheader("👤 Patient Profile")


col1, col2 = st.columns(2)



with col1:

    st.write(
        "Name :",
        patient_name
    )


    st.write(
        "Email :",
        patient_email
    )



with col2:

    st.write(
        "Account Status : Active"
    )


    st.write(
        "Authorization : Verified"
    )



st.divider()



# Dashboard Cards

st.subheader("Services")



col1, col2, col3 = st.columns(3)



with col1:

    st.info(
    """
    ❤️

    Health Monitoring

    Check health parameters
    and AI predictions.
    """
    )



with col2:

    st.success(
    """
    📍

    Live Location

    Track patient location.
    """
    )



with col3:

    st.error(
    """
    🚨

    Emergency SOS

    Send emergency alert.
    """
    )



col4, col5 = st.columns(2)



with col4:

    st.warning(
    """
    🏥

    Nearby Hospital

    Find nearest healthcare center.
    """
    )



with col5:

    st.info(
    """
    👩‍⚕️

    Nurse Assistance

    Connect with healthcare support.
    """
    )



st.divider()



# Navigation Buttons


st.subheader(
"Quick Access"
)



if st.button("❤️ Health Monitoring"):

    st.switch_page(
        "pages/4_Health_Monitoring.py"
    )

if st.button("📋 Health History"):

    st.switch_page(
        "pages/8_Health_History.py"
    )

if st.button("📍 Live Location Tracking"):

    st.switch_page(
        "pages/6_Live_Tracking.py"
    )



if st.button("🚨 Emergency SOS"):

    st.switch_page(
        "pages/5_Emergency_SOS.py"
    )



st.divider()



# Logout

if st.button("🚪 Logout"):


    st.session_state.clear()


    st.switch_page(
        "app.py"
    )