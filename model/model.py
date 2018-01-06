import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression

from pipeline import main
from constants import THRESHOLD


class MyModel():
    def __init__(self):
        ''' initialize model '''
        self.vect = TfidfVectorizer()
        self.nb = MultinomialNB()
        self.lr = LogisticRegression()

    def fit(self, X_text, X_num, y):
        ''' fit model based on training data '''
        X_text = self.vect.fit_transform(X_text)
        self.nb.fit(X_text, y)
        self.lr.fit(X_num,y)

    def predict_proba(self, X_text, X_num):
        ''' calculate probability that item is fraud '''
        pred_num = self.lr.predict_proba(X_num)[:, 1][0]
        X_t = self.vect.transform(X_text)
        pred_txt = self.nb.predict_proba(X_t)[:, 1][0]
        return (pred_txt + pred_num)/2

    def predict(self, X_text, X_num):
        ''' predict true/false for item '''
        proba = self.predict_proba(X_text, X_num)
        return int(proba > THRESHOLD)


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
