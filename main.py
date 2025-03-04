import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tennis_pay.csv')

for index, df in df.iterrows():
    print(f"In {df['year']}, the prize money was equal to {df['wimbledon_men']}")
    
