# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
labels = pd.read_csv('labels.csv', compression='zip')
labels.drop(['Unnamed: 0'], axis=1, inplace=True)


# %%
labels.loc[labels['weather_description'] !=
           'sky is clear', 'is_sky_clear'] = False
labels.loc[labels['weather_description'] ==
           'sky is clear', 'is_sky_clear'] = True


# %%
labels.head(10)


# %%
labels['is_sky_clear'].value_counts()


# %%
labels.drop(['weather_description'], axis=1, inplace=True)

# %%
labels[:10]


# %%
labels = pd.DataFrame(labels)
labels.to_csv('labels_bin.csv', compression='zip')


# %%
