import pandas as pd
from collections import Counter
import streamlit as st
import glob

def combinator(gl_var):
    globals()['project'] = gl_var
    globals()['project'] = st.sidebar.text_input("Nama Project", value=globals()['project'])
    combine = st.sidebar.button("Combine This")

    fn = glob.glob('*.pkl')
    multi = st.multiselect("Pilih", fn)


    if combine == True:
        st.title("Combine This")
        for i in multi:
            st.text(i)
        st.title(multi)    
    