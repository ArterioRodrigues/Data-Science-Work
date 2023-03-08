"""
Name:  Arterio Rodrigues
Email: arterio.rodrigues47@myhunter.cuny.edu
Resources:  Python3.8 Pandas
"""

import pandas as pd
import numpy as np
from datetime import datetime, date, time, timezone 

def date_to_month(str_data, str_type = 'month'):
    '''
    A function that takes a string an return its month
    '''
    if str_type == 'month':
        return str_data.split('-')[1]

    return str_data.split('-')[0].lower()

def parse_datetime(df, column='DATE'):
    '''
    This function takes two inputs:
    df: a DataFrame containing the column column.
    column: the name of a column. column has default value of 'DATE'.
    The function should return a DataFrame with three additional columns:
    timestamp: contains the datetime object corresponding to the string stored in column.
    month: return the number corresponding to the month of timestamp: 1 for January, 2 
    for February, 12 for December. year: return the number corresponding to year of timestamp.
    Note this is very similar, but not identical to the parse_datetime from the DS 100: 
    Section 9.4 or Program 4.
    '''
    df['timestamp'] = df[column]
    df['month'] = df[column].apply(date_to_month, str_type = 'month')
    df['year'] = df[column].apply(date_to_month, str_type = 'year')

    return df

def compute_lin_reg(xes, yes):
    '''
    This function takes two inputs:
    xes: an iterables of numeric values representing the independent variable
    yes: an iterables of numeric values representing the dependent variable
    The function computes the slope and y-intercept of the linear regression line, using ordinary
    least squares (see DS 8: Chapter 15 for detailed explanation). The pseudocode for this:
    Compute the standard deviation of the xes and yes. Call these sd_x and sd_y.
    Compute the correlation, r, of the xes and yes.
    Compute the slope, theta_1, as theta_1 = r*sd_y/sd_x.
    Compute the y-intercept, theta_0, as theta_0 = average(yes) - theta_1 * average(xes)
    Return theta_0 and theta_1.
    '''
    sd_x = xes.std()
    sd_y = yes.std()

    r_corr = np.corrcoef(sd_x, sd_y)

    theta_1 = r_corr * sd_y/sd_x
    theta_0 =(sum(yes)/len(yes)) - (theta_1 * (sum(xes)/len(xes)))

    return theta_0, theta_1

def predict(xes, theta_0, theta_1):
    '''
    This function takes three inputs:
    xes: an iterables of numeric values representing the independent variable
    theta_0: the y-intercept of the linear regression model
    theta_1: the slope of the linear regression model
    The function returns the predicted values of the dependent variable, xes, under the linear 
        regression model with y-intercept theta_0 and slope theta_1.
    '''
    predictions = []
    for value in xes:
        predictions.append((theta_1 * value) + theta_0)

    return predictions

def mse_loss(y_actual,y_estimate):
    '''
    This function takes two inputs:
        y_actual: a Series containing numeric values.
        y_estimate: a Series containing numeric values.
    The series are of the same length and contain numeric values only 
    (all null and non-numeric values have been dropped).The function returns the mean
    square error loss function between y_actual and y_estimate (e.g. the mean of the 
    squares of the differences). 
    Note: this function was part of an earlier homework (Program 3) as well as in the 
    textbook. It is included here to be used as a default argument for the error 
    computation function below.
    '''
    return 0


def rmse_loss(y_actual,y_estimate):
    '''
    This function takes two inputs:
        y_actual: a Series containing numeric values.
        y_estimate: a Series containing numeric values.
    The series are of the same length and contain numeric values only (all null and non-numeric 
    valueshave been dropped). The function returns the square root of the mean square error 
    loss function between y_actual and y_estimate (e.g. the square root of the mean of the 
    squares of the differences).
    '''
    return 0



def compute_error(y_actual,y_estimate,loss_fnc=mse_loss): 
    '''
    This function takes three inputs:
        y_actual: a Series containing numeric values.
        y_estimate: a Series containing numeric values.
        loss_fnc: function that takes two numeric series as input parameters and returns a 
    numeric value. It has a default value of mse_loss.
    The series are of the same length and contain numeric values only (all null and non-numeric 
    values have been dropped). The result of computing the loss_fnc on the inputs y_actual 
    and y_estimate is returned.
    '''
    return loss_fnc(y_actual, y_estimate)

def compute_ytd(df):
    '''
    This function takes one input:
        df: a DataFrame containing columns month, year and USINFO.
    The function returns a Series with the number of jobs since the beginning of the year for that 
    entry. For example, for the January 2022 row, the number would be 0 since January is the 
    beginning of the year. For July 2022, the number be the difference between USINFO for July and 
    USINFO for January.
    '''
    
    '''
    compute_year_over_year(df): This function takes one input:
    df: a DataFrame containing columns month, year and USINFO.
    Computes and returns a Series with the percent change from the previous year for USINFO. You can assume that the DataFrame is ordered by date, with earlier dates coming first in the DataFrame. 
    Note: you may find the df.pct_change function useful for computing the change from the previous year.
    '''