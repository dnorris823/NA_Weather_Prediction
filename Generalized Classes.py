# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import pandas as pd


# %%
labels = pd.read_csv('labels.csv', compression='zip')
labels.drop(['Unnamed: 0'], axis=1, inplace=True)

features = pd.read_csv('features.csv', compression='zip')
features.drop(['Unnamed: 0'], axis=1, inplace=True)

engineered_features = pd.read_csv('engineered_features.csv', compression='zip')
engineered_features.drop(['Unnamed: 0'], axis=1, inplace=True)


# %%
engineered_features['weather_description'] = labels
engineered_features.head()


# %%
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


# %%
engineered_features['weather_description'].value_counts()


# %%
features_gen_no_clear = []
features_gen_no_clear = engineered_features[~engineered_features['weather_description'].str.contains(
    "Clear Weather")]


# %%
features_gen_no_clear['weather_description'].value_counts()


# %%
labels_gen = []
labels_gen = engineered_features['weather_description']
engineered_features.drop(['weather_description'], axis=1, inplace=True)
features_gen = []
features_gen = engineered_features
labels_gen_no_clear = []
labels_gen_no_clear = features_gen_no_clear['weather_description']
features_gen_no_clear.drop(['weather_description'], axis=1, inplace=True)


# %%
features_gen.to_csv('features_gen.csv', compression='zip')
labels_gen.to_csv('labels_gen.csv', compression='zip')
features_gen_no_clear.to_csv('features_gen_no_clear.csv', compression='zip')
labels_gen_no_clear.to_csv('labels_gen_no_clear.csv', compression='zip')


# %%
