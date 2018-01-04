import pandas as pd
import requests
from model import MyModel
from pipeline import clean_data
import pickle

# df = pd.read_json('../data/example.json')
# df = df[["sale_duration2", "user_age", "body_length", "description", "ticket_types"]]
# ticket_types_lst = df["ticket_types"]
#
# print(ticket_types_lst)
# print(sum(d['quantity_sold'] * d['cost'] for d in ticket_types_lst))
# df = clean_data(df)
# #y = df.pop("fraud")
# X_text = df.pop("description")
# X_num = df.values
# #print(df1)
#
# #data = clean_data(df1)
# #print(data)
# #y = data.pop('fraud')
# #, X_num, y = pipeline.main()
# #model = model.MyModel()
# #model.fit(X_text,X_num,y)
#
#
# with open('model.pkl', 'rb') as f:
#     m = pickle.load(f)
#
#     pred = m.predict(X_text, X_num)
#
# print(pred)


def predict(model, X_text, X_num):
    prediction = model.predict(X_text, X_num)
    probability = model.predict_proba(X_text, X_num)
    return prediction, probability


def get_data():
    d = requests.get('http://galvanize-case-study-on-fraud.herokuapp.com/data_point').json()
    df = pd.DataFrame([d])
    df = df[["sale_duration2", "user_age", "body_length", "description", "ticket_types"]]
    df = clean_data(df)
    X_text = df.pop("description")
    X_num = df.values
    return d, X_text, X_num


if __name__ == '__main__':
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    d, X_text, X_num = get_data()
    prediction, probability = predict(model, X_text, X_num)
    d["prediction"] = prediction
    d["probability"] = probability
    print(prediction, probability)