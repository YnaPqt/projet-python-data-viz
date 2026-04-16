import streamlit as st
import pandas as pd
from src.exploration import assign_draft_group,resume_performance,calcul_scout_score,graph_correlation_heatmap,graph_efficiency_by_group, graph_net_rating_by_group, graph_net_rating_by_group, graph_availability_by_group


def show_analyse_page(df: pd.DataFrame):
    st.title("NBA Draft Analyses")
    st.markdown("Distribution d'analyse de performance par groupe de Draft.")

    # KPI metrics row
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Players", len(df))
    col2.metric("Avg Scout Score", f"{df['scout_score'].mean():.2f}")
    col3.metric("Draft Groups", df["draft_group"].nunique())

    st.divider()

    # Charts
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Net Rating by Draft Group")
        graph_net_rating_by_group(df)   # returns a fig → use st.plotly_chart / st.pyplot

    with col_b:
        st.subheader("Availability by Draft Group")
        graph_availability_by_group(df)

    st.subheader("Raw Data")
    st.dataframe(df, use_container_width=True)