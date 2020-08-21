from flask import Flask, redirect, url_for, render_template, request, jsonify, flash
import requests
import os
from werkzeug.utils import secure_filename
import pandas as pd
import json
import pprint
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import plotly
import plotly.graph_objs as go


UPLOAD_FOLDER = 'Web App/user_files'
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/multi_prediction', methods=['GET', 'POST'])
def multi_prediction():
    return render_template("multi_prediction.html")


@app.route("/single_prediction", methods=["GET", "POST"])
def Home():
    if request.method == "POST":
        # print(request.form, flush=True)

        # make sure user entered a value for all boxes
        missing = list()

        for k, v in request.form.items():
            if v == "":
                missing.append(k)

        if missing:
            feedback = f"Missing fields for {', '.join(missing)}"
            return render_template("/single_prediction.html", feedback=feedback)
        print("past missing", flush=True)
        # get all user input
        Humidity = request.form["Humidity"]
        Temperature = request.form["Temperature"]
        Pressure = request.form["Pressure"]
        Wind_Direction = request.form["Wind_Direction"]
        Wind_Speed = request.form["Wind_Speed"]
        Latitude = request.form["Latitude"]
        Longitude = request.form["Longitude"]
        Month = request.form["Month"]
        Day = request.form["Day"]
        Hour = request.form["Hour"]

        # create json object with user input

        prediction_input = {
            "humidity": Humidity,
            "temperature": Temperature,
            "pressure": Pressure,
            "wind_direction": Wind_Direction,
            "wind_speed": Wind_Speed,
            "Latitude": Latitude,
            "Longitude": Longitude,
            "month": Month,
            "day": Day,
            "hour": Hour,
            "day_avg_hum": 67.82,
            "month_avg_hum": 67.82,
            "year_avg_hum": 67.82,
            "day_avg_temp": 287.59,
            "month_avg_temp": 287.59,
            "year_avg_temp": 287.59,
            "day_avg_press": 1018.11,
            "month_avg_press": 1018.11,
            "year_avg_press": 1018.11
        }
        '''
        prediction_input = {
            "humidity": 52,
            "Temperature": 281.98,
            "pressure": 1005.0,
            "wind_direction": 280,
            "wind speed": 3.0,
            "Latitude": 42.358429,
            "Longitude": -71.059769,
            "month": 7,
            "day": 26,
            "hour": 10,
            "day_avg_hum": 57.333333,
            "month_avg_hum": 72.667123,
            "year_avg_hum": 76.430804,
            "day_avg_temp": 282.687917,
            "month_avg_temp": 280.456582,
            "year_avg_temp": 284.286528,
            "day_avg_press": 1004.916667,
            "month_avg_press": 1017.215068,
            "year_avg_press": 1017.478836
        }
        '''
        pprint.pprint(prediction_input)

        try:
            prediction_output = requests.post(
                'http://127.0.0.1:80/predict', json=prediction_input)

            prediction_output_text = prediction_output.text
            print(prediction_output_text, flush=True)

            prediction_strings = prediction_output_text.split(':')
            print(str(prediction_strings[1]), flush=True)
            print("LENGTH: " + str(len(prediction_strings[1])), flush=True)
            prediction_final = prediction_strings[1][3:len(
                prediction_strings[1]) - 5]

        except Exception as e:
            print(str(e), flush=True)

        return render_template("/single_prediction.html", prediction=prediction_final)

    return render_template("single_prediction.html")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload_features', methods=['POST'])
def upload_features():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file_features' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file_features']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(
                app.config['UPLOAD_FOLDER'], 'user_file_features.csv'))
            return render_template("multi_prediction.html", upload_complete_features='Upload of ' + filename + ' complete!')
        return render_template("multi_prediction.html")


@app.route('/upload_labels', methods=['POST'])
def upload_labels():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file_labels' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file_labels']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(
                app.config['UPLOAD_FOLDER'], 'user_file_labels.csv'))
            return render_template("multi_prediction.html", upload_complete_labels='Upload of ' + filename + ' complete!')
    return render_template("multi_prediction.html")


@app.route('/move_to_backend', methods=['GET', 'POST'])
def move_to_backend():
    if request.method == 'POST':
        try:

            files = {'file': open(
                'Web App/user_files/user_file_features.csv', 'rb')}

            move_to_back = requests.post(
                'http://127.0.0.1:80/multi_predict', files=files)
            prediction_text = move_to_back.text
            prediction_text = prediction_text.replace('[', '')
            prediction_text = prediction_text.replace(']', '')
            prediction_text = prediction_text.replace('"', '')
            prediction_text = prediction_text.replace("'", '')
            prediction_text = prediction_text.replace("\\", '')

            prediction_text = prediction_text.split(',')

            prediction_text_len = len(prediction_text)

            user_labels = pd.read_csv(
                'Web App/user_files/user_file_labels.csv')

            user_labels.drop(['Unnamed: 0'], axis=1, inplace=True)

            prediction_text_df = pd.DataFrame(
                prediction_text, columns=["weather_description"])

            conf_matrix = confusion_matrix(user_labels, prediction_text_df)
            len_conf_matrix = len(conf_matrix[0])
            class_report = classification_report(
                user_labels, prediction_text_df, output_dict=True)
            len_class_matrix = len(class_report)
            acc_score = accuracy_score(user_labels, prediction_text_df)

            class_report.pop('accuracy')
            class_report.pop('macro avg')
            class_report.pop('weighted avg')

            class_list = class_report.keys()
            class_list = list(class_list)

            data = [
                go.Bar(
                    x=prediction_text_df['weather_description'].value_counts(
                    ).index,
                    y=prediction_text_df['weather_description'].value_counts()
                )
            ]

            graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

            print(
                prediction_text_df['weather_description'].value_counts().index, flush=True)

        except Exception as e:
            print(str(e), flush=True)
            return render_template("multi_prediction.html")

        return render_template("multi_prediction.html",
                               prediction=True,
                               prediction_text_len=len(prediction_text),
                               prediction_text=prediction_text,
                               conf_matrix=conf_matrix,
                               len_conf_matrix=len_conf_matrix,
                               class_report=class_report,
                               class_list=class_list,
                               len_class_matrix=len_class_matrix,
                               acc_score=acc_score,
                               graphJSON=graphJSON
                               )


if __name__ == "__main__":
    app.run()
