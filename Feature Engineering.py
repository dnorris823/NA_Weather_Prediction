# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np


# %%
labels = pd.read_csv('labels.csv', compression='zip')
features = pd.read_csv('features.csv', compression='zip')

labels.drop(['Unnamed: 0'], axis=1, inplace=True)
features.drop(['Unnamed: 0'], axis=1, inplace=True)


# %%
engineered_features = features


# %%
engineered_features.head()


# %%
engineered_features.shape


# %%
#engineered_features.drop(['Latitude'],axis=1, inplace=True)
#engineered_features.drop(['Longitude'],axis=1, inplace=True)


# %%
#engineered_features['humidity_minus_1'] = 0
#engineered_features['temperature_minus_1'] = 0
#engineered_features['pressure_minus_1'] = 0
#engineered_features['wind_dir_minus_1'] = 0
#engineered_features['wind_spd_minus_1'] = 0
#engineered_features['latitude_minus_1'] = 0
#engineered_features['longitude_minus_1'] = 0
#engineered_features['month_minus_1'] = 0
#engineered_features['day_minus_1'] = 0
#engineered_features['hour_minus_1'] = 0
#engineered_features['HxT'] = 0
#engineered_features['TxP'] = 0
#engineered_features['PxH'] = 0
engineered_features['day_avg_hum'] = 0
engineered_features['month_avg_hum'] = 0
engineered_features['year_avg_hum'] = 0
engineered_features['day_avg_temp'] = 0
engineered_features['month_avg_temp'] = 0
engineered_features['year_avg_temp'] = 0
engineered_features['day_avg_press'] = 0
engineered_features['month_avg_press'] = 0
engineered_features['year_avg_press'] = 0


# %%
#engineered_features['HxT'] = engineered_features['humidity'] * engineered_features['temperature']
#engineered_features['TxP'] = engineered_features['temperature'] * engineered_features['pressure']
#engineered_features['PxH'] = engineered_features['pressure'] * engineered_features['humidity']


# %%
engineered_features['day_avg_hum'] = engineered_features.iloc[:, 0].rolling(
    window=24).mean()
engineered_features['month_avg_hum'] = engineered_features.iloc[:, 0].rolling(
    window=730).mean()
engineered_features['year_avg_hum'] = engineered_features.iloc[:, 0].rolling(
    window=8765).mean()

engineered_features['day_avg_temp'] = engineered_features.iloc[:, 1].rolling(
    window=24).mean()
engineered_features['month_avg_temp'] = engineered_features.iloc[:, 1].rolling(
    window=730).mean()
engineered_features['year_avg_temp'] = engineered_features.iloc[:, 1].rolling(
    window=8765).mean()

engineered_features['day_avg_press'] = engineered_features.iloc[:, 2].rolling(
    window=24).mean()
engineered_features['month_avg_press'] = engineered_features.iloc[:, 2].rolling(
    window=730).mean()
engineered_features['year_avg_press'] = engineered_features.iloc[:, 2].rolling(
    window=8765).mean()


# %%
engineered_features['day_avg_hum'].fillna(
    engineered_features['day_avg_hum'].mean(), inplace=True)
engineered_features['month_avg_hum'].fillna(
    engineered_features['month_avg_hum'].mean(), inplace=True)
engineered_features['year_avg_hum'].fillna(
    engineered_features['year_avg_hum'].mean(), inplace=True)

engineered_features['day_avg_temp'].fillna(
    engineered_features['day_avg_temp'].mean(), inplace=True)
engineered_features['month_avg_temp'].fillna(
    engineered_features['month_avg_temp'].mean(), inplace=True)
engineered_features['year_avg_temp'].fillna(
    engineered_features['year_avg_temp'].mean(), inplace=True)

engineered_features['day_avg_press'].fillna(
    engineered_features['day_avg_press'].mean(), inplace=True)
engineered_features['month_avg_press'].fillna(
    engineered_features['month_avg_press'].mean(), inplace=True)
engineered_features['year_avg_press'].fillna(
    engineered_features['year_avg_press'].mean(), inplace=True)


# %%
engineered_features.head(50)


# %%
# engineered_features['HxT'] = engineered_features.Action.apply(
#            lambda x: (engineered_features['humidity'] * engineered_features['temperature']))

# engineered_features['TxP'] = engineered_features.Action.apply(
#            lambda y: (engineered_features['temperature'] * engineered_features['pressure']))

# engineered_features['PxH'] = engineered_features.Action.apply(
#            lambda z: (engineered_features['pressure'] * engineered_features['humidity']))


# %%
# for i in range(0, len(engineered_features)):
#engineered_features['HxT'].iloc[i] = engineered_features['humidity'].iloc[i] * engineered_features['temperature'].iloc[i]
#engineered_features['TxP'].iloc[i] = engineered_features['temperature'].iloc[i] * engineered_features['pressure'].iloc[i]
#engineered_features['PxH'].iloc[i] = engineered_features['pressure'].iloc[i] * engineered_features['humidity'].iloc[i]

# if(i ==0):
#engineered_features['humidity_minus_1'].iloc[i] = multi_day_features['humidity'].iloc[i]
#engineered_features['temperature_minus_1'].iloc[i] = multi_day_features['temperature'].iloc[i]
#engineered_features['pressure_minus_1'].iloc[i] = multi_day_features['pressure'].iloc[i]
#engineered_features['wind_dir_minus_1'].iloc[i] = multi_day_features['wind direction'].iloc[i]
#engineered_features['wind_spd_minus_1'].iloc[i] = multi_day_features['wind speed'].iloc[i]
#engineered_features['latitude_minus_1'].iloc[i] = multi_day_features['Latitude'].iloc[i]
#engineered_features['longitude_minus_1'].iloc[i] = multi_day_features['Longitude'].iloc[i]
#engineered_features['month_minus_1'].iloc[i] = multi_day_features['month'].iloc[i]
#engineered_features['day_minus_1'].iloc[i] = multi_day_features['day'].iloc[i]
#engineered_features['hour_minus_1'].iloc[i] = multi_day_features['hour'].iloc[i]
# else:
#engineered_features['humidity_minus_1'].iloc[i] = multi_day_features['humidity'].iloc[i - 1]
#engineered_features['temperature_minus_1'].iloc[i] = multi_day_features['temperature'].iloc[i - 1]
#engineered_features['pressure_minus_1'].iloc[i] = multi_day_features['pressure'].iloc[i - 1]
#engineered_features['wind_dir_minus_1'].iloc[i] = multi_day_features['wind direction'].iloc[i - 1]
#engineered_features['wind_spd_minus_1'].iloc[i] = multi_day_features['wind speed'].iloc[i - 1]
#engineered_features['latitude_minus_1'].iloc[i] = multi_day_features['Latitude'].iloc[i - 1]
#engineered_features['longitude_minus_1'].iloc[i] = multi_day_features['Longitude'].iloc[i - 1]
#engineered_features['month_minus_1'].iloc[i] = multi_day_features['month'].iloc[i - 1]
#engineered_features['day_minus_1'].iloc[i] = multi_day_features['day'].iloc[i - 1]
#engineered_features['hour_minus_1'].iloc[i] = multi_day_features['hour'].iloc[i - 1]


# %%
engineered_features.head(50)


# %%
labels.head(50)


# %%
engineered_features.to_csv('engineered_features.csv', compression='zip')


# %%
engineered_features.shape
