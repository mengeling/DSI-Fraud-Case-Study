import pandas as pd
from bs4 import BeautifulSoup


def get_text_data(txt):
    return BeautifulSoup(txt).text


def get_numeric_data(df):
    df["fraud"] = (df["acct_type"] != "premium").astype(int)
    df["total_payout"] = df["ticket_types"].apply(unpack)
    df["listed"] = df["listed"].map({'y': 1, 'n': 0})
    cols = [
        "description", "country", "email_domain", "ticket_types", "venue_address", "venue_country",
        "venue_latitude", "has_header", "venue_longitude", "venue_name", "venue_state", "name", "object_id",
        "org_desc", "org_facebook", "org_twitter", "org_name", "payee_name", "previous_payouts", "acct_type"
    ]
    df.drop(cols, axis=1, inplace=True)
    df.dropna(inplace=True)
    return pd.get_dummies(df)


def unpack(ticket_types_lst):
    return sum(d['quantity_sold'] * d['cost'] for d in ticket_types_lst)


def main():
    df = pd.read_json('../data/data.json')
    X_text = df["description"].apply(get_text_data).values
    df = get_numeric_data(df)
    y = df.pop('fraud').values
    return X_text, df.values, y


if __name__ == '__main__':
    main()
