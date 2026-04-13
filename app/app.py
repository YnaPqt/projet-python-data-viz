import pandas as pd
from data_processing import load_csv,clean_data
from models import engine, init_db, Session

init_db()

# Charger et nettoyer les données
df = load_csv("../data/all_seasons.csv")
df_clean = clean_data (df)


session = Session()
df.to_sql("players", engine, if_exists="replace", index=False)
df.to_sql("players_stats", engine, if_exists="replace", index=False)

df_db = pd.read_sql("SELECT * FROM players", engine)
df_stats = pd.read_sql("SELECT * FROM players_stats", engine)
count = len(df_db)
print(count)
print(df_db)
print(df_stats)