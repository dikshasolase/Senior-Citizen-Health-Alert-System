from sklearn.ensemble import RandomForestClassifier
import numpy as np


# Sample training data

X_train = np.array([
    [80,98,36.5],
    [120,92,37.5],
    [140,85,39],
    [70,99,36],
    [130,88,38.5]
])


# 0 = Normal
# 1 = Risk

y_train = np.array([
    0,
    1,
    1,
    0,
    1
])


# Train model

model = RandomForestClassifier()

model.fit(
    X_train,
    y_train
)



def predict_health(
    heart_rate,
    oxygen,
    temperature
):


    data = np.array(
        [
            [
                heart_rate,
                oxygen,
                temperature
            ]
        ]
    )


    prediction = model.predict(data)


    if prediction[0] == 1:

        return "⚠️ High Health Risk"

    else:

        return "✅ Normal"