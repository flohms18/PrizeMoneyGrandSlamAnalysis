import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tennis_pay.csv')
df = df.iloc[::-1]

df['year'] = df['year'].astype(str)

df.plot(kind="bar", x="year", y="wimbledon_women", legend=False)

tick_pos = range(0,len(df), 10)
df.plot(kind="bar", x="year", y="wimbledon_women", legend=False).set_xticks(tick_pos)

plt.show()