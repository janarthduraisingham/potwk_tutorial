# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:32:30 2024

@author: jd_se
"""
import streamlit as st

st.header("32) Actions")

st.subheader("Now, you may want to check out:")
if st.button("13) The Develop Action"):
    st.switch_page("develop.py")
