import random
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from pipeline import main

class MyModel():
    def __init__(self):
        self.vect = TfidfVectorizer()
        self.clas = MultinomialNB()
        self.dt = DecisionTreeClassifier()

    def fit(self, X_text, X_num, y):
        #self.vect = TfidfVectorizer()
        X_text = self.vect.fit_transform(X_text)

        #clas = MultinomialNB()
        self.clas.fit(X_text, y)

        self.dt.fit(X_num,y)

    def predict(self, X, y):

        pred_num = self.dt.predict_proba(X)
        X_t = self._vectorizer.transform(X)
        pred_txt = self.clas.predict_proba(X_t)
        
        return (np.array(pred_txt) + np.array(pred_num))/2


#def get_data(datafile):
#    return X, y


if __name__ == '__main__':
    #X, y = get_data('data/data.json')
    X_text, X_num, y = main()
    model = MyModel()
    model.fit(X_text, X_num, y)
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
