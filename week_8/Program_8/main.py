from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LassoCV, RidgeCV, LinearRegression, LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

import pickle
import pandas as pd
import numpy as np


from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification


def clean_reg(reg):

    if reg == 'PAS' or reg == 'COM':
        return reg
    else: 
        return 'OTHER'
    
def clean_color(col):

    if col in ['GY', 'GRAY', 'GREY', 'SILVE', 'SIL', 'SL']:
        col = 'GRAY'
    elif col in ['WH', 'WHITE']:
        col = 'WHITE'
    elif col in ['BK', 'BLACK', 'BL']:
        col = 'BLACK'
    elif col == 'BLUE':
        col = 'BLUE'
    elif col in ['RED', 'RD']:
        col = 'RED'
    elif col in ['GR', 'GREEN']:
        col = 'GREEN'
    elif col in ['BROWN', 'TAN']:
        col = 'BROWN'
    else:
        col = 'OTHER'

    return col

def add_indicators(df, cols = ['Registration', 'Color', 'State']):
    df_dummies =  pd.get_dummies(df[cols], drop_first = True)
    df = pd.concat([df, df_dummies])

    return df
def add_excessive_flag(df, threshold = 5):
    df['Excessive Tickets'] = 0

    for index, row in df.iterrows():
        if row['Tickets'] < threshold:
            df.loc[index, 'Excessive Tickets'] = 0
        else: 
            df.loc[index, 'Excessive Tickets'] = 1
    
    return df

def split_data(df, x_cols, y_col, test_size = 0.25, random_state = 2023):
    '''
    This function takes 4 input parameters:
    df: a DataFrame containing with a columns units.
    y_col_name: the name of the column of the dependent variable.
    test_size: accepts a float between 0 and 1 and represents the proportion of the data set 
    to use for training. This parameter has a default value of 0.25.
    random_state: Used as a seed to the randomization. This parameter has a default value of 
    1870.
    Returns the data split into 4 subsets, corresponding to those returned by train_
    test_split: x_train, x_test, y_train, and y_test. where units is the "x" column and 
    the input parameter, y_col_name is the "y" column.
    Note: this is function is very similar to the splitting of data into training and 
    testing sets from Program 6.
    '''
    x_train, y_train, x_test , y_test = train_test_split(
    df['units'], df[y_col], test_size = test_size, random_state = random_state)

    return x_train, y_train, x_test , y_test

def fit_model(x_train, y_train, model_type = 'logreg'):
    if model_type == 'logreg':
        clf = LogisticRegression(solver = 'saga', penalty = '12', max_iter = 5000).fit(x_train, y_train)
    elif model_type == 'nbayes':
        clf = GaussianNB().fit(x_train, y_train)
    elif model_type == 'svm':
        clf = make_pipeline(StandardScaler(), SVC(kernel = 'rbf'))
        clf = clf.fit(x_train, y_train)
    elif model_type == 'rforest':
        clf = RandomForestClassifier(n_estimators = 100, random_state=0).fit(x_train, y_train)
    
    return clf


