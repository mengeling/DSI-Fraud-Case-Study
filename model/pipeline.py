import pandas as pd
from bs4 import BeautifulSoup


def add_labels(df):
    df["fraud"] = (df["acct_type"] != "premium").astype(int)
    return df.drop("acct_type", axis=1)


def strip_html(txt):
    return BeautifulSoup(txt, "lxml").text


def unpack(ticket_types_lst):
    return sum(d['quantity_sold'] * d['cost'] for d in ticket_types_lst)


def clean_data(df):
    df["total_payout"] = df["ticket_types"].apply(unpack)
    # df["listed"] = df["listed"].map({'y': 1, 'n': 0})
    df["description"] = df["description"].apply(strip_html)
    #cols = ["sale_duration2", "user_age", "payout_type", "total_payout", "body_length", "description", "fraud"]
    #     "country", "email_domain", "ticket_types", "venue_address", "venue_country",
    #     "venue_latitude", "has_header", "venue_longitude", "venue_name", "venue_state", "name", "object_id",
    #     "org_desc", "org_facebook", "org_twitter", "org_name", "payee_name", "previous_payouts"
    # ]
    # df.drop(cols, axis=1, inplace=True)
    #df = df[cols]
    df.drop("ticket_types", axis=1, inplace=True)
    df.dropna(inplace=True)
    return df


def main():
    df = pd.read_json('../data/data.json')
    df = df[["sale_duration2", "user_age", "body_length", "description", "acct_type", "ticket_types"]]
    df = clean_data(add_labels(df))
    y = df.pop("fraud")
    X_text = df.pop("description")
    X_num = df.values
    #print(y)
    return X_text, X_num, y


if __name__ == '__main__':
    main()
