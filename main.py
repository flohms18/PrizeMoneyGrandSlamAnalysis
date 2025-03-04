import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tennis_pay.csv')

df['year'] = df['year'].astype(str)

df.plot(kind="bar", x="year", y="wimbledon_women", legend=False)

plt.show()

