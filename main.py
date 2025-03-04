import pandas as pd
import matplotlib.pyplot as plt
import statistics as stat

df = pd.read_csv('tennis_pay.csv').sort_values(by='year',ascending=False)

for index, row in df.iterrows():
    print(row['year'])
