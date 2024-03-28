import streamlit as st
import pandas as pd
from streamlit_folium import folium_static
import folium

# Lecture du fichier CSV
data = pd.read_csv('car_crash.csv', encoding='ISO-8859-1')

# Créer une carte Folium
m = folium.Map(location=[data['Latitude'].mean(), data['Longitude'].mean()], zoom_start=10)

# Ajouter des marqueurs pour chaque point
for index, row in data.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']]).add_to(m)

# Afficher la carte dans Streamlit
folium_static(m)
