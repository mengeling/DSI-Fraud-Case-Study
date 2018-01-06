import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

import sys
sys.path.append('../model')
from pipeline import clean_data
from constants import EDA_COLS


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
    scatter_matrix(df, figsize=(12, 12), diagonal='kde')
    plt.savefig("images/scatter_matrix.png")


if __name__ == '__main__':
    ''' reads in data and makes plots '''
    df = clean_data(pd.read_json('../data/data.json'))
    plot_histograms(df[EDA_COLS])
    plot_scatter_matrix(df[EDA_COLS])
