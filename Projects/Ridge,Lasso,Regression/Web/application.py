import pickle
from flask import Flask, request, render_template
import numpy as np

application = Flask(__name__)
app = application

# load model and scaler
ridge_model = pickle.load(open("models/ridge.pkl", "rb"))
standard_scaler = pickle.load(open("models/scaler.pkl", "rb"))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predictdata", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "POST":

        plan_type = float(request.form["plan_type"])
        avg_weekly_usage_hours = float(request.form["avg_weekly_usage_hours"])
        support_tickets = float(request.form["support_tickets"])
        payment_failures = float(request.form["payment_failures"])
        tenure_months = float(request.form["tenure_months"])
        last_login_days_ago = float(request.form["last_login_days_ago"])

        input_data = np.array([[ 
            plan_type,
            avg_weekly_usage_hours,
            support_tickets,
            payment_failures,
            tenure_months,
            last_login_days_ago
        ]])

        scaled_data = standard_scaler.transform(input_data)

        prediction = ridge_model.predict(scaled_data)

        return render_template(
            "home.html",
            result=round(prediction[0], 3)
        )

    else:
        return render_template("home.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
