import pandas as pd
from collections import Counter
import streamlit as st


def cleaning(gl_var):
    globals()['project'] = gl_var
    globals()['project'] = st.sidebar.text_input("Nama Project", value=globals()['project'])
    clean = st.sidebar.button("Clean 1")

    if clean == True:
        st.text("Cleaning")
        df = pd.read_pickle(globals()['project'] + ".pkl")
        st.dataframe(df)
        
    