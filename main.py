import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tennis_pay.csv')
print(df.head())

men_columns = ['wimbledon_men', 'us_open_men', 'aus_open_men', 'roland_garros_men']
women_columns = ['wimbledon_women', 'us_open_women', 'aus_open_women', 'roland_garros_women']

colors = ['#77C264','#1DAFDB','#4291CF','#D85428']

for col, color in zip(men_columns, colors):
    plt.plot(df['year'], df[col], label=col, color=color, linestyle=':', linewidth=2)

for col, color in zip(women_columns, colors):
    plt.plot(df['year'], df[col], label=col, color=color, linestyle='-', linewidth=2)

plt.title('Men\'s and Women\'s Grand Slam Prize Money Over Time')
plt.xlabel('Year')
plt.ylabel('Prize Money')
plt.legend(title="Grand Slam Tournaments")
plt.show()