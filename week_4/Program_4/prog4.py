"""
Name:  Arterio Rodrigues
Email: arterio.rodrigues47@myhunter.cuny.edu
Resources:  Python3.8 Pandas
"""

import pandas as pd

def make_dog_df(license_file,zipcode_file):
    '''
    This function takes two inputs:
    license_file: the name of a CSV file containing NYC Dog Licensing Data from OpenData NYC, and
    zipcode_file: the name of a CSV file containing BetaNYC's NYC Zip Codes by Borough.
    The function opens the two inputted files, the first with the dog licensing information,
    and the second with zipcodes by boroughs. The function should do the following:
    The names of the dogs AnimalName should be capitalized.
    The columns, 'LicenseExpiredDate', 'Extract Year' should be dropped.
    The two DataFrames should be (left) merged on zipcodes.
    Any reported dogs not in NYC (i.e. have NaN for Borough in
    the combined DataFrame) should be dropped.
    The resulting DataFrame, with 7 columns, is returned.
    '''

    license_df = pd.read_csv(license_file)
    zipcode_df = pd.read_csv(zipcode_file)

    license_df["AnimalName"] = license_df["AnimalName"].apply(lambda name: str(name).capitalize())
    license_df = license_df.drop(['LicenseExpiredDate', 'Extract Year'], axis = 1)

    zipcode_df = zipcode_df.rename(columns = {"zip": "ZipCode"})
    new_df = pd.merge(license_df, zipcode_df, how='left', on='ZipCode')

    new_df = new_df.dropna()
    new_df = new_df.drop(['post_office','neighborhood', 'population', 'density'], axis = 1)
    new_df = new_df.rename(columns = {"borough" : 'Borough'})

    return new_df
def make_bite_df(file_name):
    '''
    This function takes one input:
    file_name: the name of a CSV file containing DOHMH Dog Bite Data from OpenData NYC.
    The function should open the file file_name as DataFrame, dropping the Species column.
    The resulting DataFrame is returned.
    '''
    bite_df = pd.read_csv(file_name)

    return bite_df.drop(['Species'], axis = 1)

def clean_age(age_str):
    '''
    This function takes one input:
    age_str: a string containing the age of the dog.
    Your function should: If age_str ends in a Y, return the rest of the string as a number.
    For example, 3Y represents 3 years and the return value is 3. If age_str ends in a M,
    return the rest of the string as a number in years. For example, 6M represents 6 months
    and the return value is 0.5. If age_str contains only a number, return it as a number.
    For example, 3 represents 3 years and the return value is 3.
    For all other values, return None.
    '''
    if age_str[-1] == 'Y':
        return float(age_str[:-1])
    elif age_str[-1] == 'M':
        return float(age_str[:-1])/12
    elif age_str.isdigit():
        return float(age_str)

    return None

def clean_breed(breed_str):
    '''
    This function takes one input:
    breed_str: a string containing the breed of the dog.
    Your function should return:
    If breed_str is empty, return "Unknown".
    Otherwise, return the string in title format with each word in the string capitalized and
    all other letters lower case. For example, If the input is BEAGLE MIXED, you should return
    Beagle Mixed.
    '''
    if not len(breed_str) > 0:
        return str(breed_str).title()

    return "Unknown"

def impute_age(df):
    '''
    This function takes one input:
    df: a DataFrame containing the column Age Num.
    Your function should replace any missing values in the df['Age Num'] column with the median
    of the values of the column. The resulting DataFrame is returned.
    '''
    median= df['Age Num'].median()
    df['Age Num'] = df['Age Num'].fillna(median)

    return df

def impute_zip(boro, zipcode):
    '''
    This function takes two inputs:
    boro: a non-empty string containing the borough.
    zipcode: a possibly empty string containing the zip code.
    If the zipcode column is empty, impute the value with the zip code of the general delivery post
    office based on value of boro: 10451 for Bronx, 11201 for Brooklyn, 10001 for Manhattan, 11431
    for Queens, 10341 for Staten Island, and None for Other.
    '''
    zip_to_boro = {'Bronx' : 10451, 'Brooklyn' : 11201, 'Manhattan' : 10001, 'Queens' : 11431,
        'Staten Island' : 10341}

    if pd.isna(zipcode):
        if boro in zip_to_boro:
            zipcode = str(zip_to_boro[boro])
        else:
            zipcode = None
            return zipcode
    return zipcode

def parse_datetime(df, column='LicenseIssuedDate'):
    '''
    This function takes two inputs:
    df: a DataFrame containing the column column. column has a default value of 'LicenseIssuedDate'
    The function should return a DataFrame with three additional columns:
    timestamp: contains the datetime object corresponding to the string stored in column.
    month: return the number corresponding to the month of timestamp: 1 for January, 2 for February,
    ...12 for December. day_of_week: return the number corresponding to the day of the week of
    timestamp: 0 f  or Monday, 1 for Tuesday, ... 6 for Sunday.
    '''
    return df
