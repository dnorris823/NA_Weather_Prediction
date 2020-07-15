# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


# %%
labels_bin = pd.read_csv('labels_bin.csv', compression='zip')
features = pd.read_csv('features.csv', compression='zip')

labels_bin.drop(['Unnamed: 0'],axis=1, inplace=True)
features.drop(['Unnamed: 0'],axis=1, inplace=True)


# %%
features.head()


# %%
labels_bin['0'].value_counts()


# %%
X_train, X_test, y_train, y_test = train_test_split(features, labels_bin, test_size=0.33, random_state=42)


# %%
# Create the model with 100 trees
model = RandomForestClassifier(n_estimators=30, 
                               bootstrap = True,
                               verbose=True,
                               n_jobs=-1)
# Fit on training data
model.fit(X_train, y_train)
y_pred = model.predict(X_test)


# %%
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))


# %%
train_rf_predictions = model.predict(X_train)
train_rf_probs = model.predict_proba(X_train)[:, 1]

# Actual class predictions
rf_predictions = model.predict(X_test)
# Probabilities for each class
rf_probs = model.predict_proba(X_test)[:, 1]


# %%
# Calculate roc auc
roc_value = roc_auc_score(y_test, rf_probs)
roc_value_train = roc_auc_score(y_train, train_rf_probs)


# %%
print(roc_value)


# %%
print(roc_value_train)


# %%



