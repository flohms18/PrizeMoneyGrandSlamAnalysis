import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tennis_pay.csv')

for i in df['year']:
    print(df['wimbledon_women'])