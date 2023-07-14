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

merged_data = pd.merge(clics, impressions, on="cookie_id", how="right")
merged_data = pd.merge(merged_data, achats, on="cookie_id",how="left")
merged_dat = merged_data.fillna("-")
merged_data = merged_dat.replace("-",pd.NA)
df = pd.DataFrame(merged_data)

st.title("Dashboard avec Streamlit et Plotly")
st.subheader("Données dfnées")
# Créer deux colonnes pour afficher les graphiques
col1, col2 = st.columns(2)
# Box plot de l'âge moyen en fonction des product_id
with col1:
    st.subheader("Box plot de l'âge moyen en fonction des product_id")
    fig = plt.figure(figsize=(10, 6))
    sns.boxplot(x="product_id", y="age", data=df)
    plt.xlabel("product_id")
    plt.ylabel("Âge moyen")
    plt.title("Distribution de l'âge moyen en fonction des product_id")
    st.pyplot(fig)

# Histogramme avec Plotly
with col2:
    st.title("Histogramme avec Plotly")
    fig1 = px.histogram(df, x="campaign_id", y="price")
    st.plotly_chart(fig1)

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

    # Affichage du diagramme dans Streamlit
    fig2.update_layout(title="Diagramme en entonnoir")
    st.plotly_chart(fig2)



