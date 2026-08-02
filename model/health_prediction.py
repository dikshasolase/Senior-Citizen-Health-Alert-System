import joblib
import numpy as np
import os


# Load Model

path = os.path.join(
    os.path.dirname(__file__),
    "health_model.pkl"
)


model = joblib.load(path)



def predict_health(
    age,
    heart_rate,
    blood_pressure,
    oxygen_level,
    temperature,
    blood_sugar
):


    data = np.array(
        [[
            age,
            heart_rate,
            blood_pressure,
            oxygen_level,
            temperature,
            blood_sugar
        ]]
    )


    prediction = model.predict(
        data
    )


    if prediction[0] == 1:

        return "⚠️ High Health Risk"

    else:

        return "✅ Normal"