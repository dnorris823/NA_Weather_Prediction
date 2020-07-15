# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib
from sklearn.model_selection import GridSearchCV


# %%
labels = pd.read_csv('labels.csv', compression='zip')
features = pd.read_csv('features.csv', compression='zip')
labels_gen = pd.read_csv('labels_gen.csv', compression='zip')
features_gen = pd.read_csv('features_gen.csv', compression='zip')
labels_gen_no_clear = pd.read_csv('labels_gen_no_clear.csv', compression='zip')
features_gen_no_clear = pd.read_csv(
    'features_gen_no_clear.csv', compression='zip')

labels.drop(['Unnamed: 0'], axis=1, inplace=True)
features.drop(['Unnamed: 0'], axis=1, inplace=True)
labels_gen.drop(['Unnamed: 0'], axis=1, inplace=True)
features_gen.drop(['Unnamed: 0'], axis=1, inplace=True)
labels_gen_no_clear.drop(['Unnamed: 0'], axis=1, inplace=True)
features_gen_no_clear.drop(['Unnamed: 0'], axis=1, inplace=True)


# %%
labels_gen['weather_description'][0]


# %%
features_gen.head()


# %%
labels_2 = labels


# %%
# Creating the Training and Test set from data
X_train, X_test, y_train, y_test = train_test_split(
    features_gen, labels_gen, test_size=0.25, random_state=21)


# %%
# Feature Scaling
#scaler = StandardScaler()
#X_train = scaler.fit_transform(X_train)
#X_test = scaler.transform(X_test)


# %%
parameters = {
    'n_estimators': [100, 130],
    # 'max_features': ['auto'],
    # 'criterion' :['gini']
}

#clf = GridSearchCV(RandomForestClassifier(), parameters, cv=5, n_jobs=-1)
#clf.fit(X_train, y_train)

# Fitting Random Forest Classification to the Training set
classifier = RandomForestClassifier(n_estimators=100, oob_score=True, n_jobs=-1,
                                    random_state=50,                                         max_features="auto", verbose=True)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)


# %%
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(accuracy_score(y_test, y_pred))


# %%
y_pred


# %%
labels


# %%


# %%
labels.head()


# %%


# %%
