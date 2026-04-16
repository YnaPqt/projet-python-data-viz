from pathlib import Path
import os

import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

from src.data_processing import load_csv, clean_data
from src.models import engine, init_db
from src.exploration import * 
from src.import_data import save_to_db

from draft_menu import show_draft_page
from analyses_menu import  show_analyse_page
from scoring_menu import show_scoring_page
from gems_menu import  show_gems_busts_page

from auth import login, logout

###############################

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "data", "all_seasons.csv")

###############################

st.set_page_config(
    layout="wide")

#############################
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()
    st.stop()

# Logout button
logout()


############################

def run_init_pipeline():
     init_db()
     df = load_csv(f"{DB_PATH}")
     df = clean_data(df)
     save_to_db(df)

@st.cache_data
def load_data() -> pd.DataFrame:
      df_db = pd.read_sql("SELECT * FROM players", engine)
      df_db['draft_group'] = df_db['draft_number'].apply(assign_draft_group)

      df_resume_perf = resume_performance(df_db)
      metrics_list = ["efficiency", "ast","oreb_pct","dreb_pct","usg_pct", "ast_pct","availability", "reb"]
      df_resume_perf= calcul_scout_score(df_resume_perf, metrics_list)

      return df_resume_perf

if "pipeline_ready" not in st.session_state:
     with st.spinner("Initializing database.."):
          run_init_pipeline()
     st.session_state["pipeline_ready"] =True

df = load_data()


############# SIDE BAR MENU###########################################

with st.sidebar:
    selected = option_menu(
            None,
            options=["NBA Draft", "Analyses", "Scout Scoring", "Hidden Gems & Busts"],
            icons=["bar-chart-fill", "graph-up", "trophy-fill", "gem"],
            default_index=0
    )


if selected == "NBA Draft":
    show_draft_page()
if selected == "Analyses":
    show_analyse_page(df)
if selected == "Scout Scoring":
    show_scoring_page(df)
if selected == "Hidden Gems & Busts":
    show_gems_busts_page(df)