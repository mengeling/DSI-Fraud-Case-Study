import os
import datetime
from flask import Flask, render_template

from acquire_data import set_up_database


app = Flask(__name__)


@app.route('/')
def index():
    data = retrieve_data_from_db()
    low_risk = []
    medium_risk = []
    high_risk = []
    for lst in data:
        # if lst[2] >= 0.1:
        #     high_risk.append(lst)
        # elif (lst[2] > 0.05) and (lst[2] < 0.1):
        #     medium_risk.append(lst)
        # # else:
        # #     low_risk.append(lst)
        high_risk.append(lst)
    return render_template('index.html', high_risk=high_risk)


def retrieve_data_from_db():
    lst = []
    for i, d in enumerate(collection.find()):
        if i < 25:
            date = datetime.datetime.fromtimestamp(d["approx_payout_date"])
            if d["prediction"]:
                prediction = "Fraud"
            else:
                prediction = " Not Fraud"
            lst.append([d["name"], date.strftime('%Y-%m-%d'), round(d["probability"], 2), prediction])
    return lst


if __name__ == '__main__':
    collection = set_up_database()
    os.system("python acquire_data.py &")
    app.run(host='0.0.0.0', port=8000, debug=True)

