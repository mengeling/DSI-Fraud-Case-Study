import json
import requests
import pickle
import time
import threading
import os
import pandas as pd
from flask import Flask, render_template
from acquire_data import set_up_database
from pymongo import MongoClient



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


def retrieve_data_from_db():
    for d in collection.find():
        print(d)
    return [d for d in collection.find() if d["total_payout"] > 100]



    #
    # thread = threading.Thread(target=run_job())
    # print("start")
    # thread.start()
    # print("start")

if __name__ == '__main__':
    collection = set_up_database()
    os.system("python acquire_data.py &")
    app.run(host='0.0.0.0', port=8080, debug=True)

