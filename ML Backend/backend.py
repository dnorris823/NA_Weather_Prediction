from flask import Flask, request, redirect, url_for, render_template, jsonify
from sklearn.externals import joblib
import os
import pandas as pd
import requests

app = Flask(__name__)


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


@app.route('/predict', methods=['POST'])
def predict():
    # Load "bin_model.pkl"
    bin_model = joblib.load("Saved Models/bin_model.pkl")
    # Load "multi_model.pkl"
    multi_model = joblib.load("Saved Models/multi_model.pkl")

    model_input = request.json
    print(model_input, flush=True)
    model_input = pd.DataFrame(model_input, index=[0])
    bin_prediction = bin_model.predict(model_input)

    if bin_prediction:
        return jsonify({'prediction': "Clear Skies"})
    else:
        return jsonify({'prediction': str(multi_model.predict(model_input))})


@app.route('/test_response', methods=['GET', 'POST'])
def test_response():
    return request.text


@app.route('/upload_file', methods=['POST'])
def upload_file():
    return request.files


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
