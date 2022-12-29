from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

 
    df = pd.read_json("https://node-api.flipsidecrypto.com/api/v2/queries/446958b3-a694-4bb5-98a0-41d556a96c5d/data/latest")
# df_1 = pd.DataFrame(df["SALES"],columns=df["PROJECT_NAMEE"])
alt.Chart(df).mark_bar().encode(
    alt.X('PROJECT_NAMEE') ,
    alt.Y('SALES'),
    alt.Color('PROJECT_NAMEE', legend=None))
