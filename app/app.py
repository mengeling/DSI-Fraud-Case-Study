import json
import requests
import pickle
import time
from flask import Flask, request, render_template
from pymongo import MongoClient
import sys
sys.path.append('..')
from model.model import predict
from model.pipeline import clean_data
from model.model import MyModel


app = Flask(__name__)


@app.route('/')
def index():
    high_risk_data = retrieve_data_from_db()
    # high_risk_data = " "
    med_risk_data = " "
    low_risk_data = " "
    # #data = get_data_from_db()
    # #data = get_live_data()
    # if data['total_payout'] > 500:
    #     high_risk_data = data
    # elif data['total_payout'] > 100:
    #     med_risk_data = data
    # else:
    #     low_risk_data = data
    return render_template('index.html', high_risk_data=high_risk_data, med_risk_data=med_risk_data, low_risk_data=low_risk_data)


@app.route('/score', methods=['POST'])
def score():
    data = get_data()
    # text = np.array([request.form['text']])
    # prediction = model.predict(text)[0]
    return render_template('submit.html', data=data)



def retrieve_data_from_db():
    return collection.find()


def add_to_database(d):
    if collection.find_one({"object_id": d["object_id"]}) is None:
        return collection.insert_one(d)


def get_datapoint():
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
        d, X_text, X_num = get_datapoint()
        prediction, probability = predict(model, X_text, X_num)
        d["prediction"] = prediction
        d["probability"] = probability
        add_to_database(d)
        time.sleep(5)
