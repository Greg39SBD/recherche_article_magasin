# Installer Streamlit si nécessaire : pip install streamlit
import streamlit as st
import pandas as pd

# Charger le fichier Excel
file_path = "Recherche article magasin.xlsx"  # À adapter selon l'emplacement local
sheet_name = "Feuil1"  # À remplacer par le nom de la feuille pertinente

df = pd.read_excel(file_path, sheet_name=sheet_name)

st.title("Recherche d'articles en magasin")

# Choix de la colonne pour la recherche
column = st.selectbox("Choisissez la colonne pour la recherche :", df.columns)

# Saisie du terme de recherche
search_term = st.text_input("Entrez le terme à rechercher :")

# Filtrer le DataFrame selon la recherche
if search_term:
    filtered_df = df[df[column].astype(str).str.contains(search_term, case=False, na=False)]
    st.write(f"Résultats pour '{search_term}' dans '{column}':", filtered_df)
else:
    st.write("Veuillez entrer un terme pour lancer la recherche.")