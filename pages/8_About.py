import streamlit as st


# Page Configuration

st.set_page_config(
    page_title="About",
    page_icon="🏥",
    layout="wide"
)


# Title

st.title("🏥 About Project")

st.divider()


# Project Information

st.header("📌 Senior Citizen Health Alert System")


st.write(
"""
The **Senior Citizen Health Alert System** is an AI-based healthcare
support system designed to help elderly people monitor their health
and receive quick medical assistance during emergency situations.

The system provides health monitoring, emergency support, location
tracking, and nearby hospital assistance to improve healthcare
accessibility for senior citizens.
"""
)



# Project Features

st.subheader("✨ Main Features")


st.markdown(
"""
- ❤️ Health Parameter Monitoring
- 🚨 Emergency SOS Support
- 📍 Live Location Tracking
- 🏥 Nearby Hospital Finder
- 🧭 Google Maps Direction Support
- 🤖 AI-Based Health Risk Prediction
- 📊 Digital Health Record Management
"""
)



# Technology

st.subheader("💻 Technologies Used")


st.markdown(
"""
- **Programming Language:** Python
- **Framework:** Streamlit
- **Database:** SQLite
- **AI/ML:** Machine Learning Algorithms
- **Location Service:** GPS & Google Maps
"""
)



st.divider()



# Location Information

st.header("📍 Project Location Example")


st.subheader("🏰 Shaniwar Wada, Pune")


st.write(
"""
Shaniwar Wada is a historical fortification located in the heart of
Pune, Maharashtra, India.

It was built in 1732 by the Peshwa rulers of the Maratha Empire and
is one of the most famous historical landmarks of Pune.

The location can be used as an example point for demonstrating the
GPS-based nearby hospital and emergency assistance features of this
project.
"""
)


# Map

st.subheader("🗺️ Location Map")


st.map(
{
"latitude":[18.5196],
"longitude":[73.8553]
}
)



# Project Workflow

st.divider()

st.header("🔄 System Workflow")


st.code(
"""
Patient Login
      |
      ↓
Health Monitoring
      |
      ↓
AI Health Analysis
      |
      ↓
Live Location Tracking
      |
      ↓
Nearby Hospital Search
      |
      ↓
Emergency Assistance
"""
)