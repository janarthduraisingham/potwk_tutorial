# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:32:30 2024

@author: jd_se
"""
import streamlit as st

st.header("9) Provisions")

st.subheader("Now, you may want to check out:")
if st.button("10) Tax"):
    st.switch_page("tax.py")
if st.button("32) Actions"):
    st.switch_page("actions.py")

