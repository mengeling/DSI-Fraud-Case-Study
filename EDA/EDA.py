import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from itertools import product

import sys
sys.path.append('../model')
from pipeline import clean_data, main
from constants import EDA_COLS, PREDICT_COLS, THRESHOLD
from model import MyModel


def plot_histograms(df):
    ''' creates a histogram '''
    for col in EDA_COLS:
        plt.hist(df[col], bins=50)
        plt.title(col)
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.savefig("images/hist_{}.png".format(col))


def plot_scatter_matrix(df):
    ''' creates a scatter-matrix plot '''
    scatter_matrix(df, alpha=0.2, figsize=(15, 15), diagonal='kde')
    plt.tight_layout()
    plt.savefig("images/scatter_matrix.png")


def create_confusion_matrix():
    ''' creates a confusion matrix '''
    X_text, X_num, y = main()
    X_text_train, X_text_test, X_num_train, X_num_test, y_train, y_test = train_test_split(X_text, X_num, y)
    model = MyModel()
    model.fit(X_text_train, X_num_train, y_train)
    predictions = model.predict(X_text_test, X_num_test)
    return confusion_matrix(y_test, predictions)


def plot_confusion_matrix():
    ''' plots confusion matrix (tweaked sklearn's implementation) '''
    cm = create_confusion_matrix()
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title("Confusion Matrix")
    plt.colorbar()
    plt.xticks(np.arange(2), ["Not Fraud", "Fraud"], rotation=45)
    plt.yticks(np.arange(2), ["Not Fraud", "Fraud"])
    for i, j in product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], 'd'), horizontalalignment="center",
                 color="white" if cm[i, j] > cm.max() / 2 else "black")
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.savefig("images/confusion_matrix.png")


if __name__ == '__main__':
    ''' reads in data and makes plots '''
    df = clean_data(pd.read_json('../data/data.json'))
    plot_histograms(df[EDA_COLS])
    plot_scatter_matrix(df[EDA_COLS])
    plot_confusion_matrix()
