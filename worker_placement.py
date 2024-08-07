# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:19:57 2024

@author: jd_se
"""
import streamlit as st

st.header("What is a worker placement game?")

st.subheader("Now, you may want to check out:")
if st.button("3) What is the aim of the game?"):
    st.switch_page("aim.py")
#st.write("What is the aim of the game?")

