import streamlit as st
import pandas as pd
import joblib
import numpy as np

# ----------------------
# Page config
# ----------------------
st.set_page_config(
    page_title="Pré-dimensionnement BT",
    page_icon="electric-meter.png",  # favicon professionnel téléchargé
    layout="centered"
)

# ----------------------
# Charger le modèle
# ----------------------
model = joblib.load("modele.pkl")  # Assurez-vous que le modèle est dans le même dossier

# ----------------------
# Titre et logo
# ----------------------
st.image("logo-PI.gif", width=300)  # Logo de l'entreprise
st.markdown(
    "<h1 style='text-align: center; color: #003366;'>Outil Intelligent de Pré-dimensionnement BT</h1>",
    unsafe_allow_html=True
)
st.write("---")

# ----------------------
# Entrée des données utilisateur
# ----------------------
st.subheader("Entrer les paramètres du tableau BT")

puissance = st.number_input("Puissance (kVA)", min_value=0.0, format="%.2f")
icc = st.number_input("Icc (kA)", min_value=0.0, format="%.2f")
temp = st.number_input("Température (°C)", min_value=0.0, format="%.1f")

# ----------------------
# Bouton de calcul
# ----------------------
if st.button("Calculer"):
    new_data = pd.DataFrame({
        "Puissance_kVA": [puissance],
        "Icc_kA": [icc],
        "Temp_C": [temp]
    })
    
    # Prédiction du disjoncteur
    prediction = model.predict(new_data)[0]
    st.success(f"Disjoncteur proposé : {prediction} A")
    
    # Vérification simple IEC 61439
    Ib = puissance * 1000 / (np.sqrt(3) * 400)  # courant nominal
    if prediction >= Ib:
        st.info("Conforme à la norme IEC 61439")
    else:
        st.error("Non conforme à la norme IEC 61439")

# ----------------------
# Sidebar
# ----------------------
st.sidebar.header("À propos")
st.sidebar.write(
    "Outil développé pour pré-dimensionner automatiquement les tableaux électriques BT "
    "selon les normes IEC 61439."
)