# 🏥 Senior Citizen Health Alert System

An AI-powered healthcare monitoring and emergency support system developed using **Python**, **Streamlit**, **SQLite**, and **Machine Learning**. The application helps senior citizens monitor their health, maintain medical records, predict health conditions using AI, and access emergency support through a simple and user-friendly interface.

---

# 🌍 Deployment

The application is deployed using **Streamlit Community Cloud**.

**Live URL**

https://senior-citizen-health-alert-system-msqkyfwzdvjp3ahd92mdhr.streamlit.app/

---

# 📖 Project Overview

The **Senior Citizen Health Alert System** is designed to improve healthcare services for elderly people by providing an intelligent platform for monitoring health conditions, storing medical records, and offering emergency assistance.

The system also includes a dedicated **Admin Panel** that allows administrators to securely log in, view all registered patients, search patient records, and access each patient's health monitoring history for effective healthcare management.

---

# ✨ Key Features
- 👨‍💼 Admin Login
- 📋 Admin Dashboard
- 🔍 Patient Search & Health Record Management
- 🏠 Home Page
- 👤 Patient Registration
- 🔐 Secure Patient Login
- 📊 Patient Dashboard
- ❤️ Health Monitoring
- 🤖 AI-Based Health Prediction
- 📜 Health History
- 🚨 Emergency SOS
- 📍 Live Location Tracking
- 🏥 Nearby Hospital Search
- 💾 SQLite Database Management
- 📂 Health Dataset Integration
- 🧠 Trained Machine Learning Model (.pkl) Integration

---

# 🤖 Machine Learning

The application uses a Machine Learning model to analyze patient health data and predict health status.

# 📂 Dataset

The system uses a health monitoring dataset containing patient health parameters.

Dataset File:
dataset/
└── health_dataset.csv

The dataset includes:

- Age
- Heart Rate
- Blood Pressure
- Oxygen Saturation (SpO₂)
- Body Temperature
- Blood Sugar Level
- Health Status Label

### Algorithm Used

- Random Forest Classifier

### Model Training

- Health dataset is used for training the machine learning model.
- The trained model is saved as `health_model.pkl`.
- The prediction model is loaded into the Streamlit application for real-time health status prediction.

### Model Files

model/
│
├── train_model.py # Model training script
└── health_model.pkl # Trained ML model

### Input Parameters

- Age
- Heart Rate
- Blood Pressure
- Oxygen Saturation (SpO₂)
- Body Temperature
- Blood Sugar Level

### Prediction Result

- ✅ Healthy
- ⚠️ At Risk

---
# 👨‍💼 Admin Module

The application provides a secure Admin Panel for managing patient information and monitoring healthcare records.

### Admin Features

- 🔐 Secure Admin Login
- 👥 View All Registered Patients
- 🔍 Search Patients by Name, Mobile Number, or Email
- 📋 View Patient Details
- ❤️ Access Complete Health Monitoring History
- 📊 Dashboard Showing Patient Statistics
- 🚪 Secure Admin Logout

# 🛠️ Technology Stack

## Frontend
- Streamlit
- HTML
- CSS

## Backend
- Python

## Database
- SQLite

## Machine Learning
- Scikit-learn
- Pandas
- NumPy

## Development Tools
- Visual Studio Code
- Git
- GitHub
- Streamlit Community Cloud

---


# 🚀 Installation

## Clone the Repository

```bash
git clone https://github.com/dikshasolase/Senior-Citizen-Health-Alert-System.git
```

## Navigate to the Project Folder

```bash
cd Senior-Citizen-Health-Alert-System
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

# 📊 Project Workflow

```text
Start
   │
   ▼
Home Page
   │
   ├────────► Patient Registration
   │              │
   │              ▼
   │         Patient Login
   │              │
   │              ▼
   │      Patient Dashboard
   │              │
   │              ├────────► Health Monitoring
   │              │              │
   │              │              ▼
   │              │       AI Health Prediction
   │              │              │
   │              │              ▼
   │              │      Save Health Records
   │              │
   │              ├────────► Health History
   │              │
   │              ├────────► Emergency SOS
   │              │
   │              ├────────► Live Location Tracking
   │              │
   │              └────────► Nearby Hospital Search
   │
   └────────► Admin Login
                  │
                  ▼
           Admin Dashboard
                  │
                  ├────────► View Registered Patients
                  │
                  ├────────► Search Patient
                  │
                  ├────────► View Patient Details
                  │
                  ├────────► View Health Records
                  │
                  └────────► Logout
```

---

# 💡 Advantages

- Easy-to-use interface for senior citizens.
- Secure patient authentication.
- AI-based health prediction.
- Digital health record management.
- Quick emergency assistance.
- Live location support.
- Nearby hospital search.
- Lightweight and fast application.

---

# 👩‍💻 Developer

**Diksha Solase**

---


# ⭐ If you like this project

If you found this project helpful, please consider giving it a **⭐ Star** on GitHub.

Thank you for visiting this repository!
