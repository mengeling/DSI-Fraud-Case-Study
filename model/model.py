import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

from pipeline import main
from constants import THRESHOLD


class MyModel():
    def __init__(self):
        ''' initialize model '''
        self.vect = TfidfVectorizer()
        self.rf_text = RandomForestClassifier(n_estimators=50)
        self.rf_num = RandomForestClassifier(n_estimators=50)

    def fit(self, X_text, X_num, y):
        ''' fit model based on training data '''
        X_text = self.vect.fit_transform(X_text)
        self.rf_text.fit(X_text, y)
        self.rf_num.fit(X_num, y)

    def predict_proba(self, X_text, X_num):
        ''' calculate probability that item is fraud '''
        X_t = self.vect.transform(X_text)
        pred_txt = self.rf_text.predict_proba(X_t)[:, 1]
        pred_num = self.rf_num.predict_proba(X_num)[:, 1]
        return np.mean([pred_txt, pred_num], axis=0)

    def predict(self, X_text, X_num):
        ''' predict true/false for item '''
        proba = self.predict_proba(X_text, X_num)
        return (proba > THRESHOLD).astype(int)


def predict(model, X_text, X_num):
    ''' return predictions for a new item'''
    prediction = model.predict(X_text, X_num)
    probability = model.predict_proba(X_text, X_num)
    return prediction, probability


if __name__ == '__main__':
    ''' run model.py to generate a model to base predictions on'''
    X_text, X_num, y = main()
    model = MyModel()
    model.fit(X_text, X_num, y)
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
