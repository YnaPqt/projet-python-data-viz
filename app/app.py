import pandas as pd
from data_processing import load_csv,clean_data
from models import engine, init_db
from exploration import * 
# top_scorers_per_season, assign_draft_group, resume_performance, calcul_scout_score, graph_correlation_heatmap, graph_efficiency_by_group, graph_net_rating_by_group,graph_availability_by_group,graph_seasonal_performance, graph_scout_score_distribution,graph_performance_vs_draft, detect_hidden_gems_and_busts
from import_data import save_to_db

def main():
    init_db()

    # Charger les données
    try:
        df = load_csv("../data/all_seasons.csv")
    except Exception as e:
        print(f"Erreur lors du chargement du fichier")
        return

     # Nettoyer les données   
    df= clean_data(df)

    # Sauvegarder les données dans la base de données
    save_to_db(df)

    df_db = pd.read_sql("SELECT * FROM players", engine)
    print(df_db)

    df_db['draft_group'] = df_db['draft_number'].apply(assign_draft_group)

    df_resume_perf = resume_performance(df_db)

    df_resume_perf= calcul_scout_score(df_resume_perf)

    graph_correlation_heatmap(df_resume_perf)

    graph_net_rating_by_group(df_resume_perf)


if __name__ == "__main__":
    main()