import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

# Load Data
df = pd.read_excel("Cleaned_Microplastics_Data.xlsx")

# Streamlit App
st.title("🌊 Microplastics Pollution Dashboard")

# Map Visualization
st.subheader("📍 Pollution Hotspots")
m = folium.Map(location=[df["Latitude (degree)"].mean(), df["Longitude(degree)"].mean()], zoom_start=5)
for _, row in df.iterrows():
    folium.Marker([row["Latitude (degree)"], row["Longitude(degree)"]], popup=row["Site"]).add_to(m)
folium_static(m)

# Data Summary
st.subheader("📊 Dataset Overview")
st.write(df.describe())
