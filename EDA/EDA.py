import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import sys
sys.path.append('..')
from model.pipeline import clean_data


def plot_histograms(df):
    ''' creates a histogram '''
    for col in cols:
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
    ''' reads in training data and makes plots '''
    df = clean_data(pd.read_json('../data/data.json'))
    cols = [
        "user_age", "body_length", "channels", "delivery_method", "fb_published", "has_analytics",
        "num_payouts", "sale_duration2", "total_payout"
    ]
    plot_histograms(df[cols])
    plot_scatter_matrix(df[cols])
