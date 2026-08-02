import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


# Load Dataset

data = pd.read_csv(
    "dataset/health_dataset.csv"
)


# Convert target

data["health_status"] = data["health_status"].map(
    {
        "Normal":0,
        "Risk":1
    }
)


# Features

X = data.drop(
    "health_status",
    axis=1
)


# Target

y = data["health_status"]



# Train Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)



# Create Model

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Train

model.fit(
    X_train,
    y_train
)



# Prediction

y_pred = model.predict(
    X_test
)



# Accuracy

accuracy = accuracy_score(
    y_test,
    y_pred
)


print(
    "Accuracy:",
    accuracy*100
)



print(
    classification_report(
        y_test,
        y_pred
    )
)



print(
    confusion_matrix(
        y_test,
        y_pred
    )
)



# Save Model

joblib.dump(
    model,
    "model/health_model.pkl"
)


print(
    "Model Saved Successfully"
)