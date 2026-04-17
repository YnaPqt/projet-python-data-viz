# 🏀 Analyse de la Draft NBA

## 📌 Contexte

La NBA Draft est un événement annuel où les 30 équipes sélectionnent de nouveaux joueurs issus du basketball universitaire ou international.

Elle se déroule en **deux tours**, chaque équipe disposant d’un choix par tour.

---

## 🎯 Objectif de la Draft

Le but principal de la draft est de **rééquilibrer la ligue** :

* Les équipes les plus faibles choisissent en premier
* Les équipes les plus performantes choisissent en dernier

---

## 🎲 La Draft Lottery

Les équipes qui ne participent pas aux playoffs entrent dans une loterie appelée **NBA Draft Lottery** :

* Seules les équipes non qualifiées participent
* Les pires équipes ont plus de chances d’obtenir un haut choix
* Un tirage au sort détermine l’ordre des premiers picks

---

## ❓ Pourquoi c’est important ?

La position de draft influence fortement :

* Le potentiel du joueur sélectionné
* Les attentes de performance
* Les opportunités de développement

👉 Cependant, tous les meilleurs joueurs ne sont pas forcément sélectionnés en premier.

---

## 📊 Objectif du projet

Ce projet consiste à développer une application Python permettant d’analyser les drafts NBA à partir d’un dataset Kaggle :

🔗 https://www.kaggle.com/datasets/justinas/nba-players-data/data

### 🎯 Questions analysées :

* Les **top picks** sont-ils réellement les meilleurs joueurs ?
* Existe-t-il des **hidden gems** (joueurs sous-estimés) ?
* Peut-on identifier des **draft busts** (joueurs décevants) ?

---

## ⚙️ Technologies utilisées

* 🐍 Python
* 📊 Streamlit (interface utilisateur)
* 🗄️ SQLAlchemy (ORM / base de données)
* 🔐 Bcrypt (hash des mots de passe)
* 🗃️ SQLite (base de données locale)
* 📈 Pandas / Scikit-learn (analyse et scoring)
* 📉 Matplotlib / Seaborn / Plotly (visualisation)

---

## 🧠 Méthodologie

Pipeline analytique :

```
Raw Data → Cleaning → Feature Engineering → Scoring → Insights
```

### Étapes clés :

1. **Nettoyage des données**
2. **Création de métriques avancées**

   * Efficiency
   * Availability
   
3. **Normalisation des performances**
4. **Calcul du Scout Score**
5. **Détection des profils**

   * Hidden Gems
   * Draft Busts

---

## 📊 Fonctionnalités de l’application

### 🏀 NBA Draft

* Explication du fonctionnement de la draft

### 📈 Analyses

* Visualisations des performances par groupe de draft

### 🧮 Scout Scoring

* Score de performance basé sur plusieurs métriques

### 💎 Hidden Gems & Busts

* Détection automatique :

  * Joueurs sous-estimés
  * Joueurs décevants

---

## 🏗️ Structure du projet

```
project/
│
├── src/
│   ├── data_processing.py
│   ├── exploration.py
│   ├── models.py
│   ├── import_data.py
│
├── app/
│   └── dashboard.py
│
├── data/
│   └── all_seasons.csv
│
├── tests/
│
└── README.md
```

---

## 🚀 Lancer le projet

### 1. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 2. Lancer l’application

```bash
streamlit run app/dashboard.py
```

---

## 🧪 Tests

Lancer les tests avec :

```bash
pytest
```

---

## 📌 Conclusion

Ce projet met en évidence que :

* La draft n’est pas toujours prédictive de la performance
* Certains joueurs draftés tardivement deviennent des stars
* Les choix élevés comportent aussi des risques

👉 Une approche data permet de mieux comprendre et évaluer ces phénomènes.

---

## 👤 Auteur

Projet réalisé dans le cadre d’un projet data / analyse NBA.
