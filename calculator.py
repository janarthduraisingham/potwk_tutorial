# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:32:30 2024

@author: jd_se
"""
import streamlit as st

st.header("34) Score Calculator")

scores = {}

cols = st.columns(4)

with cols[0]:
    
    p1 = st.text_input("Player 1 Name")
    ko1 = st.selectbox("King's Orders",
    (0, 4, 6, 8, 10, 12, 14, 18),key=3)
    faith1 = st.selectbox("Faith",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),key=3)
    influence1 = st.selectbox("Influence",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),key=3)
    strength1 = st.selectbox("Strength",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),key=3)
    develop1 = st.selectbox("Develop",
    (0, 1, 3, 6),key=3)
    debt1 = st.selectbox("Debt",
    (-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5),index=10,key=3)
    silver_provisions1 = st.selectbox("Silver and Provisions",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),key=3)
    commission1 = st.selectbox("Commission",
    (0, 2, 5, 9),key=3)
    fortify1 = st.selectbox("Fortify",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),key=3)
    garrison1 = st.selectbox("Garrison",
    (0, 2, 5, 9),key=3)
    absolve1 = st.selectbox("Absolve",
    (0, 1, 3, 6),key=3)
    convert1 = st.selectbox("Convert",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),key=3)
    
    scores[1] = sum([ko1, faith1, influence1, strength1, develop1, debt1, silver_provisions1, commission1, fortify1, garrison1, absolve1, convert1])
    
    if st.button("Calculate score"):
        st.write(scores[1])
    
with cols[1]:
    
    p2 = st.text_input("Player 2 Name")
    ko2 = st.selectbox("King's Orders",
    (0, 4, 6, 8, 10, 12, 14, 18),key=2)
    faith2 = st.selectbox("Faith",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),key=2)
    influence2 = st.selectbox("Influence",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),key=2)
    strength2 = st.selectbox("Strength",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),key=2)
    develop2 = st.selectbox("Develop",
    (0, 1, 3, 6),key=2)
    debt2 = st.selectbox("Debt",
    (-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5),index=10,key=2)
    silver_provisions2 = st.selectbox("Silver and Provisions",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),key=2)
    commission2 = st.selectbox("Commission",
    (0, 2, 5, 9),key=2)
    fortify2 = st.selectbox("Fortify",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),key=2)
    garrison2 = st.selectbox("Garrison",
    (0, 2, 5, 9),key=2)
    absolve2 = st.selectbox("Absolve",
    (0, 1, 3, 6),key=2)
    convert2 = st.selectbox("Convert",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),key=2)
    
    scores[2] = sum([ko2, faith2, influence2, strength2, develop2, debt2, silver_provisions2, commission2, fortify2, garrison2, absolve2, convert2])
    
    if st.button("Calculate score"):
        st.write(scores[2])
        
with cols[2]:
    
    p3 = st.text_input("Player 3 Name")
    ko3 = st.selectbox("King's Orders",
    (0, 4, 6, 8, 10, 12, 14, 18),key=1)
    faith3 = st.selectbox("Faith",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),key=1)
    influence3 = st.selectbox("Influence",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),key=1)
    strength3 = st.selectbox("Strength",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),key=1)
    develop3 = st.selectbox("Develop",
    (0, 1, 3, 6),key=1)
    debt3 = st.selectbox("Debt",
    (-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5),index=10,key=1)
    silver_provisions3 = st.selectbox("Silver and Provisions",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),key=1)
    commission3 = st.selectbox("Commission",
    (0, 2, 5, 9),key=1)
    fortify3 = st.selectbox("Fortify",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),key=1)
    garrison3 = st.selectbox("Garrison",
    (0, 2, 5, 9),key=1)
    absolve3 = st.selectbox("Absolve",
    (0, 1, 3, 6),key=1)
    convert3 = st.selectbox("Convert",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),key=1)
    
    scores[3] = sum([ko3, faith3, influence3, strength3, develop3, debt3, silver_provisions3, commission3, fortify3, garrison3, absolve3, convert3])
    
    if st.button("Calculate score"):
        st.write(scores[3])
    
with cols[3]:
    
    p4 = st.text_input("Player 4 Name")
    ko4 = st.selectbox("King's Orders",
    (0, 4, 6, 8, 10, 12, 14, 18),key=4)
    faith4 = st.selectbox("Faith",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),key=4)
    influence4 = st.selectbox("Influence",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),key=4)
    strength4 = st.selectbox("Strength",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),key=4)
    develop4 = st.selectbox("Develop",
    (0, 1, 3, 6),key=4)
    debt4 = st.selectbox("Debt",
    (-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5),index=10,key=4)
    silver_provisions4 = st.selectbox("Silver and Provisions",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),key=4)
    commission4 = st.selectbox("Commission",
    (0, 2, 5, 9),key=4)
    fortify4 = st.selectbox("Fortify",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),key=4)
    garrison4 = st.selectbox("Garrison",
    (0, 2, 5, 9),key=4)
    absolve4 = st.selectbox("Absolve",
    (0, 1, 3, 6),key=4)
    convert4 = st.selectbox("Convert",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),key=4)
    
    scores[4] = sum([ko4, faith4, influence4, strength4, develop4, debt4, silver_provisions4, commission4, fortify4, garrison4, absolve4, convert4])
    
    if st.button("Calculate score"):
        st.write(scores[4])
    



