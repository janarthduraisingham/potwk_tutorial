# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:32:30 2024

@author: jd_se
"""
import streamlit as st

st.header("5) The Workers")

st.subheader("Next up:")
if st.button("6) The Townsfolk"):
    st.switch_page("townsfolk.py")
    
st.write("Questions? Don't worry - later we'll look at:")    
if st.button("3) What is the aim of the game?"):
    st.switch_page("aim.py")
if st.button("Suspicion cards"):
    st.switch_page("suspicion.py")
if st.button("32) Actions"):
    st.switch_page("actions.py")
    
st.write("Went on a tangent? Return to:")
if st.button("2) What is a Worker Placement Game?"):
    st.switch_page("worker_placement.py")


