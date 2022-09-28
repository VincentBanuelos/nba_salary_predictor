import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#importing request to make sure url works
import requests
#using beautiful soup to web scrape data from basketball reference
from bs4 import BeautifulSoup

# The requests library can send a GET request to the 2022 spurs page
spurs_request = requests.get('https://www.basketball-reference.com/teams/SAS/2022.html')

# BeautifulSoup library parses the content of an HTML document, in this case wiz_res
spurs_soup = BeautifulSoup(spurs_request.content, 'lxml')

def get_pergame():
    # BeautifulSoup's .find() method searches for a tag and specified attributes, 
    # returning the first match 
    spurs_pergame = spurs_soup.find(name = 'table', attrs = {'id' : 'per_game'})
    # Creating a list of dictionaries to then convert into a Pandas Dataframe
    spurs_stats = []

    for row in spurs_pergame.find_all('tr')[1:]:  # Excluding the first 'tr', since that's the table's title head

        player = {}
        player['Name'] = row.find('a').text.strip()
        player['Age'] = row.find('td', {'data-stat' : 'age'}).text
        player['GP'] = row.find('td', {'data-stat' : 'g'}).text
        player['PPG'] = row.find('td', {'data-stat' : 'pts_per_g'}).text
        player['FGM'] = row.find('td', {'data-stat' : 'fg_per_g'}).text
        player['FGA'] = row.find('td', {'data-stat' : 'fga_per_g'}).text
        player['Field_Goal_PCT'] = row.find('td', {'data-stat' : 'fg_pct'}).text
        player['3PM'] = row.find('td', {'data-stat' : 'fg3_per_g'}).text
        player['3PA'] = row.find('td', {'data-stat' : 'fg3a_per_g'}).text
        player['3PT_PCT'] = row.find('td', {'data-stat' : 'fg3_pct'}).text
        player['2PM'] = row.find('td', {'data-stat' : 'fg2_per_g'}).text
        player['2PA'] = row.find('td', {'data-stat' : 'fg2a_per_g'}).text
        player['2PT_PCT'] = row.find('td', {'data-stat' : 'fg2_pct'}).text
        player['EFG_PCT'] = row.find('td', {'data-stat' : 'efg_pct'}).text
        player['FTM'] = row.find('td', {'data-stat' : 'ft_per_g'}).text
        player['FTA'] = row.find('td', {'data-stat' : 'fta_per_g'}).text
        player['FT_PCT'] = row.find('td', {'data-stat' : 'ft_pct'}).text
        player['ORB'] = row.find('td', {'data-stat' : 'orb_per_g'}).text
        player['DRB'] = row.find('td', {'data-stat' : 'drb_per_g'}).text
        player['Total_Rebounds_PG'] = row.find('td', {'data-stat' : 'trb_per_g'}).text
        player['Assists_PG'] = row.find('td', {'data-stat' : 'ast_per_g'}).text
        player['Steals_PG'] = row.find('td', {'data-stat' : 'stl_per_g'}).text
        player['Blocks_PG'] = row.find('td', {'data-stat' : 'blk_per_g'}).text
        player['Turnovers_PG'] = row.find('td', {'data-stat' : 'tov_per_g'}).text
        player['Fouls_PG'] = row.find('td', {'data-stat' : 'pf_per_g'}).text
        player['Min_PG'] = row.find('td', {'data-stat' : 'mp_per_g'}).text
        spurs_stats.append(player)

    pergamestats = pd.DataFrame(spurs_stats)

    return pergamestats.set_index('Name').sort_index(ascending=True)

def get_adv():
    spurs_adv = spurs_soup.find(name = 'table', attrs = {'id' : 'advanced'})

    # Creating a list of dictionaries to then convert into a Pandas Dataframe
    spurs_adv_stats = []

    for row in spurs_adv.find_all('tr')[1:]:  # Excluding the first 'tr', since that's the table's title head

        adv_player = {}
        adv_player['Name'] = row.find('a').text.strip()
        adv_player['PER'] = row.find('td', {'data-stat' : 'per'}).text
        adv_player['TS_PCT'] = row.find('td', {'data-stat' : 'ts_pct'}).text
        adv_player['3PAr'] = row.find('td', {'data-stat' : 'fg3a_per_fga_pct'}).text
        adv_player['FTr'] = row.find('td', {'data-stat' : 'fta_per_fga_pct'}).text
        adv_player['ORB_PCT'] = row.find('td', {'data-stat' : 'orb_pct'}).text
        adv_player['DRB_PCT'] = row.find('td', {'data-stat' : 'drb_pct'}).text
        adv_player['TRB_PCT'] = row.find('td', {'data-stat' : 'trb_pct'}).text
        adv_player['AST_PCT'] = row.find('td', {'data-stat' : 'ast_pct'}).text
        adv_player['STL_PCT'] = row.find('td', {'data-stat' : 'stl_pct'}).text
        adv_player['BLK_PCT'] = row.find('td', {'data-stat' : 'blk_pct'}).text
        adv_player['TOV_PCT'] = row.find('td', {'data-stat' : 'tov_pct'}).text
        adv_player['USG_PCT'] = row.find('td', {'data-stat' : 'usg_pct'}).text
        adv_player['OWS'] = row.find('td', {'data-stat' : 'ows'}).text
        adv_player['DWS'] = row.find('td', {'data-stat' : 'dws'}).text
        adv_player['WS'] = row.find('td', {'data-stat' : 'ws'}).text
        adv_player['OBPM'] = row.find('td', {'data-stat' : 'obpm'}).text
        adv_player['DBPM'] = row.find('td', {'data-stat' : 'dbpm'}).text
        adv_player['BPM'] = row.find('td', {'data-stat' : 'bpm'}).text
        adv_player['VORP'] = row.find('td', {'data-stat' : 'vorp'}).text


        spurs_adv_stats.append(adv_player)

    advstats = pd.DataFrame(spurs_adv_stats)
    return advstats.set_index('Name').sort_index(ascending=True)


def get_salaries():
# Was unable to webscrape salaries so i pulled the data into a csv and used pandas to convert to dataframe
# salaries = spurs_soup.find(name = 'table', attrs = {'id' : 'salaries2'})

    salaries = pd.read_csv('salaries - Sheet1.csv')
    return salaries.set_index('Name').sort_index(ascending=True)

def spurs_acquire():
    pergamestats = get_pergame()
    advstats = get_adv()
    salaries = get_salaries()
    spurs_df = pd.concat([pergamestats, advstats, salaries], axis=1)
    return spurs_df

def prep_spurs():
    spurs_df = spurs_acquire()

    # Since Anthony lamb does not have any statistical data i will go ahead and drop him from the dataframe.
    spurs_df.drop(spurs_df.head(1).index,inplace=True)

    spurs_df.Salary =  spurs_df.Salary.str.strip('$').str.replace(",","").astype('float')

    numerical_columns = ['PPG', 'FGM', 'FGA', 'Field_Goal_PCT', '3PM', '3PA',
       '3PT_PCT', '2PM', '2PA', '2PT_PCT', 'EFG_PCT', 'FTM', 'FTA', 'FT_PCT',
       'ORB', 'DRB', 'Total_Rebounds_PG', 'Assists_PG', 'Steals_PG',
       'Blocks_PG', 'Turnovers_PG', 'Fouls_PG', 'Min_PG', 'PER', 'TS_PCT',
       '3PAr', 'FTr', 'ORB_PCT', 'DRB_PCT', 'TRB_PCT', 'AST_PCT', 'STL_PCT',
       'BLK_PCT', 'TOV_PCT', 'USG_PCT', 'OWS', 'DWS', 'WS', 'OBPM', 'DBPM',
       'BPM', 'VORP']

    for col in numerical_columns:
       spurs_df[col] = pd.to_numeric(spurs_df[col])

    # Filling in the nulls with 0 since all columns that are null indicate a player has not done anything to fill that column
    spurs_df = spurs_df.fillna(0)

    # Encoding positions to assist wiht modeling
    dummies = pd.get_dummies(spurs_df['Pos'],drop_first=False,dtype=float)
    spurs_df = pd.concat([spurs_df, dummies], axis=1)

    # Changing all columns to lower case
    spurs_df.columns = [col.lower() for col in spurs_df.columns]

    # Feature Engineering some features that will account for whether a player is above or below league average in features i deem important to a player's value salary wise
    spurs_df['above_avg_scorer'] = spurs_df['ppg'] >= 15
    spurs_df['above_avg_scorer'] = spurs_df['above_avg_scorer'].astype(int)

    spurs_df['above_avg_3ball'] = spurs_df['3pt_pct'] >= .354
    spurs_df['above_avg_3ball'] = spurs_df['above_avg_3ball'].astype(int)

    spurs_df['above_avg_ft'] = spurs_df.ft_pct >= .775
    spurs_df['above_avg_ft'] = spurs_df['above_avg_ft'].astype(int)

    spurs_df['above_avg_ts'] = spurs_df.ft_pct >= .566
    spurs_df['above_avg_ts'] = spurs_df['above_avg_ts'].astype(int)

    return spurs_df



