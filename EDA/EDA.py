import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import sys
sys.path.append('..')
from model.pipeline import get_numeric_data


def plot_histograms(df):
    for col in cols:
        plt.hist(df[col], bins=50)
        plt.title(col)
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.savefig("images/hist_{}.png".format(col))


def plot_scatter_matrix(df):
    scatter_matrix(df, figsize=(10, 10), diagonal='kde')
    plt.savefig("images/scatter_matrix.png")


if __name__ == '__main__':
    df = pd.read_json('../data/data.json')
    cols = [
        "user_age", "body_length", "channels", "delivery_method", "fb_published", "has_analytics",
        "num_payouts", "sale_duration2"
    ]
    df = df[cols]
    df = get_numeric_data(df)
    plot_histograms(df)
    plot_scatter_matrix(df)