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

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import r2_score, mean_squared_error, explained_variance_score
from sklearn.linear_model import LinearRegression, LassoLars, TweedieRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE, SelectKBest, f_regression

import warnings
warnings.filterwarnings("ignore")
pd.options.display.float_format = '{:.2f}'.format

from allplayers_wrangle import wrangle_ss

train, val, test = wrangle_ss()


def min_max_scale(x_train, x_val, x_test):
    """
    this function takes in 3 dataframes with the same columns,
    a list of numeric column names (because the scaler can only work with numeric columns),
    and fits a min-max scaler to the first dataframe and transforms all
    3 dataframes using that scaler.
    it returns 3 dataframes with the same column names and scaled values.
    """
    # create the scaler object and fit it to x_train (i.e. identify min and max)
    # if copy = false, inplace row normalization happens and avoids a copy (if the input is already a numpy array).

    scaler = MinMaxScaler(copy=True).fit(x_train)

    xtrains = pd.DataFrame(scaler.transform(x_train), columns = x_train.columns).set_index([x_train.index])
    xvals = pd.DataFrame(scaler.transform(x_val), columns = x_val.columns).set_index([x_val.index])
    xtests = pd.DataFrame(scaler.transform(x_test), columns = x_test.columns).set_index([x_test.index])

    # scale x_train, x_val, x_test using the mins and maxes stored in the scaler derived from x_train.
    

    return xtrains, xvals, xtests


# Dropping salary and position from dataset, salary is target variable and position has been one hot encoded

x_train = train.drop(columns=['salary','pos'])
y_train = train.salary

x_val = val.drop(columns=['salary','pos'])
y_val = val.salary

x_test = test.drop(columns=['salary','pos'])
y_test = test.salary

y_train = pd.DataFrame(y_train)
y_val = pd.DataFrame(y_val)
y_test = pd.DataFrame(y_test)

# Scaling data to use for moedling
xtrains, xvals, xtests = min_max_scale(x_train, x_val, x_test)

# Going to use features I investigated along with age and winshare, as domain knowledges 
# suggests that the age of a player as well as a players contribution to winning affect their salary
# As well as using common statistics tha many causal fans find useful in player comparison
xtrains = xtrains[['ppg','ft_pct','usg_pct','vorp','ts_pct','age','ws','ast', 'stl', 'blk', 'tov', 'pf']]
xvals = xvals[['ppg','ft_pct','usg_pct','vorp','ts_pct','age','ws','ast', 'stl', 'blk', 'tov', 'pf']]
xtests = xtests[['ppg','ft_pct','usg_pct','vorp','ts_pct','age','ws','ast', 'stl', 'blk', 'tov', 'pf']]

def model_eval():
    pred_mean = y_train.salary.mean()
    y_train['pred_mean'] = pred_mean
    y_val['pred_mean'] = pred_mean
    rmse_train = mean_squared_error(y_train.salary, y_train.pred_mean, squared=False)
    rmse_validate = mean_squared_error(y_val.salary, y_val.pred_mean, squared=False)


    # save the results
    metric_df = pd.DataFrame(data=[{
        'model': 'baseline_mean',
        'rmse_train': rmse_train,
        'r2_train': explained_variance_score(y_train.salary, y_train.pred_mean),
        'rmse_validate': rmse_validate,
        'r2_validate': explained_variance_score(y_val.salary, y_val.pred_mean)
        }])

    # LassoLars Model
    lars = LassoLars(alpha=2)
    lars.fit(xtrains, y_train.salary)
    y_train['pred_lars'] = lars.predict(xtrains)
    rmse_train = mean_squared_error(y_train.salary, y_train.pred_lars, squared=False)
    y_val['pred_lars'] = lars.predict(xvals)
    rmse_validate = mean_squared_error(y_val.salary, y_val.pred_lars, squared=False)

    # save the results
    metric_df = metric_df.append({
        'model': 'LarsLasso, alpha 3',
        'rmse_train': rmse_train,
        'r2_train': explained_variance_score(y_train.salary, y_train.pred_lars),
        'rmse_validate': rmse_validate,
        'r2_validate': explained_variance_score(y_val.salary, y_val.pred_lars)}, ignore_index=True)

    # create the model object
    glm = TweedieRegressor(power=1, alpha=0)
    glm.fit(xtrains, y_train.salary)
    y_train['glm_pred'] = glm.predict(xtrains)
    rmse_train = mean_squared_error(y_train.salary, y_train.glm_pred)**(1/2)
    y_val['glm_pred'] = glm.predict(xvals)
    rmse_validate = mean_squared_error(y_val.salary, y_val.glm_pred)**(1/2)


    # save the results
    metric_df = metric_df.append({
        'model': 'Tweedie Regressor',
        'rmse_train': rmse_train,
        'r2_train': explained_variance_score(y_train.salary, y_train.glm_pred),
        'rmse_validate': rmse_validate,
        'r2_validate': explained_variance_score(y_val.salary, y_val.glm_pred)}, ignore_index=True)


    # create the model object
    pf = PolynomialFeatures(degree=2)
    X_train_degree2 = pf.fit_transform(xtrains)
    X_validate_degree2 = pf.transform(xvals)
    lm = LinearRegression()
    lm.fit(X_train_degree2, y_train.salary)
    y_train['salary_pred_pf'] = lm.predict(X_train_degree2)
    rmse_train = mean_squared_error(y_train.salary, y_train.salary_pred_pf)**(1/2)
    y_val['salary_pred_pf'] = lm.predict(X_validate_degree2)
    rmse_validate = mean_squared_error(y_val.salary, y_val.salary_pred_pf)**(1/2)


    # save the results
    metric_df = metric_df.append({
        'model': 'Polynomial Features, D2',
        'rmse_train': rmse_train,
        'r2_train': explained_variance_score(y_train.salary, y_train.salary_pred_pf),
        'rmse_validate': rmse_validate,
        'r2_validate': explained_variance_score(y_val.salary, y_val.salary_pred_pf)}, ignore_index=True)


    # create the model object
    pf = PolynomialFeatures(degree=3)
    X_train_degree2 = pf.fit_transform(xtrains)
    X_validate_degree2 = pf.transform(xvals)
    lm = LinearRegression()
    lm.fit(X_train_degree2, y_train.salary)
    y_train['salary_pred_pf'] = lm.predict(X_train_degree2)
    rmse_train = mean_squared_error(y_train.salary, y_train.salary_pred_pf)**(1/2)
    y_val['salary_pred_pf'] = lm.predict(X_validate_degree2)
    rmse_validate = mean_squared_error(y_val.salary, y_val.salary_pred_pf)**(1/2)


    # save the results
    metric_df = metric_df.append({
        'model': 'Polynomial Features, D3',
        'rmse_train': rmse_train,
        'r2_train': explained_variance_score(y_train.salary, y_train.salary_pred_pf),
        'rmse_validate': rmse_validate,
        'r2_validate': explained_variance_score(y_val.salary, y_val.salary_pred_pf)}, ignore_index=True)
        
    return metric_df

def final_model_test():

    #baseline model
    pred_mean = y_train.salary.mean()
    y_train['pred_mean'] = pred_mean
    y_val['pred_mean'] = pred_mean
    y_test['pred_mean'] = pred_mean
    base_rmse_train = mean_squared_error(y_train.salary, y_train.pred_mean, squared=False)
    base_rmse_validate = mean_squared_error(y_val.salary, y_val.pred_mean, squared=False)
    base_rmse_test = mean_squared_error(y_test.salary, y_test.pred_mean, squared=False)

    # create the model object
    glm = TweedieRegressor(power=1, alpha=0)
    glm.fit(xtrains, y_train.salary)
    y_train['glm_pred'] = glm.predict(xtrains)
    rmse_train = mean_squared_error(y_train.salary, y_train.glm_pred)**(1/2)
    y_val['glm_pred'] = glm.predict(xvals)
    rmse_validate = mean_squared_error(y_val.salary, y_val.glm_pred)**(1/2)
    y_test['glm_pred'] = glm.predict(xtests)
    rmse_test = mean_squared_error(y_test.salary, y_test.glm_pred, squared=False)

    test_metrics = pd.DataFrame({'baseline': 
                                {'rmse': base_rmse_train, 
                                'r2': explained_variance_score(y_train.salary, y_train.glm_pred)},
        
                            'train': 
                                {'rmse': rmse_train, 
                                'r2': explained_variance_score(y_train.salary, y_train.glm_pred)},
                            'validate': 
                                {'rmse': rmse_validate, 
                                'r2': explained_variance_score(y_val.salary, y_val.glm_pred)},
                            'test': 
                                {'rmse': rmse_test, 
                                'r2': explained_variance_score(y_test.salary, y_test.glm_pred)}
                                })

    return test_metrics.T