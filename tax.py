# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:32:30 2024

@author: jd_se
"""
import streamlit as st

st.header("9) Tax")

video_file = open("videos/tax.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)


st.subheader("Next up:")
if st.button("10) Debt"):
    st.switch_page("debt.py")

st.write("Questions? Don't worry - later, we'll look at:")
if st.button("13) Suspicion"):
    st.switch_page("suspicion.py")
    
    
st.write("Went on a tangent? Return to:")

if st.button("7) Silver and Bronze"):
    st.switch_page("silver_bronze.py")
