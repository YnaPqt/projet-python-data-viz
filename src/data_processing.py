import pandas as pd
import numpy as np

def load_csv(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    print(f"CSV chargé : {df.shape[0]} lignes, {df.shape[1]} colonnes")
    return df


def clean_data(df:pd.DataFrame)-> pd.DataFrame:
    initial = len(df)
    # Supprimer la colonne Unnamed
    df.drop("Unnamed: 0", axis = 1, inplace = True)

    # Supprimer les doublons 
    df= df.drop_duplicates()

    # Remplacer college manquant
    df["college"] = df["college"].fillna("Unknown")

    # Remplacer les drafts number et round number, changer le type
    df["draft_number"] = df["draft_number"].replace("Undrafted", 0)
    df["draft_year"] = df["draft_year"].replace("Undrafted", 0)
    df["draft_round"] = df["draft_round"].replace("Undrafted", 0)
    df["draft_year"] = df["draft_year"].astype(int)
    df["draft_number"] = df["draft_number"].astype(int)
    df["draft_round"] = df["draft_round"].astype(int)

    def extract_start_year(season_str):
        return int(season_str[:4]) 

    # Extraire que l'année
    df["season"] = df["season"].apply(extract_start_year)
    df["season"] = df["season"].astype(int)

    print(f"Doublons supprimés: {initial-len(df)}")
    return df

