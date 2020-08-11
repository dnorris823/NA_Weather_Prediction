from sklearn.externals import joblib
import os
import pandas as pd

if os.path.exists('ML Backend/Saved Models/bin_model.pkl') & os.path.exists('ML Backend/Saved Models/multi_model.pkl'):
    # Load "bin_model.pkl"
    bin_model = joblib.load("ML Backend/Saved Models/bin_model.pkl")
    # Load "multi_model.pkl"
    multi_model = joblib.load("ML Backend/Saved Models/multi_model.pkl")
    print("models loaded")
else:
    print("models not loaded")

model_input = {
    "humidity": 48,
    "Temperature": 315.0,
    "pressure": 1013.0,
    "wind_direction": 0,
    "wind speed": 6.0,
    "Latitude": 47.606209,
    "Longitude": -122.332069,
    "month": 8,
    "day": 5,
    "hour": 15,
    "day_avg_hum": 57.333333,
    "month_avg_hum": 66.667123,
    "year_avg_hum": 76.430804,
    "day_avg_temp": 315.687917,
    "month_avg_temp": 312.456582,
    "year_avg_temp": 288.286528,
    "day_avg_press": 1013.916667,
    "month_avg_press": 1013.215068,
    "year_avg_press": 1020.478836
}

engineered_features = pd.read_csv(
    'ML Backend/Training Data/engineered_features.csv', compression='zip')

engineered_features.drop(['Unnamed: 0'], axis=1, inplace=True)

#bin_prediction = bin_model.predict(engineered_features.tail(500))
multi_prediction = multi_model.predict(engineered_features)

print(pd.Series(multi_prediction).value_counts())
