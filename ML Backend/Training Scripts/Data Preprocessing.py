import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing

# Read in all of the different csv files into Pandas DataFrames
city_attributes_df = pd.read_csv(
    "ML Backend/historical-hourly-weather-data/city_attributes.csv")
humidity_df = pd.read_csv(
    "ML Backend/historical-hourly-weather-data/humidity.csv")
pressure_df = pd.read_csv(
    "ML Backend/historical-hourly-weather-data/pressure.csv")
temperature_df = pd.read_csv(
    "ML Backend/historical-hourly-weather-data/temperature.csv")
weather_description_df = pd.read_csv(
    "ML Backend/historical-hourly-weather-data/weather_description.csv")
wind_direction_df = pd.read_csv(
    "ML Backend/historical-hourly-weather-data/wind_direction.csv")
wind_speed_df = pd.read_csv(
    "ML Backend/historical-hourly-weather-data/wind_speed.csv")

city_attributes_df = city_attributes_df.drop(['City', 'Country'], axis=1)

# Melt all of the Dataframes so that there is a value column and a location column
melt_names = ['Vancouver', 'Portland', 'San Francisco', 'Seattle', 'Los Angeles', 'San Diego', 'Las Vegas', 'Phoenix',
              'Albuquerque', 'Denver', 'San Antonio', 'Dallas', 'Houston', 'Kansas City', 'Minneapolis', 'Saint Louis',
              'Chicago', 'Nashville', 'Indianapolis', 'Atlanta', 'Detroit', 'Jacksonville', 'Charlotte', 'Miami',
              'Pittsburgh', 'Toronto', 'Philadelphia', 'New York', 'Montreal', 'Boston', 'Beersheba', 'Tel Aviv District',
              'Eilat', 'Haifa', 'Nahariyya', 'Jerusalem']

humidity_df = pd.melt(frame=humidity_df, id_vars=[
                      'datetime'], value_vars=melt_names, var_name='city', value_name='humidity')

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

# Combine all of the DataFrames into one with different columns for each type of value
df = humidity_df
df['temperature'] = temperature_df['temperature']
df['pressure'] = pressure_df['pressure']
df['weather_description'] = weather_description_df['weather description']
df['wind direction'] = wind_direction_df['wind direction']
df['wind speed'] = wind_speed_df['wind speed']

# Convert the city column to a longitude and latitude column
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

# Make sure datetime column is stored as Pandas datetime object
df['datetime'] = pd.to_datetime(df['datetime'])

# Drop all non-NA location rows so they do not skew the model
israel_rows_index = df[(df['city'] == 'Beersheba') | (df['city'] == 'Tel Aviv District') |
                       (df['city'] == 'Eilat') | (df['city'] == 'Haifa') |
                       (df['city'] == 'Nahariyya') | (df['city'] == 'Jerusalem')].index

df = df.drop(israel_rows_index, inplace=False)

df = df.dropna()

df = df.reset_index(drop=True)

# drop the city column as it is no longer needed
df.drop(['city'], axis=1, inplace=True)

# Create a Dataframe to hold all of the features that we are labeling on
df_labels = df['weather_description']

# Drop the weather_description feature from the originial DataFrame since it is now store in the labels Dataframe
df.drop(['weather_description'], axis=1, inplace=True)

# Create new columns for the month day and hour, drop the datetime column
df['month'] = pd.DatetimeIndex(df['datetime']).month
df['day'] = pd.DatetimeIndex(df['datetime']).day
df['hour'] = pd.DatetimeIndex(df['datetime']).hour

df.drop(['datetime'], axis=1, inplace=True)

# Save the base feature and label DataFrames to csv files
df.to_csv('ML Backend/Training Data/features.csv', compression='zip')
df_labels.to_csv('ML Backend/Training Data/labels.csv', compression='zip')

# Give slightly better names to DataFrames so things are less confusing
features = pd.DataFrame(df)
labels = pd.DataFrame(df_labels)
labels_bin = pd.DataFrame(df_labels)
print("initial")

# Create new binary labels DataFrames base on labels DataFrame values "sky is clear" or someting else
labels_bin.loc[labels_bin['weather_description'] !=
               'sky is clear', 'is_sky_clear'] = False
labels_bin.loc[labels_bin['weather_description'] ==
               'sky is clear', 'is_sky_clear'] = True

labels_bin.drop(['weather_description'], axis=1, inplace=True)

# Save binary labels DataFrame to a csv file
labels_bin = pd.DataFrame(labels_bin)
labels_bin.to_csv('ML Backend/Training Data/labels_bin.csv', compression='zip')

print("binary")

# Create engineered_features DataFrame from features DataFrame
engineered_features = features

# create new columns for daily, monthly, and yearly rolling averages of humidity, temperature, and pressure
engineered_features['day_avg_hum'] = 0
engineered_features['month_avg_hum'] = 0
engineered_features['year_avg_hum'] = 0
engineered_features['day_avg_temp'] = 0
engineered_features['month_avg_temp'] = 0
engineered_features['year_avg_temp'] = 0
engineered_features['day_avg_press'] = 0
engineered_features['month_avg_press'] = 0
engineered_features['year_avg_press'] = 0

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

# Save to csv file
engineered_features.to_csv(
    'ML Backend/Training Data/engineered_features.csv', compression='zip')

print("engineered")

engineered_features['weather_description'] = labels

# Condense down the number of possible labels to make classification a bit easier
engineered_features.loc[engineered_features['weather_description'].str.contains(
    'clouds'), 'weather_description'] = 'Cloudy'
engineered_features.loc[engineered_features['weather_description'].str.contains(
    'rain'), 'weather_description'] = 'Rainy'
engineered_features.loc[engineered_features['weather_description'].str.contains(
    'drizzle'), 'weather_description'] = 'Rainy'
engineered_features.loc[engineered_features['weather_description'].str.contains(
    'mist'), 'weather_description'] = 'Rainy'
engineered_features.loc[engineered_features['weather_description'].str.contains(
    'fog'), 'weather_description'] = 'Fog/Haze'
engineered_features.loc[engineered_features['weather_description'].str.contains(
    'haze'), 'weather_description'] = 'Fog/Haze'
engineered_features.loc[engineered_features['weather_description'].str.contains(
    'dust'), 'weather_description'] = 'Poor Visibility'
engineered_features.loc[engineered_features['weather_description'].str.contains(
    'sand'), 'weather_description'] = 'Poor Visibility'
engineered_features.loc[engineered_features['weather_description'].str.contains(
    'smoke'), 'weather_description'] = 'Poor Visibility'
engineered_features.loc[engineered_features['weather_description'].str.contains(
    'snow'), 'weather_description'] = 'Snow'
engineered_features.loc[engineered_features['weather_description'].str.contains(
    'sleet'), 'weather_description'] = 'Snow'
engineered_features.loc[engineered_features['weather_description'].str.contains(
    'storm'), 'weather_description'] = 'Stormy'
engineered_features.loc[engineered_features['weather_description'].str.contains(
    'thunderstorm'), 'weather_description'] = 'Stormy'
engineered_features.loc[engineered_features['weather_description'].str.contains(
    'squall'), 'weather_description'] = 'Stormy'
engineered_features.loc[engineered_features['weather_description'].str.contains(
    'tornado'), 'weather_description'] = 'Weather Event'
engineered_features.loc[engineered_features['weather_description'].str.contains(
    'volcanic ash'), 'weather_description'] = 'Weather Event'
engineered_features.loc[engineered_features['weather_description'].str.contains(
    'sky is clear'), 'weather_description'] = 'Clear Weather'

# Create a features DataFrame that does not contain any records that contain "Clear Weather"
features_gen_no_clear = []
features_gen_no_clear = engineered_features[~engineered_features['weather_description'].str.contains(
    "Clear Weather")]

labels_gen = []
labels_gen = engineered_features['weather_description']
engineered_features.drop(['weather_description'], axis=1, inplace=True)
features_gen = []
features_gen = engineered_features
labels_gen_no_clear = []
labels_gen_no_clear = features_gen_no_clear['weather_description']
features_gen_no_clear.drop(['weather_description'], axis=1, inplace=True)

features_gen.to_csv(
    'ML Backend/Training Data/features_gen.csv', compression='zip')
labels_gen.to_csv('ML Backend/Training Data/labels_gen.csv', compression='zip')
features_gen_no_clear.to_csv(
    'ML Backend/Training Data/features_gen_no_clear.csv', compression='zip')
labels_gen_no_clear.to_csv(
    'ML Backend/Training Data/labels_gen_no_clear.csv', compression='zip')

print("done with data preprocessing")
