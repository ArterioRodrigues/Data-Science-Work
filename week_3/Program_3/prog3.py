"""
Name:  Arterio Rodrigues
Email: arterio.rodrigues47@myhunter.cuny.edu
Resources:  Python3.8 Pandas
"""
import pandas as pd

def clean_df(df, year = 2015):
    """
    df: the name of a DataFrame containing TreesCount Data from OpenData NYC.
    year: the year of the data set. There are three possible years 1995, 2005, or 2015
    The default value is 2015.
    """

    exceptions_2015 = ['tree_dbh', 'health', 'spc_latin', 'spc_common', 'nta', 'latitude',
        'longitude']
    exceptions_2005 = ['tree_dbh', 'status', 'spc_latin', 'spc_common', 'nta', 'latitude',
        'longitude']
    exceptions_1995 = ['diameter', 'condition', 'spc_latin', 'spc_common', 'nta_2010', 'latitude',
        'longitude']

    if year == 2015:
        exceptions = exceptions_2015
    elif year == 2005:
        exceptions = exceptions_2005
    else:
        exceptions = exceptions_1995

    for column in list(df.columns):

        if not column.lower() in exceptions:
            df = df.drop(columns = column)

    for index, _ in enumerate(exceptions_2015):
        df = df.rename(columns = {exceptions[index]: exceptions_2015[index]})

    df = df[exceptions_2015]
    return df

def make_nta_df(file_name):
    """
    file_name: the name of a CSV file containing population and names for neighborhood tabulation
    areas (NYC OpenData NTA Demographics). The function should open the file file_name as DataFrame,
    returns a DataFrame containing only the columns containing the NTA code (labeled as nta_code),
    the neigborhood name (labeled as nta_name), and the 2010 population (labeled as population).
    """
    df = pd.read_csv(file_name)
    exceptions= ['nta_code', 'nta_name', 'population']

    pos_x = 0
    for column in df.columns:
        if not "nta" in column.lower() and not "population 2010 number" in column.lower():
            df = df.drop(columns = column)
        else:
            df = df.rename(columns = {column: exceptions[pos_x]})
            pos_x += 1

    return df

def count_by_area(df):
    """
    This function takes one inputs:
    df: a DataFrame that includes the nta column.
    The function should return a DataFrame that has two columns, [nta, num_trees] where nta is the
    code of the Neighborhood Tabulation Area and num_trees is the sum of the number of trees,
    grouped by nta.
    """

    keys = []
    tree_data = []

    data = df.groupby('nta').apply(len)

    for key in data.keys():
        keys.append(key)
        tree_data.append(data[key])

    data = pd.DataFrame.from_dict({'nta': keys , 'num_trees': tree_data})
    return data

def neighborhood_trees(tree_df, nta_df):
    """
    This function takes two inputs:
    tree_df: a DataFrame containing the column nta
    nta_df: a DataFrame with two columns, 'NTACode' and 'NTAName'.
    This function returns a DataFrame as a result of joining the two input dataframes, with tree_df
    as the left table. The join should be on NTA code. The resulting dataframe should contain the
    following columns, in the following order:

    nta
    num_trees
    nta_name
    population
    trees_per_capita: this is a newly calculated column, calculatefd by dividing the number of trees
    by the population in each neighborhood.
    """

    new_df = pd.DataFrame({'nta':[], 'num_trees' : [],
        "nta_name" : [], "population" : [], "trees_per_capita" : []})

    for _, row in tree_df.iterrows():
        data = nta_df.loc[nta_df['nta_code'] == row['nta']]
        data = data.values.tolist()[0]


        new_row = list(row) + data[1:]
        new_row.append(new_row[1]/new_row[-1])

        new_df.loc[len(new_df)] = new_row
    return new_df

def compute_summary_stats(df, col):
    '''
    This function takes two inputs:
    df: a DataFrame containing a column col.
    col: the name of a numeric-valued col in the DataFrame.
    This function returns the mean and median of the Series df[col]. Note that since numpy is
    not oneof the libraries for this assignment, your function should compute these
    statistics without using numpy.
    '''

    mean = df[col].mean()
    median = df[col].median()

    return mean , median

def mse_loss(theta,y_vals):
    '''
    This function takes two inputs:
    theta: a numeric value.
    y_vals: a Series containing numeric values.
    Computes the Mean Squared Error of the parameter theta and a
    Series, y_vals. See Section 4.2: Modeling Loss Functions where this
    function is implemented using numpy. Note that numpy is not one of the
    libraries for this assignment and your function should compute MSE without using numpy.
    '''
    mean_square_value = 0

    for val in y_vals:
        mean_square_value += ((val - theta) * (val - theta))

    return mean_square_value/len(y_vals)

def mae_loss(theta,y_vals):
    '''
    This function takes two inputs:
    theta: a numeric value.
    y_vals: a Series containing numeric values.
    Computes the Mean Absolute Error of the parameter theta and a Series, y_vals. See Section 4.2:
    Modeling Loss Functions where this function is implemented using numpy. Note that numpy is not
    one of the libraries for this assignment and your function should compute MAE without
    using numpy.
    '''

    mean_absolute_value = 0

    for val in y_vals:
        mean_absolute_value +=  abs(val - theta)

    return mean_absolute_value/len(y_vals)

def test_mse(loss_fnc=mse_loss):
    '''
    This test function takes one input:
    loss_fnc: a function that takes in two input parameters (a numeric value and a
    Series of numeric values) and returns a numeric value. It has a default value of mse
    loss. This is a test function, used to test whether the loss_fnc returning True
    if the loss_fnc performs correctly (e.g. computes Mean Squared Error) and False otherwise.
    '''
    vals = []
    for num in range(10000):
        vals.append(num)

    theta = 500


    if loss_fnc(theta, vals) == mse_loss(theta, vals):
        return True

    if loss_fnc(theta, vals) == mae_loss(theta, vals):
        return True

    return False
