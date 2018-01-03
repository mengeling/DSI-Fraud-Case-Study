import pandas as pd


def get_data(filename):
    '''

    parameters: filename
    return: Pandas DataFrame

    '''
    return pd.read_json(filename)


def clean_numerical_data(df):
    df["fraud"] = (df["acct_type"] != "premium").astype(int)
    cols = ["country", "description", "email_domain", "ticket_types", "venue_address", "venue_country", "venue_latitude",
             "has_header", "venue_longitude", "venue_name", "venue_state", "name", "object_id", "org_desc",
             "org_facebook", "org_twitter", "org_name", "payee_name", "previous_payouts", "acct_type"]
    df.drop(cols, axis=1, inplace=True)
    df["listed"] = df["listed"].map({'y': 1, 'n': 0})
    df.dropna(inplace=True)
    return pd.get_dummies(df)


def clean_text_data(df):



if __name__ == '__main__':
    df = get_data('../data/data.json')
    numerical_df = clean_numerical_data(df)
    text_df = clean_text_data(df)
