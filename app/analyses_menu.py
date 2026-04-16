import streamlit as st
import pandas as pd
from src.exploration import graph_correlation_heatmap,graph_efficiency_by_group, graph_availability_by_group, graph_net_rating_by_group


def show_analyse_page(df: pd.DataFrame):
    st.title("NBA Draft Analyses")
    st.markdown("Distribution d'analyse de performance par groupe de Draft.")
    st.write("Groupes de Draft : **Top 15 Picks**, **Mid Picks**, **Late Picks**, **Undrafted/Unknown**")

    # KPI metrics row
    col1, col2, col3 = st.columns(3)
    col1.metric("Nombre total de joueurs", len(df))
    col2.metric("Moyenne Générale de Scout Score", f"{df['scout_score'].mean():.2f}")
    col3.metric("Nombre de Groupes de Draft", df["draft_group"].nunique())
    
    # Charts
    st.divider()

    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Correlation heatmap")
        fig_heatmap = graph_correlation_heatmap(df)
        st.pyplot(fig_heatmap)
        st.write("efficacité")

    with col_b:
        st.subheader("Efficacité par Draft Group")
        fig_efficiency =graph_efficiency_by_group(df)
        st.pyplot(fig_efficiency)
        st.write(f"efficacdsggggggggggggggggggggggggdgdf gdsggdfdggfhfhh dgfdhhhdgfdgfh ggfdf dsggf sdggglkbb npodopofd igofghofihgggggggité")

    st.divider()

    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Net Rating par Draft Group")
        fig_net_rating=graph_net_rating_by_group(df)
        st.pyplot(fig_net_rating)

    with col_b:
        st.subheader("Disponibilité par Draft Group")
        fig_availability =graph_availability_by_group(df)
        st.pyplot(fig_availability)

    st.divider()
    
    st.subheader("Table de joueurs NBA")
    st.dataframe(df, use_container_width=True)