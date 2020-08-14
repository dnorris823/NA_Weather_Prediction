from flask import Flask, request, redirect, url_for, render_template, jsonify
from sklearn.externals import joblib
import os
import pandas as pd
import requests
import json

UPLOAD_FOLDER = 'user_files'
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/model_training', methods=['GET'])
def model_training():
    try:
        exec(open("Training Scripts/Data Preprocessing.py").read())
        exec(open("Training Scripts/Model Training.py").read())
    except Exception as e:
        return str(e)

    if os.path.exists('Saved Models/bin_model.pkl') & os.path.exists('Saved Models/multi_model.pkl'):
        return 'Models trained successfully'
    else:
        return 'Models did not train successfully'


@app.route('/load_models', methods=['GET'])
def load_models():
    try:
        if os.path.exists('Saved Models/bin_model.pkl') & os.path.exists('Saved Models/multi_model.pkl'):
            # Load "bin_model.pkl"
            bin_model = joblib.load("Saved Models/bin_model.pkl")
            # Load "multi_model.pkl"
            multi_model = joblib.load("Saved Models/multi_model.pkl")
            return "models loaded successfully"
        else:
            return 'Models do not exist.'

    except Exception as e:
        return str(e)


@app.route('/test_load_models', methods=['GET'])
def test_load_models():
    if os.path.exists('Saved Models/bin_model.pkl') & os.path.exists('Saved Models/multi_model.pkl'):
        # Load "bin_model.pkl"
        bin_model = joblib.load("Saved Models/bin_model.pkl")
        # Load "multi_model.pkl"
        multi_model = joblib.load("Saved Models/multi_model.pkl")
        return ("models loaded")
    else:
        return ("models not loaded")


@app.route('/single_predict', methods=['POST'])
def predict():
    # Load "bin_model.pkl"
    bin_model = joblib.load("Saved Models/bin_model.pkl")
    # Load "multi_model.pkl"
    multi_model = joblib.load("Saved Models/multi_model.pkl")

    model_input = request.json
    model_input = pd.DataFrame(data=model_input, index=[0])

    bin_prediction = bin_model.predict(model_input)

    if bin_prediction:
        return jsonify({'prediction': "['Clear Skies']"})
    else:
        return jsonify({'prediction': str(multi_model.predict(model_input))})


@ app.route('/test_response', methods=['GET', 'POST'])
def test_response():
    return request.text


@ app.route('/multi_predict', methods=['POST'])
def multi_predict():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            file.save(os.path.join(
                app.config['UPLOAD_FOLDER'], 'user_file.csv'))

        user_features = pd.read_csv(
            'user_files/user_file.csv')

        user_features.drop(['Unnamed: 0'], axis=1, inplace=True)

        # Load "bin_model.pkl"
        bin_model = joblib.load("Saved Models/bin_model.pkl")
        # Load "multi_model.pkl"
        multi_model = joblib.load("Saved Models/multi_model.pkl")

        multi_predictions = []

        for ind in engineered_features.index:
        bin_prediction = bin_model.predict(
            pd.DataFrame(engineered_features.loc[ind]).T)

        if(bin_prediction):
            results.append("['clear skies']")
        else:
            results.append(str(multi_model.predict(
                pd.DataFrame(engineered_features.loc[ind]).T)))

        multi_predictions = pd.DataFrame(
            multi_predictions, columns=['weather_desc'])
    return "file not saved"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
