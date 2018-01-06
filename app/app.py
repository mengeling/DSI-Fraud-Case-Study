import os
from datetime import datetime
from flask import Flask, render_template

from acquire_data import set_up_database


app = Flask(__name__)


@app.route('/')
def index():
    high_risk, medium_risk, low_risk = retrieve_data_from_db()
    return render_template('index.html', high_risk=high_risk, medium_risk=medium_risk, low_risk=low_risk)


def retrieve_data_from_db():
    high_risk = []
    medium_risk = []
    low_risk = []
    for i, d in enumerate(collection.find()):
        if i < 50:
            date = datetime.fromtimestamp(d["approx_payout_date"]).strftime('%Y-%m-%d')
            prediction = "Fraud" if d["prediction"] else "Not Fraud"
            if d["probability"] >= 0.8:
                high_risk.append([
                    d["org_name"], d["name"], date, round(d["probability"], 2), prediction
                ])
            elif (d["probability"] > 0.5) and (d["probability"] < 0.8):
                medium_risk.append([
                    d["org_name"], d["name"], date, round(d["probability"], 2), prediction
                ])
            else:
                low_risk.append([
                    d["org_name"], d["name"], date, round(d["probability"], 2), prediction
                ])
    return high_risk, medium_risk, low_risk


if __name__ == '__main__':
    collection = set_up_database()
    os.system("python acquire_data.py &")
    app.run(host='0.0.0.0', port=8000, debug=True)

