import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tennis_pay.csv').sort_values(by='year',ascending=False)
df['year'] = df['year'].astype(int)

df.plot(kind='line',x='year',y=['wimbledon_women','wimbledon_men'],legend=False)

plt.show()