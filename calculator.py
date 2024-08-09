# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:32:30 2024

@author: jd_se
"""
import streamlit as st

st.header("34) Score Calculator")


cols = st.columns(4)

with cols[0]:
    
    p1 = st.text_input("Player 1 Name")

st.write(p1)


