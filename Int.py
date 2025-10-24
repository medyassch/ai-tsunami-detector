import streamlit as st
import numpy as np
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import base64

# --------------------------
# ⚙️ Configuration de la page
# --------------------------
st.set_page_config(page_title="Prédiction Tsunami", page_icon="🌊", layout="centered")

# Chargement du modèle
model = pickle.load(open(
    r"C:\Users\ACH\OneDrive - OFPPT\Documents\AI\Analyse_des_donnees\Data2\DT_95.pkl", "rb"))

# Titre et description
st.title("🌊 Prédiction des Tsunami")
st.markdown("Veuillez renseigner les caractéristiques physiques et géographiques pour obtenir une prédiction.")

# --------------------------
# 🧾 Saisie utilisateur
# --------------------------
with st.form("input_form"):
    col1, col2 = st.columns(2)

    with col1:
        cdi = st.number_input("🔹 Intensité ressentie par la population (CDI)", min_value=0, max_value=9, step=1)
        mmi = st.number_input("🔹 Intensité instrumentale de Mercalli modifiée (MMI)", min_value=1, max_value=9, step=1)
        dmin = st.number_input("🔹 Distance à la station sismique la plus proche (°)", min_value=0.0, max_value=1000.0)
        nst = st.number_input("🔹 Nombre de stations sismiques ayant détecté l’événement", min_value=0.0, max_value=1000.0)

    with col2:
        gap = st.number_input("🔸 Écart azimutal entre les stations (°)", min_value=0.0)
        latitude = st.number_input("🔸 Latitude de l’épicentre (WGS84)", min_value=-90.0, max_value=90.0)
        longitude = st.number_input("🔸 Longitude de l’épicentre (WGS84)", min_value=-180.0, max_value=180.0)
        Year = st.number_input("🔸 Année de survenue de l’événement", min_value=1900, step=1)

    submit = st.form_submit_button("Prédire")

# --------------------------
# 🤖 Prédiction
# --------------------------
if submit:
    inputs = [cdi, mmi, dmin, nst, gap, latitude, longitude, Year]

    if all(x == 0.0 for x in inputs):
        st.warning("⚠️ Veuillez saisir des valeurs valides pour lancer une prédiction.")
    else:
        features = np.array([inputs])
        prediction = model.predict(features)

        st.markdown("---")
        st.subheader("🧠 Résultat de la Prédiction")
        st.success(f"✅ Classe prédite : **{int(prediction[0])}**")

        # ✅ Correction du DataFrame : noms uniques et ordre correct
        df_feat = pd.DataFrame(features, columns=[
            'cdi', 'mmi', 'dmin', 'nst', 'gap', 'latitude', 'longitude', 'Year'
        ])

        with st.expander("📈 Visualiser les valeurs d'entrée"):
            st.dataframe(df_feat)

        # ✅ Graphique amélioré
        with st.expander("📊 Représentation graphique"):
            fig, ax = plt.subplots()
            sns.barplot(x=df_feat.columns, y=features[0], palette="viridis", ax=ax)
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
            ax.set_ylabel("Valeur")
            st.pyplot(fig)

# --------------------------
# 🖼️ Arrière-plan personnalisé
# --------------------------
image_path = r"C:\Users\ACH\OneDrive - OFPPT\Documents\AI\Analyse_des_donnees\Data2\Image.jfif"

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

encoded_image = get_base64_of_bin_file(image_path)

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)),
                          url("data:image/png;base64,{encoded_image}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: white;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------
# ℹ️ À propos
# --------------------------
st.markdown("---")
st.markdown("""
### ℹ️ À propos de cette application
Cette application utilise un modèle de machine learning pour prédire la probabilité qu’un séisme provoque un tsunami à partir de ses caractéristiques physiques et géographiques.  

**Projet développé par :** *Mohamed Yassine Chalbat*  
**Technologies utilisées :** Streamlit, Random Forest, Scikit-learn, Python  
**Source des données :** [Kaggle - Tsunami Risk Assessment](https://www.kaggle.com/datasets/ahmeduzaki/global-earthquake-tsunami-risk-assessment-dataset)
""")
