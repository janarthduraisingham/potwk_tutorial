# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:32:30 2024

@author: jd_se
"""
import streamlit as st

st.header("21) The Commission Action")

st.write("part 1")
video_file = open("videos/commission1.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

st.write("part 2")
video_file = open("videos/commission2.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

st.write("part 3")
video_file = open("videos/commission3.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)


st.subheader("Next up:")
if st.button("22) The Fortify Action"):
    st.switch_page("fortify.py")

st.write("Questions? Don't worry - later, we'll look at:")
if st.button("32) Iconography"):
    st.switch_page("iconography.py")
