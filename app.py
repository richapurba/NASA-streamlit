import streamlit as st
import pandas as pd
import numpy as np

# Change background into image
st.markdown(
   f”””
   <style>
   p {
   background-image: url(‘bg.jpeg’);
   }
   </style>
   ”””,
   unsafe_allow_html=True)

#Title and subtitle
st.title("Habitable Exoplanets and Stars")
st.subheader("NASA Discovery")

#Load dataframe
df = pd.read_csv('Habitable.csv')
st.dataframe(df)
