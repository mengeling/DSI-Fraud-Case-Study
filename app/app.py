import json
import requests
import pickle
import time
from flask import Flask, request, render_template
from pymongo import MongoClient
import sys
sys.path.append('..')
from model.model import predict
from model.pipeline import clean_data, main
from model.model import MyModel

app = Flask(__name__)


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


def add_to_database(d, collection):
    obj_id = d["object_id"]
    if collection.find_one({"object_id": d["object_id"]}) is None:
        return collection.insert_one(d)


def get_data():
    d = requests.get('http://galvanize-case-study-on-fraud.herokuapp.com/data_point').json()
    df = pd.DataFrame([d])
    df = df[["sale_duration2", "user_age", "body_length", "description", "ticket_types"]]
    df = clean_data(df)
    X_text = df.pop("description")
    X_num = df.values
    return d, X_text, X_num


def set_up_database():
    client = MongoClient()
    db = client["fraud"]
    collection = db["fraud"]
    return collection


if __name__ == '__main__':
    collection = set_up_database()
    with open('../model/model.pkl', 'rb') as f:
        model = pickle.load(f)
    app.run(host='0.0.0.0', port=8080, debug=True)
    while True:
        d, X_text, X_num = get_data()
        prediction, probability = predict(model, X_text, X_num)
        d["prediction"] = prediction
        d["probability"] = probability
        add_to_database(d)
        time.sleep(5)
