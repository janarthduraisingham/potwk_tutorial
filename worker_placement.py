# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:19:57 2024

@author: jd_se
"""
import streamlit as st

st.header("2) What is a worker placement game?")

st.subheader("Now, you may want to check out:")
if st.button("3) What is the aim of the game?"):
    st.switch_page("aim.py")
if st.button("5) The Workers"):
    st.switch_page("workers.py")


