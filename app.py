import streamlit as st


# Page Configuration
st.set_page_config(
    page_title="Senior Citizen Health Alert System",
    page_icon="🏥",
    layout="wide"
)

# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Navigation Bar
st.markdown("""
<div class="navbar">

<div class="logo">
🏥 Senior Citizen Health Alert System
</div>

""", unsafe_allow_html=True)
# ---------------- HERO SECTION ----------------

col1, col2 = st.columns([1,1])

with col1:

    st.markdown("""
    <h1 class="title">
    Senior Citizen<br>
    Health Alert System
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p class="subtitle">
    AI-Based Healthcare Monitoring and Emergency Support
    for Senior Citizens.
    </p>
    """, unsafe_allow_html=True)

with col2:

    st.image("images/banner.jpg", use_container_width=True)

st.write("")
st.write("")

# Authentication Buttons

col_btn1, col_btn2 ,col_btn3 = st.columns(3)

with col_btn1:

    if st.button("📝 Patient Registration"):

        st.switch_page(
            "pages/1_Patient_Registration.py"
        )


with col_btn2:

    if st.button("👤 Patient Login"):

        st.switch_page(
            "pages/2_Patient_Login.py"
        )
with col_btn3:
    
    if st.button("🔐 Admin Login"):
        
        st.switch_page(
            "pages/9_Admin_Login.py"
        )

# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">
© 2026 Senior Citizen Health Alert System | Developed using Streamlit
</div>
""", unsafe_allow_html=True)
