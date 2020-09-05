import pandas as pd
from collections import Counter
import streamlit as st
import seaborn as sns

def timeliner(gl_var):
    globals()['project'] = gl_var
    globals()['project'] = st.sidebar.text_input("Nama Project", value=globals()['project'])
    timeliner = st.sidebar.button("Display time")

    if timeliner == True:
        st.title("Display Timeline")
        df = pd.read_pickle(globals()['project'] + ".pkl")

        df['Dt'] = pd.to_datetime(df['date'].str.split().str[0])
        df1 = df.groupby(df['Dt'].dt.date).size().reset_index(name='Count')

        chart = sns.barplot(df1['Dt'],df1['Count'])
        chart.set_xticklabels(chart.get_xticklabels(), rotation=90)

        st.pyplot()
        
    