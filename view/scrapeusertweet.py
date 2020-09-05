import pandas as pd
from collections import Counter
import streamlit as st


def scrapeusertweet(gl_var):
    globals()['project'] = gl_var
    globals()['project'] = st.sidebar.text_input("Nama Project", value=globals()['project'])
    scrapeuser = st.sidebar.button("Scrape User")

    if  scrapeuser == True:
        st.title("User Tweet")
        df = pd.read_pickle(globals()['project'] + ".pkl")
        st.dataframe(df)
        
    