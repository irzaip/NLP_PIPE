import twint
import pandas as pd
from collections import Counter
import streamlit as st



def twitscrape(gl_var):
    globals()['project'] = gl_var
    df = pd.DataFrame(None)
    globals()['project'] = st.sidebar.text_input("Nama Project", value=globals()['project'])
    search = st.sidebar.text_input("Kata Kunci yang menarik")
    limits = st.sidebar.number_input("Limit tweet", value=100, step=20, max_value=2000)
    lang = st.sidebar.text_input("Bahasa", value="id")
    jalankan = st.sidebar.button("Jalan")

    if jalankan == True:
        st.title("Search: " + search)
        df = dig_tweet(search, limits, lang)
        st.text("done")
    return globals()['project']

def dig_tweet(search, limits, lang):
    global df, project
    c = twint.Config()
    c.Store_object = True
    c.Pandas =True
    c.Search = str(search)
    c.Limit = int(limits)
    c.Lang = str(lang)
    c.Hide_output = True
    rets = twint.run.Search(c)
    df = twint.storage.panda.Tweets_df
    df.to_pickle(str(project) + ".pkl")
    st.dataframe(df)
    st.text("Dapat " + str(len(df)) + " tweets")
    return df
    


