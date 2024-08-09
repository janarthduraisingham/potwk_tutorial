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
    ko1 = st.selectbox("King's Orders",
    (0, 4, 6, 8, 10, 12, 14, 18),)
    faith1 = st.selectbox("Faith",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),)
    influence1 = st.selectbox("Influence",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),)
    strength1 = st.selectbox("Strength",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),)
    develop1 = st.selectbox("Develop",
    (0, 1, 3, 6),)
    debt1 = st.selectbox("Debt",
    (-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5),index=10)
    
with cols[1]:
    
    p2 = st.text_input("Player 2 Name")
    
with cols[2]:
    
    p3 = st.text_input("Player 3 Name")
    
with cols[3]:
    
    p4 = st.text_input("Player 4 Name")
    
st.write(p1)



