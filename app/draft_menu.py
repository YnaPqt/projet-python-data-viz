import streamlit as st

def show_draft_page():
    st.title("Comment fonctionne la Draft NBA?")

    st.markdown("""
La **draft NBA** est un événement annuel où les 30 équipes sélectionnent de nouveaux joueurs issus du basket universitaire ou international.

Elle se déroule en **deux tours**, chaque équipe ayant un choix par tour.
""")

    st.subheader("Objectif de la Draft")

    st.markdown("""
Le but principal est de **rééquilibrer la ligue** :

- Les équipes les plus faibles choisissent en premier  
- Les équipes les plus performantes choisissent en dernier  
""")

    st.subheader("La Draft Lottery")

    st.markdown("""
Les équipes qui ne participent pas aux playoffs entrent dans une **loterie** appelée *NBA Draft Lottery*.

- Seules les équipes non qualifiées participent  
- Les pires équipes ont **plus de chances** d’obtenir un haut choix  
- Un tirage au sort détermine l’ordre des premiers picks (*Top Picks*)  
""")

    st.subheader("Pourquoi c’est important ?")

    st.markdown("""
La position de draft influence fortement :

- Le potentiel du joueur sélectionné  
- Les attentes de performance  
- Les opportunités de développement  

Cependant, tous les meilleurs joueurs ne sont pas forcément sélectionnés en premier.

👉 C’est exactement ce que nous analysons dans ce projet.
""")