import streamlit as st


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Patient Dashboard",
    page_icon="🏥",
    layout="wide"
)



# ---------------- AUTHENTICATION CHECK ----------------

if "login" not in st.session_state or not st.session_state.login:

    st.warning(
        "Please Login First"
    )

    st.stop()



# ---------------- SESSION DATA CHECK ----------------

if "patient_name" not in st.session_state or "patient_email" not in st.session_state:

    st.warning(
        "Patient information not found. Please login again."
    )

    st.stop()



# ---------------- PATIENT INFORMATION ----------------

patient_name = st.session_state.patient_name

patient_email = st.session_state.patient_email




# ---------------- HEADER ----------------

st.title(
    "🏥 Patient Dashboard"
)


st.success(
    f"Welcome {patient_name}"
)


st.write(
    "Senior Citizen Health Alert System"
)



st.divider()




# ---------------- PATIENT PROFILE ----------------

st.subheader(
    "👤 Patient Profile"
)


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




# ---------------- SERVICES ----------------

st.subheader(
    "Services"
)



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




# ---------------- QUICK ACCESS ----------------

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




# ---------------- LOGOUT ----------------

if st.button("🚪 Logout"):


    st.session_state.clear()


    st.switch_page(
        "app.py"
    )