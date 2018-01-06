import os
import pandas as pd
from datetime import datetime
from flask import Flask, render_template

from acquire_data import set_up_database


app = Flask(__name__)


@app.route('/')
def index():
    df_high, df_medium, df_low = retrieve_data_from_db()
    print(df_medium)
    high_risk = df_high.sort_values(by='probability', ascending=False).values
    medium_risk = df_medium.sort_values(by='probability', ascending=False).values
    low_risk = df_low.sort_values(by='probability', ascending=False).values
    print(high_risk)
    return render_template('index.html', high_risk=high_risk, medium_risk=medium_risk, low_risk=low_risk)


def retrieve_data_from_db():
    df_high = pd.DataFrame()
    df_medium = pd.DataFrame()
    df_low = pd.DataFrame()
    for i, d in enumerate(collection.find()):
        if i < 50:
            date = datetime.fromtimestamp(d["approx_payout_date"]).strftime('%Y-%m-%d')
            prediction = "Fraud" if d["prediction"] else "Not Fraud"
            if d["probability"] >= 0.8:
                df_high = df_high.append({"org": d["org_name"], "event": d["name"], "date": date,
                                          "probability": round(d["probability"], 2), "prediction": prediction},
                                         ignore_index=True)
            elif (d["probability"] > 0.5) and (d["probability"] < 0.8):
                df_medium = df_medium.append({"org": d["org_name"], "event": d["name"], "date": date,
                                              "probability": round(d["probability"], 2), "prediction": prediction},
                                             ignore_index=True)
            else:
                df_low = df_low.append({"org": d["org_name"], "event": d["name"], "date": date,
                                        "probability": round(d["probability"], 2), "prediction": prediction},
                                       ignore_index=True)
    return df_high, df_medium, df_low


if __name__ == '__main__':
    collection = set_up_database()
    os.system("python acquire_data.py &")
    app.run(host='0.0.0.0', port=8000, debug=True)

