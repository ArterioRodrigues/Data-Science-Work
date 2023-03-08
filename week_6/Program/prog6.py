"""
Name:  Arterio Rodrigues
Email: arterio.rodrigues47@myhunter.cuny.edu
Resources:  Python3.8 Pandas
"""

import pandas as pd
from datetime import datetime

def import_data(file_name): 
    '''
        This function takes as one input parameter:
        file_name: the name of a CSV file containing Yellow Taxi Trip Data from OpenData NYC.
        The data in the file is read into a DataFrame, and
        the columns: VendorID,RatecodeID,store_and_fwd_flag,payment_type,extra,mta_tax,tolls_amount,improvement_surcharge,congestion_surcharge are dropped.
        Any rows with non-positive total_amount are dropped.
        The resulting DataFrame is returned.
    '''
    df = pd.read_csv(file_name)
    column = [ "VendorID", "RatecodeID", "store_and_fwd_flag" , "payment_type", "extra", "mta_tax", "tolls_amount", "improvement_surcharge", "congestion_surcharge"]

    df = df.drop(columns = column)
    
    for index, row in df.iterrows():
        if float(row["total_amount"]) <= 0:
            df = df.drop(index, axis = 0)

    return df

def add_tip_time_features(df): 

    '''
        This function takes one input:
        df: a DataFrame containing Yellow Taxi Trip Data from OpenData NYC.
        The function computes 3 new columns:
        percent_tip: which is 100*tip_amount/(total_amount-tip_amount)
        duration: the time the trip took in seconds.
        dayofweek: the day of the week that the trip started, represented as 0 for Monday, 1 for Tuesday, ... 6 for Sunday.
        The original DataFrame with these additional three columns is returned.
    '''
    df["percent_tip"] = 100 * df["tip_amount"].astype(float)/(df["total_amount"].astype(float) - df["tip_amount"].astype(float))

    dropoff = pd.to_datetime(df["tpep_dropoff_datetime"])
    pickup = pd.to_datetime(df["tpep_pickup_datetime"])

    df["duration"] = dropoff - pickup
    df["duration"] = df["duration"].apply(lambda dura:  dura.total_seconds())

    df["dayofweek"] = pickup.apply(datetime.weekday)

    return df

def impute_numeric_cols(df): 
    
    '''
    This function takes one input:
    df: a DataFrame containing Yellow Taxi Trip Data from OpenData NYC.
    Missing data in the numeric columns passenger_count,trip_distance,fare_amount,tip_amount,total_amount,duration,dayofweek are replaced with the median of the respective column. 
    Returns the resulting DataFrame.
    '''
    columns = ["passenger_count", "trip_distance", "fare_amount","tip_amount","total_amount", "duration", "dayofweek"]

    for column in columns:
        df[column] = df[column].fillna(df[column].median())


    return df

def add_boro(df, file_name) -> pd.DataFrame: 
    
    '''
        This function takes as two input parameters:
        df: a DataFrame containing Yellow Taxi Trip Data from OpenData NYC.
        file_name: the name of a CSV file containing NYC Taxi Zones from OpenData NYC.
        Makes a DataFrame, using file_name, to add pick up and drop off boroughs to df. In particular, adds two new columns to the df:
        PU_borough that contain the borough corresponding to the pick up taxi zone ID (stored in PULocationID), and
        DO_borough that contain the borough corresponding to the drop off taxi zone (stored in DOLocationID)
        Returns df with these two additional columns (PU_borough and DO_borough).
    '''
    df_file = pd.read_csv(file_name, index_col=False)

    location_id = {}

    for index, row in df_file.iterrows():
        location_id[row['LocationID']] = row["borough"]

    for index, row in df.iterrows():
        
        df.loc[index, "PU_borough"] = location_id.get(int(row['PULocationID']), float("nan"))
        df.loc[index, "DO_borough"] = location_id.get(int(row['DOLocationID']), float("nan"))

    return df.reset_index()

def encode_categorical_col(col,prefix): 

    '''
        This function takes two input parameters:
        col: a column of categorical data.
        prefix: a prefix to use for the labels of the resulting columns.
        Takes a column of categorical data and uses categorical encoding to 
        create a new DataFrame with the k-1 columns, where k is the number of 
        different nomial values for the column. Your function should create k columns, 
        one for each value, labels by the prefix concatenated with the value. The columns 
        should be sorted and the DataFrame restricted to the first k-1 columns returned.       
        For example, if the column contains values: 'Bronx', 'Brooklyn', 'Manhattan', 'Queens', and 'Staten Island', 
        and the prefix parameter has the value 'PU_' (and set the separators to be the empty string: prefix_sep=''), 
        then the resulting columns would be labeled: 'PU_Bronx', 'PU_Brooklyn', 'PU_Manhattan', 'PU_Queens', and 'PU_Staten Island'. 
        The last one alphabetically is dropped (in this example, 'PU_Staten Island'), and the DataFrame restricted to the first k-1 columns is returned. 
    '''
    new_coloumns_dict = {}
    col_to_drop = col[0]
    for _, value in col.items():
        new_coloumns_dict[prefix + str(value)] = [0 for i in range(len(col))]
        if col_to_drop < value:
            col_to_drop = value

    df = pd.DataFrame(new_coloumns_dict)

    for index, value in col.items():
        df.loc[index, prefix + str(value)] = "1"

    df = df.drop(prefix + col_to_drop, axis = 1)  
    df = df.reindex(sorted(df.columns), axis=1)
    return df
    