import streamlit as st
import requests
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go


st.title("Bienvenue sur l'application DMWM !")
st.write("Je vous souhaite bon visionnage!")


# Fonction pour appeler l'API et obtenir les données
impressions = pd.read_csv('impressions.csv')
clics = pd.read_csv('clics.csv')
achats = pd.read_csv('achats.csv')

impr_clic = pd.merge(impressions,clics, on ='cookie_id')
fusion = pd.merge(impr_clic, achats, on ='cookie_id')
fusion
data = st.write(fusion)
df = pd.DataFrame(data)

# Afficher les données dans le dashboard

# Calcul du chiffre d'affaires
chiffre_affaires = df['price'].sum()
st.write(f"<span style='color:red; font-size:40px;'>Chiffre d'affaires : {chiffre_affaires} € </span>", unsafe_allow_html=True)

## Box plot
fig_col1, fig_col2 = st.columns(2)
with fig_col1:
        fig = px.box(df, x='product_id', y='age')
        fig.update_layout(
            xaxis_title='Produits',
            yaxis_title="Âge",
            title="Relation entre l'âge et les produits")
        st.plotly_chart(fig)

# Création du diagramme des ventes en fonction des campagnes
fig = px.bar(fusion, x='campaign_id', y='price', title='Diagramme des ventes en fonction des campagnes')

# Affichage du diagramme dans Streamlit
st.plotly_chart(fig)
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
with fig_col2:
    fig2 = go.Figure(
    go.Funnel(
                y=['Impressions', 'Clics', 'Achats'],
                x=[nb_impressions, nb_clics, nb_achats]
            )
        )

# Affichage du diagramme dans Streamlit
fig2.update_layout(title="Diagramme en entonnoir")
st.plotly_chart(fig2)

# Filtrage des données en fonction de la campaign_id sélectionnée
campaign_ids = df['campaign_id'].unique()
selected_campaign_id = st.selectbox('Sélectionnez une campaign_id', campaign_ids)
filtered_df = df[df['campaign_id'] == selected_campaign_id]

# Calcul des statistiques sur les données filtrées
nb_impressions = filtered_df['timestamp'].count()
nb_clics = filtered_df['timestamp_x'].count()
nb_achats = filtered_df['timestamp_y'].count()

# Création du diagramme en entonnoir avec les données filtrées
fig2 = go.Figure(
            go.Funnel(
                y=['Impressions', 'Clics', 'Achats'],
                x=[nb_impressions, nb_clics, nb_achats]
            )
        )

# Affichage du diagramme dans Streamlit
fig2.update_layout(title="Diagramme en entonnoir - Filtrage des données en fonction de la campaign_id sélectionnée")
st.plotly_chart(fig2)


