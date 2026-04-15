from models import Player, engine

def save_to_db(df):

    if df.empty:
        print("Dataframe vide, rien à importer.")
        return
    
    try:
        df.to_sql(
            "players",
            engine,
            if_exists="replace",
            index=False

        )
        print(f"{len(df)} lignes inserées.")

    except Exception as e:
        print(f"Erreur: {e}")

