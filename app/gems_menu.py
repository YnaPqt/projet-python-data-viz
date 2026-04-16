import streamlit as st
import pandas as pd
from src.exploration import detect_busts, detect_hidden_gems


def show_gems_busts_page(df: pd.DataFrame):
    st.title("Hidden Gems & Busts")
    df_hidden_gems = detect_hidden_gems(df)
    df_busts = detect_busts(df)

    col1, col2 = st.columns(2)
    col1.metric("Nombre de Hidden Gems", len(df_hidden_gems))
    col2.metric("Nombre de Busts", len(df_busts))

    st.divider()

    st.subheader("💎 Hidden Gems")
    st.dataframe(df_hidden_gems, use_container_width=True)

    st.divider()

    st.subheader("❌ Draft Busts")
    st.dataframe(df_busts, use_container_width=True)