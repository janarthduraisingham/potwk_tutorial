# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:32:30 2024

@author: jd_se
"""
import streamlit as st

st.header("16) The Hunt Action")

video_file = open("videos/hunt.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)


st.subheader("Next up:")
if st.button("17) The Trade Action"):
    st.switch_page("trade.py")

