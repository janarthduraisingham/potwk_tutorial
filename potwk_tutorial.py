# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 11:51:36 2024

@author: jd_se
"""
import streamlit as st

worker_placement = st.Page("worker_placement.py", title="What is a worker placement game?", icon = ":material/thumb_up:")
aim = st.Page("aim.py", title="What is the aim of the game?", icon=":material/thumb_up:")

pg = st.navigation([worker_placement, aim])
st.set_page_config(page_title="POTWK Tutorial", page_icon=":material/thumb_up:")
pg.run()

st.title("Paladins of the West Kingdom: How to Play")
st.header("Why should you play Paladins of the West Kingdom?")

st.subheader("Now, you may want to check out:")
st.write("What is a worker placement game?")
st.write("What is the aim of the game?")