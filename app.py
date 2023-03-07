import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# Change background into image
st.markdown(
   """
   <style>
   p {background-image: url("bg.jpeg");}
   </style>
   """,
   unsafe_allow_html=True)

#Sidebar
image = Image.open('logo.png')

st.sidebar.image(image, caption=None)

st.sidebar.title("Habitable Exoplanets and Stars")
st.sidebar.subheader("NASA Discovery")

#Load dataframe
df = pd.read_csv('Habitable.csv')
st.dataframe(df)
