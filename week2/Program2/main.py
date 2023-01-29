"""
Name:  Arterio Rodrigues
Email: arterio.rodrigues47@myhunter.cuny.edu
Resources:  Python3.8 Pandas
"""

def clean_df(df, year = 2015):
    """
    df: the name of a DataFrame containing TreesCount Data from OpenData NYC.
    year: the year of the data set. There are three possible years 1995, 2005, or 2015
    The default value is 2015.
    """

    exceptions_2015 = ['tree_dbh', 'health', 'spc_latin', 'spc_common', 'address', 'zipcode',
        'boroname', 'nta', 'latitude', 'longitude', 'council_district', 'census_tract']

    exceptions_2005 = ['tree_dbh', 'status', 'spc_latin', 'spc_common', 'address', 'zipcode',
        'boroname', 'nta', 'latitude', 'longitude', 'cncldist', 'census_tract']

    exceptions_1995 = ['diameter', 'condition', 'spc_latin', 'spc_common', 'address',
        'zip_original', 'borough', 'nta_2010', 'latitude', 'longitude', 'council_district',
        'censustract_2010']

    if year == 2015:
        exceptions = exceptions_2015
    elif year == 2005:
        exceptions = exceptions_2005
    else:
        exceptions = exceptions_1995

    for column in df.columns:

        if not column.lower() in exceptions:
            df = df.drop(columns = column)

    for index, _ in enumerate(exceptions_2015):
        df = df.rename(columns = {exceptions[index]: exceptions_2015[index]})

    df = df[exceptions_2015]
    return df

def filter_health(df, keep):
    """
    df: a DataFrame that includes the health column.
    keep: a list of values for the health column.
    The function returns the DataFrame with only rows that where the column health contains
    a value from the list keep. All rows where the health column contains a different value
    are dropped.
    """
    for index, row in df.iterrows():
        if not row["health"] in keep:
            df = df.drop(index)
    return df

def add_indicator(row):
    """
    row: a Series (a row) containing values for tree_dbh and health.
    The function should return 1 if health is not Poor and tree_dbh is larger than
    10. Otherwise, it should return 0.
    """
    if row['health'] != "Poor" and row['tree_dbh'] > 10:
        return 1
    return 0

def find_trees(df, species):
    """
    df: a DataFrame that includes the spc_latin column and the address column.
    species: a string containing the Latin name of a tree.
    The function should return, as a list, the address for all trees of that
    species in spc_latin. If that species does not occur in the DataFrame,
    then an empty list is returned.
    """
    list_d = []

    for _, row in df.iterrows():
        if str(row["spc_latin"]).lower() == species.lower():
            list_d.append(row["address"])

    return list_d

def count_by_area(df, area = "boroname"):
    """
    df: a DataFrame that includes the area column.
    area: the name of a column in df. The default value is "boroname".
    The function should return the sum of the number of trees, grouped by
    area. For example if area = "boroname", your function should group by
    boroname and return the number of each trees in each of the boroughs.
    """

    return df.groupby(area).size()
