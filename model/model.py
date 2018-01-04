import random
import pickle
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from pipeline import main


class MyModel():
    def __init__(self):
        self.vect = TfidfVectorizer()
        self.clas = MultinomialNB()
        self.lr = LogisticRegression()

    def fit(self, X_text, X_num, y):
        #self.vect = TfidfVectorizer()
        X_text = self.vect.fit_transform(X_text)

        #clas = MultinomialNB()
        self.clas.fit(X_text, y)

        self.lr.fit(X_num,y)

    def predict(self, X_text, X_num):

        #X_text = df.pop('description')
        #X_num = pd.get_dummies(df).values
        #print(X_num)
        pred_num = self.lr.predict_proba(X_num)[:, 1]
        X_t = self.vect.transform(X_text)
        pred_txt = self.clas.predict_proba(X_t)[:, 1]
        #return np.mean(pred_num, pred_txt)
        return (pred_txt[0] + pred_num[0])/2
        #return (np.array(pred_txt) + np.array(pred_num))/2
        #print(pred_num)

#def get_data(datafile):
#    return X, y


if __name__ == '__main__':
    #X, y = get_data('data/data.json')
    X_text, X_num, y = main()
    model = MyModel()
    model.fit(X_text, X_num, y)
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
