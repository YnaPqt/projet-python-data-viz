import pandas as pd

df = pd.read_csv(r"C:\Users\ronal\LIVECAMPUS\PROJET_Python_Data_Viz\projet-python-data-viz\data\all_seasons.csv")
print(df.head())
print(df.describe())
print(df.info())