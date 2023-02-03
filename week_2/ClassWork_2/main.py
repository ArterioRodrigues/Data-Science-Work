"""
Name:  Arterio Rodrigues
Email: arterio.rodrigues47@myhunter.cuny.edu
Resources:  Python3.8
I attended lecture today.
Row:  2
Seat:  72
"""
import pandas as pd

file_name = input("Enter input file name: ")
out_file = input("Enter output file name: ")

df = pd.read_csv(file_name)

df = df.loc[(df["Grade"] == '3') & (df["Year"] == 2019), :]

df.to_csv(out_file, index="false")
