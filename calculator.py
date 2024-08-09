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
    
with cols[1]:
    
    p2 = st.text_input("Player 2 Name")
    
with cols[2]:
    
    p3 = st.text_input("Player 3 Name")
    
with cols[3]:
    
    p4 = st.text_input("Player 4 Name")

st.write(p1+p2+p3+p4)


