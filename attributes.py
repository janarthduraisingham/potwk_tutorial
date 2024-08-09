# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:32:30 2024

@author: jd_se
"""
import streamlit as st

st.header("11) Attributes")

video_file = open("videos/attributes.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)


st.subheader("Next up:")
if st.button("12) The Workers"):
    st.switch_page("workers.py")
    
st.write("Questions? Don't worry - later, we'll look at:")
if st.button("14) Actions"):
    st.switch_page("actions.py")
    
st.write("Went on a tangent? Return to:")
if st.button("3) What is the aim of the game?"):
    st.switch_page("aim.py")

if st.button("4) Game Board Setup"):
    st.switch_page("setup.py")

