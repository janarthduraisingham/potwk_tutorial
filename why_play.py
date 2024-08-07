"""
Created on Wed Aug  7 00:32:30 2024

@author: jd_se
"""
import streamlit as st

st.header("Why should you play Paladins of the West Kingdom?")


video_file = open("videos/test.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

st.subheader("Now, you may want to check out:")
st.write("What is a worker placement game?")
st.write("What is the aim of the game?")