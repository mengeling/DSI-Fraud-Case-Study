import sys
sys.path.append('..')
from model.pipeline import clean_numeric_data




if __name__ == '__main__':
    df = clean_numeric_data('../data/data.json')
    df = clean_data(df)
