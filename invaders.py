# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:32:30 2024

@author: jd_se
"""
import streamlit as st

st.header("7) The Invaders")

st.subheader("Now, you may want to check out:")


st.write("Questions? Don't worry - later, we'll look at")    
if st.button("8) Silver and Bronze"):
    st.switch_page("silver_bronze.py")
if st.button("32) Actions"):
    st.switch_page("actions.py")
    
st.write("Went on a tangent? Return to:")
    
if st.button("4) Game Board Setup"):
    st.switch_page("setup.py")