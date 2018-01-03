import pandas as pd


def get_data(filename):
    '''

    parameters: filename
    return: Pandas DataFrame

    '''
    return pd.read_json(filename)


if __name__ == '__main__':
    df = get_data('data/data.json')
