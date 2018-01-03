import random
import pickle


class MyModel():
    def __init__(self):

    def fit(self):
        pass

    def predict(self):
        return random.choice([True, False])


def get_data(datafile):
    return X, y


if __name__ == '__main__':
    X, y = get_data('data/data.json')
    model = MyModel()
    model.fit(X, y)
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)