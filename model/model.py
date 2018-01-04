import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from pipeline import main


class MyModel():
    def __init__(self):
        self.vect = TfidfVectorizer()
        self.nb = MultinomialNB()
        self.lr = LogisticRegression()

    def fit(self, X_text, X_num, y):
        X_text = self.vect.fit_transform(X_text)
        self.nb.fit(X_text, y)
        self.lr.fit(X_num,y)

    def predict_proba(self, X_text, X_num):
        pred_num = self.lr.predict_proba(X_num)[:, 1]
        X_t = self.vect.transform(X_text)
        pred_txt = self.nb.predict_proba(X_t)[:, 1]
        return (pred_txt[0] + pred_num[0])/2

    def predict(self, X_text, X_num):
        proba = self.predict_proba(X_text, X_num)
        return int(proba > 0.5)


if __name__ == '__main__':
    X_text, X_num, y = main()
    model = MyModel()
    model.fit(X_text, X_num, y)
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
