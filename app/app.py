from flask import Flask, request, render_template
import json
import requests
import pickle
import time
import pymongo
from datetime import datetime
import sys
sys.path.append('..')

# from model import predict

app = Flask(__name__)
DATA = []
TIMESTAMP = []

data = {
    "approx_payout_date": 1366956000,
    "body_length": 41,
    "channels": 11,
    "country": "CR",
    "currency": "USD",
    "delivery_method": 0.0,
    "description": "<p>Unlimited bowling and pizza.&nbsp;</p>",
    "email_domain": "continentalrescueafrica.com",
    "event_created": 1364920231,
    "event_end": 1366524000,
    "event_published": 1364920533.0,
    "event_start": 1366509600,
    "fb_published": 0,
    "gts": 110.45,
    "has_analytics": 0,
    "has_logo": 1,
    "listed": "y",
    "name": "Bowl for Change Fundraiser",
    "name_length": 26,
    "num_order": 1,
    "num_payouts": 0,
    "object_id": 6088095,
    "org_desc": "<p>Continental Rescue Africa is an international development organization which provides education, and resources for youth in Africa.&nbsp;</p>",
    "org_facebook": 41.0,
    "org_name": "Continental Rescue Africa",
    "org_twitter": 0.0,
    "payee_name": "",
    "payout_type": "ACH",
    "previous_payouts": [

    ],
    "sale_duration": 18.0,
    "sale_duration2": 18,
    "show_map": 1,
    "ticket_types": [
        {
            "availability": 1,
            "cost": 20.0,
            "event_id": 6088095,
            "quantity_sold": 0,
            "quantity_total": 1
        },
        {
            "availability": 1,
            "cost": 20.0,
            "event_id": 6088095,
            "quantity_sold": 5,
            "quantity_total": 5
        },
        {
            "availability": 1,
            "cost": 0.0,
            "event_id": 6088095,
            "quantity_sold": 0,
            "quantity_total": 0
        }
    ],
    "total_payout": 400,
    "user_age": 0,
    "user_created": 1364919449,
    "user_type": 1,
    "venue_address": "128 Queen St E",
    "venue_country": "CA",
    "venue_latitude": 43.5554641,
    "venue_longitude": -79.5871987,
    "venue_name": "Streetsville Bowl",
    "venue_state": "ON"
}


def get_live_data():
    r = requests.get('http://galvanize-case-study-on-fraud.herokuapp.com/data_point')
    return json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
    # DATA.append(json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': ')))
    # TIMESTAMP.append(time.time())

def get_data_from_db():
    r = db.collection.findOne()
    return json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
    # DATA.append(json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': ')))
    # TIMESTAMP.append(time.time())



@app.route('/')
def index():
    high_risk_data = " "
    med_risk_data = " "
    low_risk_data = " "
    #data = get_data_from_db()
    #data = get_live_data()
    if data['total_payout'] > 500:
        high_risk_data = data
    elif data['total_payout'] > 100:
        med_risk_data = data
    else:
        low_risk_data = data
    return render_template('index.html', high_risk_data=high_risk_data, med_risk_data=med_risk_data, low_risk_data=low_risk_data)


@app.route('/score', methods=['POST'])
def score():
    data = get_data()
    # text = np.array([request.form['text']])
    # prediction = model.predict(text)[0]
    return render_template('submit.html', data=data)


# @app.route('/check')
# def check():
#     line1 = "Number of data points: {0}".format(len(DATA))
#     if DATA and TIMESTAMP:
#         dt = datetime.fromtimestamp(TIMESTAMP[-1])
#         data_time = dt.strftime('%Y-%m-%d %H:%M:%S')
#         line2 = "Latest datapoint received at: {0}".format(data_time)
#         line3 = DATA[-1]
#         output = "{0}\n\n{1}\n\n{2}".format(line1, line2, line3)
#     else:
#         output = line1
#     return output, 200, {'Content-Type': 'text/css; charset=utf-8'}


if __name__ == '__main__':
    # with open('../model/model.pkl', 'rb') as f:
    #     model = pickle.load(f)
    # connect to database
    app.run(host='0.0.0.0', port=8080, debug=True)
    while True:
        get_data()
        time.sleep(5)
