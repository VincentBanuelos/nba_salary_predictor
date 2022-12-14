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

def get_advstats():
    advstats = pd.read_csv('advstats.csv')
    return advstats.set_index('Player').sort_index(ascending=True)

def prepare_ss():
    '''
    Using our best performing model, returna dataframe that shows how the model
    performed on all 3 samples of data as well as how the baseline model compares.
    '''
    stats = get_players_stats()
    salaries = get_salaries()
    advstats = get_advstats()

    # Combining stats and adv stats
    stats = stats.merge(advstats, how = 'outer', left_on = ['Player'],right_on = ['Player'])

    # Feature Engineering feature's i think will assit in providing accurate model.
    stats['above_avg_scorer'] = stats['PPG'] >= 16.15
    stats['above_avg_scorer'] = stats['above_avg_scorer'].astype(int)

    stats['above_avg_3ball'] = stats['3P_PCT'] >= .362
    stats['above_avg_3ball'] = stats['above_avg_3ball'].astype(int)

    stats['above_avg_ft'] = stats.FT_PCT >= .767
    stats['above_avg_ft'] = stats['above_avg_ft'].astype(int)

    stats['above_avg_ts'] = stats.TS_PCT >= .556
    stats['above_avg_ts'] = stats['above_avg_ts'].astype(int)

    stats['above_avg_usg_pct'] = stats.USG_PCT >= stats.USG_PCT.mean()
    stats['above_avg_usg_pct'] = stats['above_avg_usg_pct'].astype(int)

    #Combining all stats and salaries.
    ss = stats.merge(salaries, how = 'outer', left_on = ['Player'],right_on = ['Player'])
    # Changing all columns to lower case
    ss.columns = [col.lower() for col in ss.columns]
    # Replacing dual position players to guard, wings, big men.
    ss.replace({'F-C': 'F', 'C-F': 'C', 'G-F': 'G', 'F-G': 'F'},inplace=True)

    dummies = pd.get_dummies(ss['pos'],drop_first=False,dtype=float)
    ss = pd.concat([ss, dummies], axis=1)
    # Dropping rk column which was basketbal refernce's index as well as player's team
    ss.drop(columns=['rk','team'],inplace=True)
    # Dropping nulls for players with incomplete stats or no salary.
    ss = ss.dropna()
    return ss

def my_split(df):
    '''
    Splitting the dataframe into 3 seperate samples to prevent data leakage
    '''

    train_validate, test = train_test_split(df, test_size=.2, random_state=123)
    train, val = train_test_split(train_validate, test_size=.3, random_state=123)
    return train, val, test

def wrangle_ss():
    '''
    Splitting dataset into three sub datasets to prevent data leakage.
    '''
    ss = prepare_ss()
    train, val, test = my_split(ss)

    return train, val, test