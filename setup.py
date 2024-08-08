# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:32:30 2024

@author: jd_se
"""
import streamlit as st

st.header("4) Game Board Setup")

video_file = open("videos/setup.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)


st.subheader("Next up:")
if st.button("5) The Townsfolk"):
    st.switch_page("townsfolk.py")
    
st.write("Questions? Don't worry - later, we'll look at:")
if st.button("5) The Workers"):
    st.switch_page("workers.py")
    
if st.button("7) The Invaders"):
    st.switch_page("invaders.py")
    
if st.button("12) Attributes"):
    st.switch_page("attributes.py")
