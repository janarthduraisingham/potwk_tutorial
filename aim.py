# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:32:30 2024

@author: jd_se
"""
import streamlit as st

st.header("3) What is the aim of the game?")

video_file = open("videos/aim.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)


st.subheader("Next up:")
if st.button("4) Game Board Setup"):
    st.switch_page("setup.py")

st.write("Went on a tangent? Return to:")
if st.button("1) Why play Paladins of the West Kingdom?"):
    st.switch_page("worker_placement.py")





