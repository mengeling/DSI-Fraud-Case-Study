import time
import pandas as pd
import requests
import pickle
from pymongo import MongoClient
import sys
sys.path.append('..')
sys.path.insert(0, '/Users/mengeling/Documents/Galvanize/Fraud-Case-Study/model')
from model import predict
from pipeline import clean_data
from model import MyModel


def add_to_database(d):
    if collection.find_one({"object_id": d["object_id"]}) is None:
        return collection.insert_one(d)


def get_datapoint():
    d = requests.get('http://galvanize-case-study-on-fraud.herokuapp.com/data_point').json()
    df = pd.DataFrame([d])
    df = df[["sale_duration2", "user_age", "body_length", "description", "ticket_types"]]
    df = clean_data(df)
    X_text = df.pop("description")
    return d, X_text, df


def set_up_database():
    client = MongoClient()
    db = client["fraud"]
    collection = db["fraud"]
    return collection


def acquire_data():
    while True:
        d, X_text, df = get_datapoint()
        X_num = df.values
        prediction, probability = predict(model, X_text, X_num)
        d["total_payout"] = df["total_payout"].values[0]
        d["prediction"] = prediction
        d["probability"] = probability
        add_to_database(d)
        time.sleep(5)


if __name__ == '__main__':
    collection = set_up_database()
    with open('../model/model.pkl', 'rb') as f:
        model = pickle.load(f)
    acquire_data()