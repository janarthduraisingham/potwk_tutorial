# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:32:30 2024

@author: jd_se
"""
import streamlit as st

st.header("4) Game Board Setup")

st.subheader("Now, you may want to check out:")
if st.button("5) The Workers"):
    st.switch_page("workers.py")
if st.button("6) The Townsfolk"):
    st.switch_page("townsfolk.py")
    
if st.button("7) The Invaders"):
    st.switch_page("invaders.py")
    
if st.button("12) Attributes"):
    st.switch_page("attributes.py")
