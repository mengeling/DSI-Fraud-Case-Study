from flask import Flask, request, render_template
import json
import requests
import pickle
import time
from datetime import datetime
import sys
sys.path.append('..')

# from model import predict

app = Flask(__name__)
DATA = []
TIMESTAMP = []


def get_data():
    r = requests.get('http://galvanize-case-study-on-fraud.herokuapp.com/data_point')
    return json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
    # DATA.append(json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': ')))
    # TIMESTAMP.append(time.time())


@app.route('/')
def index():
    return render_template('index.html', data=get_data())


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
