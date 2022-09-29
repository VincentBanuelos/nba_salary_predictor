import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


def get_players_stats():
    stats = pd.read_csv('stats.csv')
    return stats.set_index('Player').sort_index(ascending=True)

def get_salaries():
    salaries = pd.read_csv('NBA_season1718_salary.csv')
    salaries.drop(columns=['Unnamed: 0','Tm'],inplace=True)
    salaries.rename(columns = {'season17_18' : 'salary'},inplace=True)
    return salaries.set_index('Player').sort_index(ascending=True)



def prepare_ss():
    stats = get_players_stats()
    salaries = get_salaries()
    ss = stats.merge(salaries, how = 'outer', left_on = ['Player'],right_on = ['Player'])
    # Changing all columns to lower case
    ss.columns = [col.lower() for col in ss.columns]
    # Replacing dual position players to guard, wings, big men.
    ss.replace({'F-C': 'F', 'C-F': 'C', 'G-F': 'G', 'F-G': 'F'},inplace=True)
    # Dropping nulls for players with incomplete stats or no salary.
    ss = ss.dropna()

    ss['above_avg_scorer'] = ss['ppg'] >= 16.15
    ss['above_avg_scorer'] = ss['above_avg_scorer'].astype(int)

    ss['above_avg_3ball'] = ss['3p_pct'] >= .362
    ss['above_avg_3ball'] = ss['above_avg_3ball'].astype(int)

    ss['above_avg_ft'] = ss.ft_pct >= .767
    ss['above_avg_ft'] = ss['above_avg_ft'].astype(int)

    ss['above_avg_ts'] = ss.ts_pct >= .556
    ss['above_avg_ts'] = ss['above_avg_ts'].astype(int)
    return ss

def my_split(df):
    '''
    Splitting the dataframe into 3 seperate samples to prevent data leakage
    '''

    train_validate, test = train_test_split(df, test_size=.2, random_state=123)
    train, val = train_test_split(train_validate, test_size=.3, random_state=123)
    return train, val, test

def wrangle_ss():
    ss = prepare_ss()
    train, val, test = my_split(ss)

    return train, val, test