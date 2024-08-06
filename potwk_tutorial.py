# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 11:51:36 2024

@author: jd_se
"""
import streamlit as st

st.title("Paladins of the West Kingdom: How to Play")

why = st.Page("why_play.py", title="Why play Paladins of the West Kingdom?", icon=":material/thumb_up:")
worker_placement = st.Page("worker_placement.py", title="What is a worker placement game?", icon = ":material/thumb_up:")
aim = st.Page("aim.py", title="What is the aim of the game?", icon=":material/thumb_up:")

pg = st.navigation([why, worker_placement, aim])
st.set_page_config(page_title="POTWK Tutorial", page_icon=":material/thumb_up:")
pg.run()


