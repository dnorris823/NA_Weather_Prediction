from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def Home():
    return render_template("main.html")


@app.route("/", methods=['POST'])
def GetModelInputs():
    model_input = []
    model_input['humidity'] = []
    model_input['temperature'] = []
    model_input['pressure'] = []
    model_input['wind direction'] = []
    model_input['wind speed'] = []
    model_input['Latitude'] = []
    model_input['Longitude'] = []
    model_input['month'] = []
    model_input['day'] = []
    model_input['hour'] = []
    model_input['humidity'] = request.form['humidity']
    model_input['temperature'] = request.form['temperature']
    model_input['pressure'] = request.form['pressure']
    model_input['wind direction'] = request.form['wind direction']
    model_input['wind speed'] = request.form['wind speed']
    model_input['Latitude'] = request.form['Latitude']
    model_input['Longitude'] = request.form['Longitude']
    model_input['month'] = request.form['month']
    model_input['day'] = request.form['day']
    model_input['hour'] = request.form['hour']

    return render_template("main.html")


if __name__ == "__main__":
    app.run()
