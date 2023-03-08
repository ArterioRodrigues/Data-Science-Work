import prog3
import pandas as pd

def print_val(value):
    print(value)

df = pd.read_csv("./data/2015.csv")


df = prog3.clean_df(df)

print(df)