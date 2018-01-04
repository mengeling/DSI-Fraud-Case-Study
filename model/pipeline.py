import pandas as pd
from bs4 import BeautifulSoup
import constants as C

def add_labels(df):
    ''' adds 'fraud' column based on 'acct_type' column '''
    df["fraud"] = (df["acct_type"] != "premium").astype(int)
    return df.drop("acct_type", axis=1)


def strip_html(txt):
    ''' extracts text from html '''
    return BeautifulSoup(txt, "lxml").text


def unpack(ticket_types):
    ''' unpacks column 'ticket_types '''
    if type(ticket_types) is dict:
        return ticket_types['quantity_sold'] * ticket_types['cost']
    return sum(d['quantity_sold'] * d['cost'] for d in ticket_types)


def clean_data(df):
    ''' clean input training or test data '''
    df["total_payout"] = df["ticket_types"].apply(unpack)
    df["description"] = df["description"].apply(strip_html)
    df.drop("ticket_types", axis=1, inplace=True)
    df.dropna(inplace=True)
    return df


def run_pipeline():
    ''' extracts text, numeric values, and labels from training data '''
    df = pd.read_json('../data/data.json')
    df = df[C.COLS]     # COLS defined in constants.py
    df = clean_data(add_labels(df))
    y = df.pop("fraud")
    X_text = df.pop("description")
    X_num = df.values
    return X_text, X_num, y


if __name__ == '__main__':
    main()
