from flask import Flask, redirect, url_for, render_template, request, jsonify
import requests

app = Flask(__name__)


@app.route("/predict", methods=["GET", "POST"])
def Home():
    if request.method == "POST":
        #print(request.form, flush=True)

        # make sure user entered a value for all boxes
        missing = list()

        for k, v in request.form.items():
            if v == "":
                missing.append(k)

        if missing:
            feedback = f"Missing fields for {', '.join(missing)}"
            return render_template("/signup.html", feedback=feedback)
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
        '''
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

        print(prediction_input, flush=True)

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

            print(prediction_final, flush=True)

        except Exception as e:
            print(str(e), flush=True)
        return render_template("/signup.html", prediction=prediction_final)

    return render_template("signup.html")


if __name__ == "__main__":
    print("hello")
    app.run()