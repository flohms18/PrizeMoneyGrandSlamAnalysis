import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tennis_pay.csv')

for i in df['year']:
    print(f"in {i}, the prize money was equal to {df['wimbledon_women']}")