# 🌊 Projet de Prédiction de Tsunami

Ce projet utilise le machine learning pour prédire si un séisme est susceptible de provoquer un tsunami en fonction de ses caractéristiques physiques et géographiques.

Il est composé de deux parties principales :
1.  Un **notebook Jupyter** (`tsunami.ipynb`) pour l'analyse exploratoire des données (EDA), le prétraitement et l'entraînement du modèle.
2.  Une **application web interactive** (`Int.py`) construite avec Streamlit pour effectuer des prédictions en direct.

## Aperçu de l'application

(Vous pouvez prendre une capture d'écran de votre application Streamlit et l'ajouter ici. Par exemple, placez-la dans un dossier `assets/` et liez-la comme ceci : `![Aperçu de l'app](assets/demo.png)`)

## Fonctionnalités

* Interface web interactive pour des prédictions faciles.
* Saisie de 8 caractéristiques sismiques (MMI, CDI, latitude, longitude, etc.).
* Prédiction en temps réel à l'aide d'un modèle de classification (Decision Tree / Random Forest) pré-entraîné.
* Visualisation des données d'entrée saisies par l'utilisateur.

## Lancement

Il y a deux façons d'utiliser ce projet :

### 1. Lancer l'application web

Pour démarrer l'interface Streamlit, exécutez la commande suivante dans votre terminal :

```bash
streamlit run Int.py
```

Ouvrez votre navigateur à l'adresse `http://localhost:8501`.

### 2. Explorer l'analyse et l'entraînement

Pour voir comment les données ont été analysées et le modèle entraîné, lancez Jupyter :

```bash
jupyter notebook tsunami.ipynb
```

## 📁 Structure du projet

```
projet-tsunami/
│
├── 📄 .gitignore           # Fichiers à ignorer par Git
├── 📄 README.md             # Ce fichier
├── 📄 requirements.txt      # Dépendances Python
│
├── 🐍 Int.py               # Script de l'application Streamlit
├── 📓 tsunami.ipynb         # Notebook d'analyse et d'entraînement
│
├── 📁 data/
│   └── 📊 earthquake_data_tsu... # Données brutes
│
├── 📁 models/
│   └── 🤖 DT_95.pkl           # Modèle de classification entraîné
│
└── 📁 assets/
    └── 🖼️ Image.jfif # Image de fond de l'app
```

## Données et Modèle

* **Source des données :** [Kaggle - Global Earthquake & Tsunami Risk Assessment](https://www.kaggle.com/datasets/ahmeduzaki/global-earthquake-tsunami-risk-assessment-dataset)
* **Modèle :** Le classificateur utilisé est un **Random Forest** (confirmé dans votre script `Int.py`), sauvegardé en tant que fichier `DT_95.pkl`.

## Auteur

* **Mohamed Yassine Chalbat**
