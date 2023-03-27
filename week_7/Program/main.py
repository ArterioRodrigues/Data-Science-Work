import pandas as pd
from sklearn.preprocessing import PolynomialFeatures 
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LassoCV, RidgeCV, LinearRegression
import pickle


#def import_data(csv_file):
df = pd.read_csv("../data/data.csv")
df["units"] = df.index.to_series()

print(df.head())
#return df
#########################################################
#########################################################

y_col_name = "OIL"
test_size = 0.25
random_state = 21

x_train = df["units"][: int(len(df["units"]) * (1 - test_size))]
y_train = df[y_col_name][: int(len( df[y_col_name]) * (1 - test_size))]
x_test = df["units"][int(len(df["units"]) * (1 - test_size)):]
y_test = df[y_col_name][int(len( df[y_col_name]) * (1 - test_size)):]

#return x_train, x_test, y_train, y_col_name

xes = df['units']
yes = df['OIL']
epsilon = 100
verbose = False


poly = PolynomialFeatures(degree=5, include_bias=False)
poly_features = poly.fit_transform(xes.array.reshape(-1,1))


degrees = [1, 2, 3, 4, 5]

mods = [LinearRegression().fit(poly_features[ :, :deg], yes) for deg in degrees]

for index, mod in enumerate(mods):
    prediction = mod.predict(poly_features[:, :degrees[index]])
    #print(index, mean_squared_error(yes, prediction))

############################################################

#Fit model

xes = df["units"]
yes = df["OIL"]
poly_deg = 2
reg = "lasso"

poly = PolynomialFeatures(degree = poly_deg, include_bias = False)
poly_features = poly.fit_transform(xes.array.reshape(-1 , 1))

if reg == "lasso":
    mod = LassoCV().fit(poly_features, yes)
else:
    mod = RidgeCV().fit(poly_features, yes)

ser_mod = pickle.dumps(mod)

###############################################################

mod_pkl = ser_mod
poly_xes = df['units']
yes = df['OIL']

mod_pkl_reconstructed = pickle.loads(mod_pkl)

predicted_values = mod_pkl_reconstructed.predict(xes)

mse = mean_squared_error(yes, predicted_values)
r2s = r2_score(yes, predicted_values)