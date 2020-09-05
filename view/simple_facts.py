import pandas as pd
from collections import Counter
import streamlit as st
import re

   

def simple_facts(gl_var):
    globals()['project'] = gl_var
    globals()['project'] = st.sidebar.text_input("Nama Project", value=globals()['project'])
    simple_fact = st.sidebar.button("Run Simple Facts")

    related_user = []
    htag = []

    def gettag(text):
        for i in text:
            htag.append(i)

    def get_username(text):
        result = re.findall(r"(@[A-Za-z]+[A-Za-z0-9_]+)(?![A-Za-z0-9_]*\\.)",text)
        related_user.extend(result)

    if simple_fact == True:
        st.text("Cleaning")
        st.title("Most User")
        df = pd.read_pickle(globals()['project'] + ".pkl")
        st.text("total file record length :" + str(len(df)))
        df.tweet.apply(get_username)
        st.text("total scraped user:" + str(len(related_user)))
        most = Counter(related_user).most_common(10)
        st.dataframe(most)

        st.title("Most Hashtag")
        df.hashtags.apply(gettag)
        st.text("Total Hashtags : "+ str(len(htag)))
        most_htag = Counter(htag).most_common(10)
        st.dataframe(most_htag)









    return globals()['project']


    

