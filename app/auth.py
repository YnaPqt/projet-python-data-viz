import streamlit as st
import bcrypt
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Récupérer les credentials
USERNAME = os.getenv("APP_USERNAME")
PASSWORD_HASH = os.getenv("APP_PASSWORD")


def login():
    st.title("🔐 Login")

    username_input = st.text_input("Username")
    password_input = st.text_input("Password", type="password")

    if st.button("Login"):

        # Vérification username
        if username_input == USERNAME:

            # Vérification password avec bcrypt
            if bcrypt.checkpw(password_input.encode(), PASSWORD_HASH.encode()):
                st.session_state["authenticated"] = True
                st.session_state["username"] = username_input
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Incorrect password")

        else:
            st.error("User not found")


def logout():
    if st.sidebar.button("Logout"):
        st.session_state["authenticated"] = False
        st.session_state["username"] = None
        st.rerun()