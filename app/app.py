import pandas as pd
from src.data_processing import load_csv,clean_data
from src.models import engine, init_db
from src.exploration import * 
from src.import_data import save_to_db

import os 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "data", "all_seasons.csv")

def main():
    init_db()

    # Charger les données
    try:
        df = load_csv(f"{DB_PATH}")
    except Exception as e:
        print(f"Erreur lors du chargement du fichier")
        return

     # Nettoyer les données   
    df= clean_data(df)

    # Sauvegarder les données dans la base de données
    save_to_db(df)

    # Charger les données de la db
    df_db = pd.read_sql("SELECT * FROM players", engine)
    print(df_db)

    # Assigner les goupes de draft
    df_db['draft_group'] = df_db['draft_number'].apply(assign_draft_group)

    # Aggrégation des toutes les colonnes concernant les metriques
    df_resume_perf = resume_performance(df_db)

    # Appliquer le Scout Score avec la normalisation des valeurs (MinMaxScaler)
    metrics_list = ['efficiency', 'ast', 'availability', 'reb']
    df_resume_perf= calcul_scout_score(df_resume_perf, metrics_list)

    # Graphique HeatMap
    graph_correlation_heatmap(df_resume_perf)

    # Graphique Comparaison Draft Group Vs net_rating
    graph_net_rating_by_group(df_resume_perf)

    # Graphique Comparaison Draft Group Vs Availability
    graph_availability_by_group(df_resume_perf)
    
    # Graphique performance globale par saison vs draft group
    graph_seasonal_performance(df_resume_perf)

    # Lis hidden gems et Busts dans les groupes de Draft
    detect_hidden_gems(df_resume_perf)
    detect_busts(df_resume_perf)

    # Graphique Draft Vs Scout Score
    graph_scout_score_distribution(df_resume_perf)

    # Graphique Performance des joueurs par Scout Score
    graph_performance_vs_draft(df_resume_perf)


if __name__ == "__main__":
    main()