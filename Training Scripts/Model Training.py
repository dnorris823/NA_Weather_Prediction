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
import pickle

# %%
labels_bin = pd.read_csv('labels_bin.csv', compression='zip')
features = pd.read_csv('features.csv', compression='zip')

labels_bin.drop(['Unnamed: 0'], axis=1, inplace=True)
features.drop(['Unnamed: 0'], axis=1, inplace=True)

# %%
X_train, X_test, y_train, y_test = train_test_split(
    features, labels_bin, test_size=0.33, random_state=42)

# %%
# Create the model with 100 trees
bin_model = RandomForestClassifier(n_estimators=500,
                                   oob_score=True,
                                   n_jobs=-1,
                                   random_state=50,
                                   max_features="auto",
                                   verbose=True)
# Fit on training data
bin_model.fit(X_train, y_train)
y_pred = bin_model.predict(X_test)


# %%
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(accuracy_score(y_test, y_pred))


# %%
train_rf_predictions = bin_model.predict(X_train)
train_rf_probs = bin_model.predict_proba(X_train)[:, 1]

# Actual class predictions
rf_predictions = bin_model.predict(X_test)
# Probabilities for each class
rf_probs = bin_model.predict_proba(X_test)[:, 1]


# %%
# Calculate roc auc
roc_value = roc_auc_score(y_test, rf_probs)
roc_value_train = roc_auc_score(y_train, train_rf_probs)


# %%
print("Model ROC value")
print(roc_value)

# %%
print("Training ROC value")
print(roc_value_train)

# %%
filename = 'Saved_models/binary_model.sav'
pickle.dump(bin_model, open(filename, 'wb'))

# %%
labels_gen_no_clear = pd.read_csv('labels_gen_no_clear.csv', compression='zip')
features_gen_no_clear = pd.read_csv(
    'features_gen_no_clear.csv', compression='zip')

labels_gen_no_clear.drop(['Unnamed: 0'], axis=1, inplace=True)
features_gen_no_clear.drop(['Unnamed: 0'], axis=1, inplace=True)

# %%
# Creating the Training and Test set from data
X_train, X_test, y_train, y_test = train_test_split(
    features_gen_no_clear, labels_gen_no_clear, test_size=0.25, random_state=21)

# %%
# Fitting Random Forest Classification to the Training set
multi_model = RandomForestClassifier(n_estimators=500,
                                     oob_score=True,
                                     n_jobs=-1,
                                     random_state=50,
                                     max_features="auto",
                                     verbose=True)
multi_model.fit(X_train, y_train)
y_pred = multi_model.predict(X_test)


# %%
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(accuracy_score(y_test, y_pred))

# %%
filename = 'Saved_models/multiclass_model.sav'
pickle.dump(multi_model, open(filename, 'wb'))
