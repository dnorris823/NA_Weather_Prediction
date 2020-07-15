# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing


# %%
city_attributes_df = pd.read_csv(
    "historical-hourly-weather-data/city_attributes.csv")
humidity_df = pd.read_csv("historical-hourly-weather-data/humidity.csv")
pressure_df = pd.read_csv("historical-hourly-weather-data/pressure.csv")
temperature_df = pd.read_csv("historical-hourly-weather-data/temperature.csv")
weather_description_df = pd.read_csv(
    "historical-hourly-weather-data/weather_description.csv")
wind_direction_df = pd.read_csv(
    "historical-hourly-weather-data/wind_direction.csv")
wind_speed_df = pd.read_csv("historical-hourly-weather-data/wind_speed.csv")


# %%
city_attributes_df = city_attributes_df.drop(['City', 'Country'], axis=1)
city_attributes_df.head()

humidity_df = pd.read_csv("historical-hourly-weather-data/humidity.csv")
melt_names = ['Vancouver', 'Portland', 'San Francisco', 'Seattle', 'Los Angeles', 'San Diego', 'Las Vegas', 'Phoenix',
              'Albuquerque', 'Denver', 'San Antonio', 'Dallas', 'Houston', 'Kansas City', 'Minneapolis', 'Saint Louis',
              'Chicago', 'Nashville', 'Indianapolis', 'Atlanta', 'Detroit', 'Jacksonville', 'Charlotte', 'Miami',
              'Pittsburgh', 'Toronto', 'Philadelphia', 'New York', 'Montreal', 'Boston', 'Beersheba', 'Tel Aviv District',
              'Eilat', 'Haifa', 'Nahariyya', 'Jerusalem']
# print(melt_names)
humidity_df = pd.melt(frame=humidity_df, id_vars=[
                      'datetime'], value_vars=melt_names, var_name='city', value_name='humidity')
humidity_df.head()


# %%
melt_names = ['Vancouver', 'Portland', 'San Francisco', 'Seattle', 'Los Angeles', 'San Diego', 'Las Vegas', 'Phoenix',
              'Albuquerque', 'Denver', 'San Antonio', 'Dallas', 'Houston', 'Kansas City', 'Minneapolis', 'Saint Louis',
              'Chicago', 'Nashville', 'Indianapolis', 'Atlanta', 'Detroit', 'Jacksonville', 'Charlotte', 'Miami',
              'Pittsburgh', 'Toronto', 'Philadelphia', 'New York', 'Montreal', 'Boston', 'Beersheba', 'Tel Aviv District',
              'Eilat', 'Haifa', 'Nahariyya', 'Jerusalem']
pressure_df = pd.melt(frame=pressure_df, id_vars=[
                      'datetime'], value_vars=melt_names, var_name='city', value_name='pressure')
temperature_df = pd.melt(frame=temperature_df, id_vars=[
                         'datetime'], value_vars=melt_names, var_name='city', value_name='temperature')
weather_description_df = pd.melt(frame=weather_description_df, id_vars=[
                                 'datetime'], value_vars=melt_names, var_name='city', value_name='weather description')
wind_direction_df = pd.melt(frame=wind_direction_df, id_vars=[
                            'datetime'], value_vars=melt_names, var_name='city', value_name='wind direction')
wind_speed_df = pd.melt(frame=wind_speed_df, id_vars=[
                        'datetime'], value_vars=melt_names, var_name='city', value_name='wind speed')


# %%
df = humidity_df
df['temperature'] = temperature_df['temperature']
df['pressure'] = pressure_df['pressure']
df['weather_description'] = weather_description_df['weather description']
df['wind direction'] = wind_direction_df['wind direction']
df['wind speed'] = wind_speed_df['wind speed']


# %%
df.loc[df['city'] == 'Vancouver', 'Latitude'] = 49.249660
df.loc[df['city'] == 'Vancouver', 'Longitude'] = -123.119339
df.loc[df['city'] == 'Portland', 'Latitude'] = 45.523449
df.loc[df['city'] == 'Portland', 'Longitude'] = -122.676208
df.loc[df['city'] == 'San Francisco', 'Latitude'] = 37.774929
df.loc[df['city'] == 'San Francisco', 'Longitude'] = -122.419418
df.loc[df['city'] == 'Seattle', 'Latitude'] = 47.606209
df.loc[df['city'] == 'Seattle', 'Longitude'] = -122.332069
df.loc[df['city'] == 'Los Angeles', 'Latitude'] = 34.052231
df.loc[df['city'] == 'Los Angeles', 'Longitude'] = -118.243683
df.loc[df['city'] == 'San Diego', 'Latitude'] = 32.715328
df.loc[df['city'] == 'San Diego', 'Longitude'] = -117.157257
df.loc[df['city'] == 'Las Vegas', 'Latitude'] = 36.174969
df.loc[df['city'] == 'Las Vegas', 'Longitude'] = -115.137222
df.loc[df['city'] == 'Phoenix', 'Latitude'] = 33.448380
df.loc[df['city'] == 'Phoenix', 'Longitude'] = -112.074043
df.loc[df['city'] == 'Albuquerque', 'Latitude'] = 35.084492
df.loc[df['city'] == 'Albuquerque', 'Longitude'] = -106.651138
df.loc[df['city'] == 'Denver', 'Latitude'] = 39.739151
df.loc[df['city'] == 'Denver', 'Longitude'] = -104.984703
df.loc[df['city'] == 'San Antonio', 'Latitude'] = 29.424120
df.loc[df['city'] == 'San Antonio', 'Longitude'] = -98.493629
df.loc[df['city'] == 'Dallas', 'Latitude'] = 32.783058
df.loc[df['city'] == 'Dallas', 'Longitude'] = -96.806671
df.loc[df['city'] == 'Houston', 'Latitude'] = 29.763281
df.loc[df['city'] == 'Houston', 'Longitude'] = - 95.363274
df.loc[df['city'] == 'Kansas City', 'Latitude'] = 39.099731
df.loc[df['city'] == 'Kansas City', 'Longitude'] = -94.578568
df.loc[df['city'] == 'Minneapolis', 'Latitude'] = 44.979969
df.loc[df['city'] == 'Minneapolis', 'Longitude'] = -93.263840
df.loc[df['city'] == 'Saint Louis', 'Latitude'] = 38.627270
df.loc[df['city'] == 'Saint Louis', 'Longitude'] = -90.197891
df.loc[df['city'] == 'Chicago', 'Latitude'] = 41.850029
df.loc[df['city'] == 'Chicago', 'Longitude'] = -87.650047
df.loc[df['city'] == 'Nashville', 'Latitude'] = 36.165890
df.loc[df['city'] == 'Nashville', 'Longitude'] = -86.784439
df.loc[df['city'] == 'Indianapolis', 'Latitude'] = 39.768379
df.loc[df['city'] == 'Indianapolis', 'Longitude'] = -86.158043
df.loc[df['city'] == 'Atlanta', 'Latitude'] = 33.749001
df.loc[df['city'] == 'Atlanta', 'Longitude'] = -84.387978
df.loc[df['city'] == 'Detroit', 'Latitude'] = 42.331429
df.loc[df['city'] == 'Detroit', 'Longitude'] = -83.045753
df.loc[df['city'] == 'Jacksonville', 'Latitude'] = 30.332180
df.loc[df['city'] == 'Jacksonville', 'Longitude'] = -81.655647
df.loc[df['city'] == 'Charlotte', 'Latitude'] = 35.227089
df.loc[df['city'] == 'Charlotte', 'Longitude'] = -80.843132
df.loc[df['city'] == 'Miami', 'Latitude'] = 25.774269
df.loc[df['city'] == 'Miami', 'Longitude'] = -80.193657
df.loc[df['city'] == 'Pittsburgh', 'Latitude'] = 40.440620
df.loc[df['city'] == 'Pittsburgh', 'Longitude'] = -79.995888
df.loc[df['city'] == 'Toronto', 'Latitude'] = 43.700111
df.loc[df['city'] == 'Toronto', 'Longitude'] = -79.416298
df.loc[df['city'] == 'Philadelphia', 'Latitude'] = 39.952339
df.loc[df['city'] == 'Philadelphia', 'Longitude'] = -75.163788
df.loc[df['city'] == 'New York', 'Latitude'] = 40.714272
df.loc[df['city'] == 'New York', 'Longitude'] = -74.005966
df.loc[df['city'] == 'Montreal', 'Latitude'] = 45.508839
df.loc[df['city'] == 'Montreal', 'Longitude'] = -73.587807
df.loc[df['city'] == 'Boston', 'Latitude'] = 42.358429
df.loc[df['city'] == 'Boston', 'Longitude'] = -71.059769
df.loc[df['city'] == 'Beersheba', 'Latitude'] = 31.251810
df.loc[df['city'] == 'Beersheba', 'Longitude'] = 34.791302
df.loc[df['city'] == 'Tel Aviv District', 'Latitude'] = 32.083328
df.loc[df['city'] == 'Tel Aviv District', 'Longitude'] = 34.799999
df.loc[df['city'] == 'Eilat', 'Latitude'] = 29.558050
df.loc[df['city'] == 'Eilat', 'Longitude'] = 34.948212
df.loc[df['city'] == 'Haifa', 'Latitude'] = 32.815559
df.loc[df['city'] == 'Haifa', 'Longitude'] = 34.989170
df.loc[df['city'] == 'Nahariyya', 'Latitude'] = 33.005859
df.loc[df['city'] == 'Nahariyya', 'Longitude'] = 35.094090
df.loc[df['city'] == 'Jerusalem', 'Latitude'] = 31.769039
df.loc[df['city'] == 'Jerusalem', 'Longitude'] = 35.216331


# %%
df.head()


# %%
df['datetime'] = pd.to_datetime(df['datetime'])


# %%
israel_rows_index = df[(df['city'] == 'Beersheba') | (df['city'] == 'Tel Aviv District') |
                       (df['city'] == 'Eilat') | (df['city'] == 'Haifa') |
                       (df['city'] == 'Nahariyya') | (df['city'] == 'Jerusalem')].index

df = df.drop(israel_rows_index, inplace=False)


# %%
df = df.dropna()


# %%
df = df.reset_index(drop=True)


# %%
df.drop(['city'], axis=1, inplace=True)

# use pd.concat to join the new columns with your original dataframe
df_labels = df['weather_description']

# now drop the original 'country' column (you don't need it anymore)
df.drop(['weather_description'], axis=1, inplace=True)


# %%
df_labels.value_counts()


# %%
df_labels.tail()


# %%
df.describe()


# %%
t = pd.DatetimeIndex(df['datetime'])
df['month'] = t.month
df['day'] = t.day
df['hour'] = t.hour


# %%
df.head()


# %%
df.drop(['datetime'], axis=1, inplace=True)


# %%
#df['month_sin'] = np.sin(2 * np.pi * df['month']/12.0)
#df['month_cos'] = np.cos(2 * np.pi * df['month']/12.0)

#df['day_sin'] = np.sin(2 * np.pi * df['hour']/365.0)
#df['day_cos'] = np.cos(2 * np.pi * df['hour']/365.0)

#df['hour_sin'] = np.sin(2 * np.pi * df['hour']/23.0)
#df['hour_cos'] = np.cos(2 * np.pi * df['hour']/23.0)

#df.drop(['month'],axis=1, inplace=True)
#df.drop(['day'],axis=1, inplace=True)
#df.drop(['hour'],axis=1, inplace=True)


# %%
df.head(30)


# %%
#df['humidity'] = preprocessing.normalize(df['humidity'])
#df['temperature'] = preprocessing.normalize(df['temperature'])
#df['pressure'] = preprocessing.normalize(df['pressure'])
#df['wind direction'] = preprocessing.normalize(df['wind direction'])
#df['wind speed'] = preprocessing.normalize(df['wind speed'])
#df['latitude'] = preprocessing.normalize(df['latitude'])
#df['longitude'] = preprocessing.normalize(df['longitude'])
# print(df.shape)
#df = preprocessing.normalize(df)

#df = pd.DataFrame(df)
# print(df.shape)


# %%
df.to_csv('features.csv', compression='zip')
df_labels.to_csv('labels.csv', compression='zip')


# %%
