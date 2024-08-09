# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:32:30 2024

@author: jd_se
"""
import streamlit as st

st.header("5) The Townsfolk")

video_file = open("videos/townsfolk.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)


st.subheader("Next up:")
if st.button("6) The Invaders"):
    st.switch_page("invaders.py")
    
st.write("Went on a tangent? Return to:")
if st.button("3) What is the aim of the game?"):
    st.switch_page("aim.py")
    
    

