import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set()

ti = sns.load_dataset('...\input\titanic.csv').dropna().reset_index(drop=True)

sns.histplot(data = ti['age'], kde = True, bins =30)
plt.show()