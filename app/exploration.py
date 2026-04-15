import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from models import engine
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

filepath = "../data/"



##### Groupement des joueurs par catégorie de Draft
# Top Picks (1-15), Mid Picks (16-30), Late Picks (>30) else Undrafted
def assign_draft_group(draft_number):
    if draft_number == 0:
        return "Undrafted/Unknown"
    elif 1 <= draft_number <= 15:
        return "Top 15 Picks"
    elif 16 <= draft_number <= 30:
        return "Mid Picks"
    else:
        return "Late Picks"
    
##### Agrégation des performances des joueurs (Efficacité/Disponibilité)
# Calcul des moyennes et création des colonnes Efficiency (pts*ts_pct) et Availability (gp/82).
def resume_performance(df):
    
    perf_df = df.groupby(["player_name", "draft_group"]).agg(
        pts = ("pts", "mean"),
        reb = ("reb", "mean"),
        ast = ("ast", "mean"),
        net_rating = ("net_rating", "mean"),
        ts_pct = ("ts_pct", "mean"),
        gp = ("gp", "mean"),
        draft_number = ("draft_number", "first")

    ).reset_index()

    # Calcul des métriques Efficiency et Availability
    perf_df["efficiency"] = perf_df["pts"] * perf_df["ts_pct"] #!ce calcul favorise davantage les profils des scoreurs
    perf_df["availability"] = perf_df["gp"] / 82 # 82 de matchs NBA

    return perf_df

##### Création du Scout Score
# Normalisation des métricues avec MinMaxScaler 
def calcul_scout_score(df, metrics=["efficiency", "ast", "availability", "reb"]):

    df_result = df.copy()
    # Normaliser avc MinMaxScaler
    scaler = MinMaxScaler()

    df_result[metrics] = scaler.fit_transform(df_result[metrics])
    df_result["scout_score"] = df_result[metrics].sum(axis=1)

    return df_result


##### Graphique: Correlation_heatmap
def graph_correlation_heatmap(df, columns=None):

    if columns is None:
        columns = ['pts', 'reb', 'ast', 'net_rating', 'ts_pct', 'efficiency', 'availability', 'scout_score']
    
    corr_matrix = df[columns].corr()

    plt.figure(figsize=(10,8))
    
    heatmap = sns.heatmap(
        corr_matrix,
        annot=True,
        cmap="coolwarm",
        center=0,
        square=True,
        linewidths=1,
        linecolor="white"
    )
    plt.title("Heatmap des Corrélations de performance", fontsize=16, fontweight="bold", pad=20)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    
    graph_heatmap = f"{filepath}/graph_heatmap"
    plt.savefig(graph_heatmap, dpi=150)
    plt.show()
    print("graph_correlation_heatmap sauvegardé dans /data/")
    

##### Graphique: Comparaison d'efficacité par Draft Group
def graph_efficiency_by_group(df):
    # Analyse de l'efficacité par Group de Draft
    efficiency_by_group = df.groupby("draft_group")["efficiency"].mean().sort_values(ascending=False)

    plt.figure(figsize=(10,6))

    ax = sns.barplot(
        x=efficiency_by_group.index,
        y=efficiency_by_group.valuers,
        palette="mako",
        hue=efficiency_by_group.index, 
        legend=True
    )

    for container in ax.containers:
        ax.bar_label(container, fmt="%.2f", padding=5, fontsize=11, fontweight="bold")

    plt.title("Efficacité Moyenne par Groupe de Draft", fontsize=14, fontweight="bold", pad=20)
    plt.ylabel("Efficiency (pts * ts_pct)", fontsize=12)
    plt.xlabel("Groupe de Draft", fontsize=12)
    plt.ylim(0, efficiency_by_group.max() * 1.15)

    plt.tight_layout
    graph_efficiency_by_group = f"{filepath}/graph_efficiency_by_group "
    plt.savefig(graph_efficiency_by_group , dpi=150)
    plt.show()
    print("graph_efficiency_by_group sauvegardé dans /data/")

#### Graphique : Net Rating par groupe de draft
def graph_net_rating_by_group(df):

    # Analyse du Net Rating par Groupe de Draft
    net_rating_by_group = df.groupby('draft_group')['net_rating'].mean().sort_values(ascending=True)

    plt.figure(figsize=(10, 6))

    ax = sns.barplot(
        x=net_rating_by_group.index, 
        y=net_rating_by_group.values, 
        palette='viridis', 
        hue=net_rating_by_group.index, 
        legend=False
    )

    for container in ax.containers:
        ax.bar_label(container, fmt='%.3f', padding=3, fontsize=11, fontweight='bold')

    plt.title('Net Rating Moyen par Groupe de Draft', fontsize=14, pad=20)
    plt.ylabel('Net Rating Mean', fontsize=12)
    plt.xlabel('Groupe de Draft', fontsize=12)

    plt.tight_layout()

    graph_net_rating_by_group= f"{filepath}/graph_net_rating_by_group "
    plt.savefig(graph_net_rating_by_group , dpi=150)
    plt.show()
    print("graph_efficiency_by_group sauvegardé dans /data/")


##### Graphique: Distribution Games Played par Groupe de Draft
def graph_availability_by_group(df):

    # Analyse de la Disponibilité par Groupe de Draft
    availability_by_group = df.groupby('draft_group')['availability'].mean().sort_values(ascending=False)

    plt.figure(figsize=(10, 6))

    ax = sns.barplot(
        x=availability_by_group.index, 
        y=availability_by_group.values, 
        palette='magma', 
        hue=availability_by_group.index, 
        legend=False
    )

    for container in ax.containers:
        ax.bar_label(container, fmt='%.3f', padding=5, fontsize=11, fontweight='bold')

    plt.title('Disponibilité Moyenne par Groupe de Draft', fontsize=14, pad=20)
    plt.ylabel('Availability (GP / 82)', fontsize=12)
    plt.ylim(0, 1)

    plt.tight_layout()
    plt.savefig(filepath, dpi=150)
    plt.show()
    print("graph_net_rating_by_group sauvegardé dans /data/")


def graph_seasonal_performance(df):
    """
    Calcule les Scout Scores saisonniers et génère un graphique linéaire interactif Plotly
    montrant les tendances de performance par groupe de draft au fil du temps.
    """
    # 1. Préparer les métriques saisonnières
    seasonal_metrics = df.copy()
    seasonal_metrics['efficiency'] = seasonal_metrics['pts'] * seasonal_metrics['ts_pct']
    seasonal_metrics['availability'] = seasonal_metrics['gp'] / 82

    # 2. Normaliser pour créer un Scout Score saisonnier
    scaler = MinMaxScaler()
    metrics_to_scale = ['efficiency', 'ast', 'availability', 'reb']
    seasonal_metrics[metrics_to_scale] = scaler.fit_transform(seasonal_metrics[metrics_to_scale])
    seasonal_metrics['scout_score'] = seasonal_metrics[metrics_to_scale].sum(axis=1)

    # 3. Aggréger par saison et par groupe de draft
    yearly_summary = seasonal_metrics.groupby(['season', 'draft_group'])['scout_score'].mean().reset_index()

    # 4. Créer le graphique interactif
    fig = px.line(
        yearly_summary,
        x='season',
        y='scout_score',
        color='draft_group',
        markers=True,
        title='Évolution de la Performance (Scout Score) par Année et Groupe de Draft',
        labels={'scout_score': 'Score de Scout Moyen', 'season': 'Saison', 'draft_group': 'Groupe de Draft'}
    )

    fig.update_layout(
        xaxis_title='Saison (Année de début)',
        yaxis_title='Score de Scout Moyen',
        legend_title='Groupe de Draft',
        hovermode='x unified',
        xaxis=dict(
            tickmode='linear',
            tick0=yearly_summary['season'].min(),
            dtick=2
        )
    )

    filepath = f"../data/top_scorers_{fig}.html"
    fig.write_html(filepath)
    fig.show()

### Distribution des scores par groupe de draft
def graph_scout_score_distribution(df):
    """
    Génère un boxplot de la distribution du Scout Score par groupe de draft.
    """
    plt.figure(figsize=(12, 6))
    sns.boxplot(
        data=df, 
        x='draft_group', 
        y='scout_score', 
        palette='viridis', 
        hue='draft_group', 
        legend=False
    )
    plt.title('Distribution du Scout Score par Groupe de Draft')
    plt.ylabel('Scout Score')
    plt.xlabel('Draft Group')
    plt.tight_layout()
    plt.savefig(filepath, dpi=150)
    plt.show()
    print("graph_scout_score_distribution sauvegardé dans /data/")


def graph_performance_vs_draft(df, threshold):
    """
    Génère un scatter plot montrant la performance par rapport à la position de draft.
    """
    plt.figure(figsize=(12, 6))
    sns.scatterplot(
        data=df, 
        x='draft_number', 
        y='scout_score', 
        hue='draft_group', 
        alpha=0.6
    )
    plt.axhline(y=threshold, color='r', linestyle='--', label=f'Seuil Q3: {threshold:.2f}')
    plt.title('Performance vs Position de Draft')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(filepath, dpi=150)
    plt.show()
    print("graph_performance_vs_draft sauvegardé dans /data/")



### DETECTION DES HIDDEN GEMS et BUSTS
#  Hidden Gems : Draft tardive (>15) mais top performance.
#  Busts : Top 15 draft mais bottom  performance.

def detect_hidden_gems_and_busts(df):
    """
    Identifie les 'Hidden Gems' (draft tardive, haute performance)
    et les 'Busts' (draft précoce, basse performance).
    Sauvegarde également les résultats en fichiers CSV.
    """
    # Calcul des seuils
    high_threshold = df['scout_score'].quantile(0.75)
    low_threshold = df['scout_score'].quantile(0.25)

    # Identification des groupes
    hidden_gems = df[(df['draft_number'] > 15) & (df['scout_score'] >= high_threshold)]
    busts = df[(df['draft_number'] <= 15) & (df['scout_score'] <= low_threshold) & (df['draft_number'] > 0)]

    # Sauvegarde en CSV incluse dans la fonction
    hidden_gems.to_csv('hidden_gems.csv', index=False)
    busts.to_csv('busts.csv', index=False)

    return hidden_gems, busts, high_threshold, low_threshold

