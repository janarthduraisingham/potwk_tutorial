# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:32:30 2024

@author: jd_se
"""
import streamlit as st

st.header("5) The Workers")

st.subheader("Now, you may want to check out:")
if st.button("Suspicion cards"):
    st.switch_page("suspicion.py")
if st.button("32) Actions"):
    st.switch_page("actions.py")

