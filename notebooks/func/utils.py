# -*- coding: utf-8 -*-
import pandas as pd

def read_data():
    return pd.read_csv('../data/raw_data/tweet-sentiment-extraction/train.csv')

def save_processed_csv(df, folder, filename):
    df.to_csv(f'../data/processed_data/{folder}/{filename}.csv', index=False)
    return None