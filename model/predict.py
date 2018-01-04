import pandas as pd
import model
import pipeline

df = pd.read_json('../data/example.json')

X_text, X_num, y = pipeline.main()

model = model.MyModel()
model.fit(X_text,X_num,y)

print(df)
