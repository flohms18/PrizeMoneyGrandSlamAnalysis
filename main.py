import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tennis_pay.csv').sort_values(by='year',ascending=False)
df.iloc[::-1]

GrandSlam_Women = ['wimbledon_women','aus_open_women','us_open_women','roland_garros_women']
GrandSlam_Men = ['wimbledon_men','aus_open_men','us_open_men','roland_garros_men']
colors = ['blue', 'red', 'orange', 'purple', 'green', 'yellow', 'brown', 'pink']

GrandSlam = GrandSlam_Women + GrandSlam_Men
print(GrandSlam)

df.plot(kind='line',x='year',y=GrandSlam,legend=False, color=colors)
plt.show()



