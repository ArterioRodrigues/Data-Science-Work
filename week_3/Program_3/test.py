import prog3
import pandas as pd

def print_val(value):
    print(value)

df = pd.read_csv("./data/2015.csv")
df = prog3.clean_df(df)

nta_df = prog3.make_nta_df("./data/df1.csv")
df_counts = prog3.count_by_area(df)

nta_code = list(nta_df['nta_code'])

new_df = pd.DataFrame({'nta':[], 'num_trees' : [], "nta_name" : [], "population" : [], "trees_per_capita" : []})

for index, row in df_counts.iterrows():
    data = nta_df.loc[nta_df['nta_code'] == row['nta']]
    data = data.values.tolist()[0]


    new_row = list(row) + data[1:]
    new_row.append(new_row[1]/new_row[-1])

    new_df.loc[len(new_df)] = new_row

print(new_df)
   