import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt

df = pd.read_csv('fred_info_2022_5yr.csv')

index = [i for i in range(len(list(df['USINFO'])))]
df['DATE'] = index

corr = df.corr()

print("###### CORR")
print(corr)


print("###### Linear Regression")
print((corr * df["USINFO"].std())/df["DATE"].std())

print("###### y intercept Linear Regression")
print(df["USINFO"].mean() -(1.78 *  df["DATE"].mean()))


#df = pd.read_csv('USINFO.csv')
print("############# STD")
print(df["DATE"].std())