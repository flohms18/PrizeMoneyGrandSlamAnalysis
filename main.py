import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tennis_pay.csv')
print(df.head())

GrandSlam = ['wimbledon_men','us_open_men','aus_open_men','roland_garros_men']

men_colors = ['#77C264','#1DAFDB','#4291CF','#D85428']

df.plot(kind='line',x='year',y=GrandSlam,color=men_colors)

plt.show()