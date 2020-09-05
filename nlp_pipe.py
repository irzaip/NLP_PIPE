import streamlit as st
import numpy
import pandas as pd
from view.twitscrape import twitscrape
from view.sentiment import sentiment
from view.cleaning import cleaning
from view.simple_facts import simple_facts

globals()['project'] = "project_"

def main():
  app_mode = st.sidebar.selectbox("Choose the app mode",
    ["_", "Scrape Twitter", "Simple Facts", "Cleaning", "Sentiment Result"])
  if app_mode == "Scrape Twitter":
    globals()['project'] = twitscrape(globals()['project'])
  elif app_mode == "Sentiment Result":
    globals()['project'] = sentiment(globals()['project'])
  elif app_mode == "Cleaning":
    globals()['project'] = cleaning(globals()['project'])
  elif app_mode == "Simple Facts":
    globals()['project'] = simple_facts(globals()['project'])

if __name__ == "__main__":
    main()