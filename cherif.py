import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
# Charger les données depuis les fichiers
impressions = pd.read_csv('impressions.csv')
clics = pd.read_csv('clics.csv')
achats = pd.read_csv('achats.csv')
impr_clic = pd.merge(clics, impressions, on="cookie_id", how="right")
fusion  = pd.merge(impr_clic, achats, on="cookie_id",how="left")
fusion
df = pd.DataFrame(fusion)

st.title("Dashboard avec Streamlit et Plotly")
st.subheader("Données fusionnées")
# Créer deux colonnes pour afficher les graphiques
col1, col2 = st.columns(2)
# Box plot de l'âge moyen en fonction des product_id
with col1:
    st.subheader("Box plot de l'âge moyen en fonction des product_id")
    fig = plt.figure(figsize=(10, 6))
    sns.boxplot(x="product_id", y="age", data=fusion)
    plt.xlabel("product_id")
    plt.ylabel("Âge moyen")
    plt.title("Distribution de l'âge moyen en fonction des product_id")
    st.pyplot(fig)

# Histogramme avec Plotly
with col2:
    st.title("Histogramme avec Plotly")
    fig1 = px.histogram(fusion, x="campaign_id", y="price")
    st.plotly_chart(fig1)
fcol1, fcol2 = st.columns(2)  
with fcol1:
    st.title("Histogramme avec Plotly")
    fig = px.histogram(fusion, x="gender", y="price")
    st.plotly_chart(fig, width=200)

with fcol2:
    # Calcul du chiffre d'affaires
    chiffre_affaires = df['price'].sum()
    st.write(f"<span style='color:red; font-size:40px;'>Chiffre d'affaires : {chiffre_affaires} € </span>", unsafe_allow_html=True)

# Entonnoir
# Conversion des variables en date
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
df['timestamp_x'] = pd.to_datetime(df['timestamp_x'], unit='s')
df['timestamp_y'] = pd.to_datetime(df['timestamp_y'], unit='s')

 # Calcul des statistiques
nb_impressions = df['timestamp'].count()
nb_clics = df['timestamp_x'].count()
nb_achats = df['timestamp_y'].count()

# Création du diagramme en entonnoir

fig2 = go.Figure(
            go.Funnel(
                y=['Impressions', 'Clics', 'Achats'],
                x=[nb_impressions, nb_clics, nb_achats]
            )
        )
