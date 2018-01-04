import pandas as pd
from model import MyModel
from pipeline import clean_data
import pickle

df = pd.read_json('../data/example.json')
df1 = df.head(1)

df1 = df1[["sale_duration2", "user_age", "body_length", "description","ticket_types"]]
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
