import pandas as pd
from model import MyModel
from pipeline import clean_data
import pickle

df = pd.read_json('../data/example.json')
df1 = df.head(1)
df1 = df1[["sale_duration2", "user_age", "body_length", "description", "ticket_types"]]
ticket_types_lst = df1["ticket_types"]
total = 0
for d in ticket_types_lst:
    total += d['quantity_sold'] * d['cost']

# print(total)
# print(ticket_types_lst)
# print(sum(d['quantity_sold'] * d['cost'] for d in ticket_types_lst))
df = clean_data(df1)
#y = df.pop("fraud")
X_text = df.pop("description")
X_num = df.values
#print(df1)

#data = clean_data(df1)
#print(data)
#y = data.pop('fraud')
#, X_num, y = pipeline.main()
#model = model.MyModel()
#model.fit(X_text,X_num,y)


with open('model.pkl', 'rb') as f:
    m = pickle.load(f)

    pred = m.predict(X_text, X_num)

print(pred)


def get_data():
    data = requests.get('http://galvanize-case-study-on-fraud.herokuapp.com/data_point').json()


if __name__ == '__main__':
    d = get_data()
    df = pd.read_dict(d)
    df = df[["sale_duration2", "user_age", "body_length", "description", "ticket_types"]]
    ticket_types_lst = df["ticket_types"]
    data["prediction"] = prediction
    data["probability"] = probability