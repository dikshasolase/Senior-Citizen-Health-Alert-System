import streamlit as st


# Page Configuration

st.set_page_config(
    page_title="Emergency SOS",
    page_icon="🚨",
    layout="wide"
)


# Title

st.title("🚨 Emergency SOS")

st.divider()


# Information

st.warning(
"""
Emergency SOS provides quick access to emergency
medical support for senior citizens.
"""
)


# Emergency Buttons

st.subheader("📞 Emergency Contacts")


col1, col2 = st.columns(2)


with col1:

    st.markdown(
    """
    <a href="tel:108">

    <button style="
    background:red;
    color:white;
    padding:15px 25px;
    border:none;
    border-radius:10px;
    font-size:18px;
    cursor:pointer;
    ">

    🚑 Call Ambulance (108)

    </button>

    </a>
    """,
    unsafe_allow_html=True
    )



with col2:

    st.markdown(
    """
    <a href="tel:112">

    <button style="
    background:orange;
    color:white;
    padding:15px 25px;
    border:none;
    border-radius:10px;
    font-size:18px;
    cursor:pointer;
    ">

    📞 Emergency Helpline (112)

    </button>

    </a>
    """,
    unsafe_allow_html=True
    )



# Additional Contact

st.divider()

st.subheader("👨‍⚕️ Medical Support")


doctor_number = st.text_input(
    "Enter Doctor / Family Contact Number"
)


if doctor_number:

    st.markdown(
    f"""
    <a href="tel:{doctor_number}">

    <button style="
    background:green;
    color:white;
    padding:12px 20px;
    border:none;
    border-radius:8px;
    font-size:16px;
    ">

    📞 Call Contact

    </button>

    </a>
    """,
    unsafe_allow_html=True
    )



# System Flow

st.divider()

st.subheader("🔄 Emergency SOS Flow")


st.code(
"""
Patient
   |
   ↓
Emergency SOS Page
   |
   ↓
Select Emergency Contact
   |
   ↓
Make Call
   |
   ↓
Get Medical Assistance
"""
)