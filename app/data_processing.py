import pandas as pd

def load_csv(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath, index_col=0)
    print(f"CSV chargé : {df.shape[0]} lignes, {df.shape[1]} colonnes")
    return df


def clean_data(df:pd.DataFrame)-> pd.DataFrame:
    initial = len(df)
    df= df.drop_duplicates()
    print(f"Doublons supprimés: {initial-len(df)}")
    df= df.dropna()
    return df

