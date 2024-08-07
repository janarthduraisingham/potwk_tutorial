# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:32:30 2024

@author: jd_se
"""
import streamlit as st

st.header("What are workers?")

st.subheader("Now, you may want to check out:")
if st.button("Suspicion cards"):
    st.switch_page("suspicion.py")


