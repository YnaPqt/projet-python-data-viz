import streamlit as st
import pandas as pd
from src.exploration import detect_busts, detect_hidden_gems,player_global_performance


def show_gems_busts_page(df: pd.DataFrame):

    st.title("Hidden Gems & Busts")

    df_hidden_gems = detect_hidden_gems(df)
    df_busts = detect_busts(df)

    col1, col2 = st.columns(2)
    col1.metric("Nombre de Hidden Gems", len(df_hidden_gems["player_name"].unique()))
    col2.metric("Nombre de Busts", len(df_busts))

    st.divider()

    # Filtres

    st.subheader("Filtrer un joueur")

    col1, col2 = st.columns(2)

    selected_player = st.selectbox("Choisir un joueur", sorted(df["player_name"].unique()))
    kpis, fig_evolution, fig_bar, fig_radar  = player_global_performance(df, selected_player)

    st.divider()

        # KPIs
    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Efficiency", f"{kpis['efficiency']:.2f}")
    col2.metric("AST", f"{kpis['ast']:.2f}")
    col3.metric("Availability", f"{kpis['availability']:.2f}")
    col4.metric("OREB%", f"{kpis['oreb_pct']:.2f}")
    col5.metric("DREB%", f"{kpis['dreb_pct']:.2f}")
    st.divider()

    # Graphs
    st.plotly_chart(fig_evolution, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
            st.plotly_chart(fig_bar, use_container_width=True)
    with col2:
            st.plotly_chart(fig_radar, use_container_width=True)


    st.divider()

    st.subheader("💎 Hidden Gems")
    st.dataframe(df_hidden_gems, use_container_width=True)

    st.divider()

    st.subheader("❌ Draft Busts")
    st.dataframe(df_busts, use_container_width=True)