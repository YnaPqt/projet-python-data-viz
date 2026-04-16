import streamlit as st
import pandas as pd
from src.exploration import graph_seasonal_performance, graph_performance_vs_draft, graph_scout_score_distribution

st.set_page_config(
    layout="wide",
     initial_sidebar_state="expanded")

def show_scoring_page(df: pd.DataFrame):
    st.title("NBA Draft Analyses")
    st.markdown("Distribution d'analyse de performance par groupe de Draft.")
    st.write("Groupes de Draft : **Top 15 Picks**, **Mid Picks**, **Late Picks**, **Undrafted/Unknown**")

    # Charts
    st.divider()

    col_a, col_b = st.columns([1,1])

    with col_a:
        st.subheader("Draft Vs Scout Score")
        fig_score_draft =graph_scout_score_distribution(df)
        st.pyplot(fig_score_draft, use_container_width=True)
        st.write(f"efficacdsgggggggggggggggggggité")
    with col_b:
        st.subheader("Performance des joueurs par Scout Score")
        fig_perf_draft = graph_performance_vs_draft(df)
        st.pyplot(fig_perf_draft)
        st.write("efficacité")

    st.divider()

    st.subheader("performance globale par saison vs draft group")
    fig_seasonal_draft=graph_seasonal_performance(df)
    st.plotly_chart(fig_seasonal_draft, use_container_width=True)
