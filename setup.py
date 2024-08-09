# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:32:30 2024

@author: jd_se
"""
import streamlit as st

st.header("4) Game Board Setup")

st.write("part 1")
video_file = open("videos/setup1.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

st.write("part 2")
video_file = open("videos/setup2.mp4", "rb")
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
       
if st.button("30) The King's Orders"):
    st.switch_page("kings_orders.py")

if st.button("31) The King's Favours"):
    st.switch_page("kings_favours.py")
    
if st.button("28) The Paladins"):
    st.switch_page("paladins.py")
    
if st.button("14) Actions"):
    st.switch_page("actions.py")
    
if st.button("11) Attributes"):
    st.switch_page("attributes.py")
    
if st.button("7) Silver and Bronze"):
    st.switch_page("silver_bronze.py")
    
if st.button("8) Provisions"):
    st.switch_page("provisions.py")
    
if st.button("29) Tavern Cards"):
    st.switch_page("kings_orders.py")
    
if st.button("13) Suspicion"):
    st.switch_page("kings_orders.py")
    
if st.button("10) Debt"):
    st.switch_page("kings_orders.py")