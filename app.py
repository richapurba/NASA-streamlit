import streamlit as st
import pandas as pd
import numpy as np

#Title and subtitle
st.title("Habitable Exoplanets and Stars")
st.subheader("NASA Discovery")

#Load dataframe
df = pd.read_excel('Habitable.csv')
st.dataframe(df)