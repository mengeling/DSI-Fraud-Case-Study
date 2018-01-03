import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('..')
from model.pipeline import get_numeric_data


def plot_histograms(df):
    cols = [
        "user_age", "body_length", "channels", "delivery_method", "fb_published", "has_analytics",
        "num_payouts", "sale_duration2"
    ]
    for col in cols:
        plt.hist(df[col], bins=50)
        plt.title(col)
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.savefig("images/hist_{}.png".format(col))


if __name__ == '__main__':
    df = pd.read_json('../data/data.json')
    df = get_numeric_data(df)
    plot_histograms(df)