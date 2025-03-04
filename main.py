import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tennis_pay.csv').sort_values(by='year',ascending=False)
df.iloc[::-1]

GrandSlam = ['wimbledon_women','aus_open_women','us_open_women']

df.plot(kind='line',x='year',y=GrandSlam,legend=False)

plt.show()