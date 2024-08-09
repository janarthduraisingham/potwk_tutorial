# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:32:30 2024

@author: jd_se
"""
import streamlit as st

st.header("31) The King's Favours")

st.write("part 1")
video_file = open("videos/kings_favours1.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

st.write("part 2")
video_file = open("videos/kings_favours2.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)


st.subheader("Next up:")
if st.button("32) Iconography"):
    st.switch_page("iconography.py")

st.write("Went on a tangent? Return to:")

if st.button("4) Game Board Setup"):
    st.switch_page("setup.py")
