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
# Box plot de l'âge moyen en fonction des product_id

st.subheader("Box plot de l'âge moyen en fonction des product_id")
fig = plt.figure(figsize=(10, 6))
sns.boxplot(x="product_id", y="age", data=fusion)
plt.xlabel("product_id")
plt.ylabel("Âge moyen")
plt.title("Distribution de l'âge moyen en fonction des product_id")
st.pyplot(fig)

# Histogramme avec Plotly

st.title("Histogramme avec Plotly")
fig1 = px.histogram(fusion, x="campaign_id", y="price")
st.plotly_chart(fig1,width=400)

st.title("Histogramme avec Plotly")
fig = px.histogram(fusion, x="gender", y="price")
st.plotly_chart(fig, width=400)

# Calcul du chiffre d'affaires

chiffre_affaires = df['price'].sum()
st.write(f"<span style='color:red; font-size:40px;'>Chiffre d'affaires : {chiffre_affaires} € </span>", unsafe_allow_html=True)

st.title("Histogramme avec Plotly")
fig = px.bar(fusion, x="product_id" , y="age")
st.plotly_chart(fig, width=400)
