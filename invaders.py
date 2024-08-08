# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:32:30 2024

@author: jd_se
"""
import streamlit as st

st.header("6) The Invaders")

st.subheader("Next up:")
if st.button("7) Silver and Bronze"):
    st.switch_page("silver_bronze.py")

st.write("Questions? Don't worry - later, we'll look at")    

if st.button("14) Actions"):
    st.switch_page("actions.py")
    
st.write("Went on a tangent? Return to:")
    
if st.button("4) Game Board Setup"):
    st.switch_page("setup.py")