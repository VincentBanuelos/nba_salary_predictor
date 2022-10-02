import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats as st
import allplayers_wrangle as wr

# plotting defaults
plt.rc('figure', figsize=(16, 8))
plt.style.use('dark_background')
plt.rc('font', size=16)

import warnings
warnings.filterwarnings("ignore")
pd.options.display.float_format = '{:.2f}'.format

from allplayers_wrangle import wrangle_ss

train, val, test = wrangle_ss()

def fe_plot():
    shooting_stats = ['above_avg_scorer','above_avg_3ball','above_avg_ft','above_avg_ts']

    for i in shooting_stats:
        sns.boxplot(x=i, y='salary', data=train)
        plt.show()
    return

def fe_test():
    not_a_baller = train[(train.above_avg_scorer == 0)&(train.above_avg_ts == 0)].salary
    baller = train[(train.above_avg_scorer == 1)&(train.above_avg_ts == 1)].salary

    # Set alpha
    alpha = 0.05

    # Check for equal variances
    s, pval = st.levene(baller, not_a_baller)

    # Use the results from checking for equal variances to set equal_var
    t, p = st.ttest_ind(baller, not_a_baller, equal_var=(pval >= alpha))

    # Evaluate results based on the t-statistic and the p-value
    if p/2 < alpha and t > 0:
        print('''Reject the Null Hypothesis.
        
    Players with an above avg TS% and PPG DO earn a significantly different salary than then the rest of the league.''')
    else:
        print('''Fail to reject the Null Hypothesis.
        
    Players with an above avg TS% and PPG DO NOT earn a significantly different salary than then the rest of the league.''')
    return

def usg_pt_plot():
    sns.lmplot(x='usg_pct', y='salary', data=train, height=10)
    plt.show()
    return

def usg_pct_test():
    notta_floor_general = train[train.above_avg_usg_pct == 0].salary
    floor_general = train[train.above_avg_usg_pct == 1].salary

    # Set alpha
    alpha = 0.05

    # Check for equal variances
    s, pval = st.levene(floor_general, notta_floor_general)

    # Use the results from checking for equal variances to set equal_var
    t, p = st.ttest_ind(floor_general, notta_floor_general, equal_var=(pval >= alpha))

    # Evaluate results based on the t-statistic and the p-value
    if p/2 < alpha and t > 0:
        print('''Reject the Null Hypothesis.
        
    Players with an above avg USG % DO earn a significantly different salary than then the rest of the league.''')
    else:
        print('''Fail to reject the Null Hypothesis.
        
    Players with an above avg USG % DO NOT earn a significantly different salary than then the rest of the league.''')
    return

def vorp_plot():
    sns.lmplot(x='vorp', y='salary', data=train, height=10)
    plt.show()
    return

def vorp_test():
    below_avg_vorp = train[train.vorp < train.vorp.mean()].salary
    above_avg_vorp = train[train.vorp >= train.vorp.mean()].salary

    # Set alpha
    alpha = 0.05

    # Check for equal variances
    s, pval = st.levene(above_avg_vorp, below_avg_vorp)

    # Use the results from checking for equal variances to set equal_var
    t, p = st.ttest_ind(above_avg_vorp, below_avg_vorp, equal_var=(pval >= alpha))

    # Evaluate results based on the t-statistic and the p-value
    if p/2 < alpha and t > 0:
        print('''Reject the Null Hypothesis.
        
    Players with an above avg VORP DO earn a significantly different salary than then the rest of the league.''')
    else:
        print('''Fail to reject the Null Hypothesis.
        
    Players with an above avg VORP DO NOT earn a significantly different salary than then the rest of the league.''')
    return

def pos_plot():
    sns.boxplot(x='pos', y='salary', data=train)
    plt.show()
    return

def pos_test():
    centers_sal = train[train.pos == 'C'].salary
    league_avg_sal = train.salary.mean()

    # Set alpha
    alpha = 0.05

    t, p = st.ttest_1samp(centers_sal, league_avg_sal)

    # Evaluate results based on the t-statistic and the p-value
    if p/2 < alpha and t > 0:
        print('''Reject the Null Hypothesis.
        
    Centers DO make more than the league average.''')
    else:
        print('''Fail to reject the Null Hypothesis.
        
    Centers DO NOT make more than the league average.''')
    return