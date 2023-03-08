import pandas as pd
from datetime import datetime

dataframe = pd.read_csv("../../Data/taxi_jfk_june2020.csv", dtype = 'unicode')

print(dataframe.head())

columns_to_drop = ["VendorID","RatecodeID","store_and_fwd_flag","payment_type","extra","mta_tax","tolls_amount","improvement_surcharge","congestion_surcharge"]

dataframe = dataframe.drop(columns = columns_to_drop)

for index, row in dataframe.iterrows():
    if float(row["total_amount"]) < 0:
        dataframe = dataframe.drop(index, axis = 0)

#print(dataframe.head())

###########################################################################################################################

dataframe["percent_tip"] = 100 * dataframe["tip_amount"].astype(float)/(dataframe["total_amount"].astype(float) - dataframe["tip_amount"].astype(float))

dropoff = pd.to_datetime(dataframe["tpep_dropoff_datetime"])
pickup = pd.to_datetime(dataframe["tpep_pickup_datetime"])

dataframe["duration"] = dropoff - pickup
dataframe["duration"] = dataframe["duration"].apply(lambda dura:  dura.total_seconds())

dataframe["dayofweek"] = pickup.apply(datetime.weekday)

#print(dataframe.head())

#######################################################################################################################################

columns = ["passenger_count", "trip_distance", "fare_amount","tip_amount","total_amount", "duration", "dayofweek"]

for column in columns:
    dataframe[column] = dataframe[column].fillna(dataframe[column].median())

#print(dataframe)

##################################################################################################################################################

df = pd.read_csv("../../Data/taxi_zones.csv")
location_id = {}

for index, row in df.iterrows():
    location_id[row['LocationID']] = row["zone"]


for index, row in dataframe.iterrows():
   
    dataframe.loc[index, "PU_borough"] = location_id.get(int(row['PULocationID']), "NONE")
    dataframe.loc[index, "DO_borough"] = location_id.get(int(row['DOLocationID']), "NONE")

#######################################################################################################################################################
print(dataframe.head())

col = dataframe['DO_borough']
prefix = "PU_"
new_coloumns_dict = {}
col_to_drop = col[0]

for _, value in col.items():
    new_coloumns_dict[prefix + value] = [0 for i in range(len(col))]
    if col_to_drop < value:
        col_to_drop = value

df = pd.DataFrame(new_coloumns_dict)



for index, value in col.items():
    df.loc[index, prefix + value] = "1"

df = df.drop(df.columns[-1], axis = 1)
print(df, col_to_drop)