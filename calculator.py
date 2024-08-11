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
    (0, 4, 6, 8, 10, 12, 14, 18),key=1)
    faith1 = st.selectbox("Faith",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),key=2)
    influence1 = st.selectbox("Influence",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),key=3)
    strength1 = st.selectbox("Strength",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),key=4)
    develop1 = st.selectbox("Develop",
    (0, 1, 3, 6),key=5)
    debt1 = st.selectbox("Debt",
    (-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5),index=10,key=6)
    silver_provisions1 = st.selectbox("Silver and Provisions",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),key=7)
    commission1 = st.selectbox("Commission",
    (0, 2, 5, 9),key=8)
    fortify1 = st.selectbox("Fortify",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),key=9)
    garrison1 = st.selectbox("Garrison",
    (0, 2, 5, 9),key=10)
    absolve1 = st.selectbox("Absolve",
    (0, 1, 3, 6),key=11)
    convert1 = st.selectbox("Convert",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),key=12)
    
    scores[1] = sum([ko1, faith1, influence1, strength1, develop1, debt1, silver_provisions1, commission1, fortify1, garrison1, absolve1, convert1])
    
    
with cols[1]:
    
    p2 = st.text_input("Player 2 Name")
    ko2 = st.selectbox("King's Orders",
    (0, 4, 6, 8, 10, 12, 14, 18),key=13)
    faith2 = st.selectbox("Faith",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),key=14)
    influence2 = st.selectbox("Influence",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),key=15)
    strength2 = st.selectbox("Strength",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),key=16)
    develop2 = st.selectbox("Develop",
    (0, 1, 3, 6),key=17)
    debt2 = st.selectbox("Debt",
    (-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5),index=10,key=18)
    silver_provisions2 = st.selectbox("Silver and Provisions",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),key=19)
    commission2 = st.selectbox("Commission",
    (0, 2, 5, 9),key=20)
    fortify2 = st.selectbox("Fortify",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),key=21)
    garrison2 = st.selectbox("Garrison",
    (0, 2, 5, 9),key=22)
    absolve2 = st.selectbox("Absolve",
    (0, 1, 3, 6),key=23)
    convert2 = st.selectbox("Convert",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),key=24)
    
    scores[2] = sum([ko2, faith2, influence2, strength2, develop2, debt2, silver_provisions2, commission2, fortify2, garrison2, absolve2, convert2])
    
        
with cols[2]:
    
    p3 = st.text_input("Player 3 Name")
    ko3 = st.selectbox("King's Orders",
    (0, 4, 6, 8, 10, 12, 14, 18),key=25)
    faith3 = st.selectbox("Faith",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),key=26)
    influence3 = st.selectbox("Influence",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),key=27)
    strength3 = st.selectbox("Strength",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),key=28)
    develop3 = st.selectbox("Develop",
    (0, 1, 3, 6),key=29)
    debt3 = st.selectbox("Debt",
    (-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5),index=10,key=30)
    silver_provisions3 = st.selectbox("Silver and Provisions",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),key=31)
    commission3 = st.selectbox("Commission",
    (0, 2, 5, 9),key=32)
    fortify3 = st.selectbox("Fortify",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),key=33)
    garrison3 = st.selectbox("Garrison",
    (0, 2, 5, 9),key=34)
    absolve3 = st.selectbox("Absolve",
    (0, 1, 3, 6),key=35)
    convert3 = st.selectbox("Convert",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),key=36)
    
    scores[3] = sum([ko3, faith3, influence3, strength3, develop3, debt3, silver_provisions3, commission3, fortify3, garrison3, absolve3, convert3])
    
    
with cols[3]:
    
    p4 = st.text_input("Player 4 Name")
    ko4 = st.selectbox("King's Orders",
    (0, 4, 6, 8, 10, 12, 14, 18),key=37)
    faith4 = st.selectbox("Faith",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),key=38)
    influence4 = st.selectbox("Influence",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),key=39)
    strength4 = st.selectbox("Strength",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),key=40)
    develop4 = st.selectbox("Develop",
    (0, 1, 3, 6),key=41)
    debt4 = st.selectbox("Debt",
    (-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5),index=10,key=42)
    silver_provisions4 = st.selectbox("Silver and Provisions",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),key=43)
    commission4 = st.selectbox("Commission",
    (0, 2, 5, 9),key=44)
    fortify4 = st.selectbox("Fortify",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),key=45)
    garrison4 = st.selectbox("Garrison",
    (0, 2, 5, 9),key=46)
    absolve4 = st.selectbox("Absolve",
    (0, 1, 3, 6),key=47)
    convert4 = st.selectbox("Convert",
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),key=48)
    
    scores[4] = sum([ko4, faith4, influence4, strength4, develop4, debt4, silver_provisions4, commission4, fortify4, garrison4, absolve4, convert4])
    
if st.button("Calculate all scores", key=49):
    st.write(p1 + ": " + str(scores[1]))
    st.write(p2 + ": " + str(scores[2]))
    st.write(p3 + ": " + str(scores[3]))    
    st.write(p4 + ": " + str(scores[4]))
    



