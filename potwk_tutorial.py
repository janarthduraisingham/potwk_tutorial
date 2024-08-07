# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 11:51:36 2024

@author: jd_se
"""
import streamlit as st


st.set_page_config(page_title="POTWK Tutorial", page_icon=":material/thumb_up:")

st.title("Paladins of the West Kingdom: Bitesize How to Play")

st.write ("Check off chapters to fill the progress bar!")
#checks = st.columns(4)
#with checks[0]:
#    one=st.checkbox('1')
#with checks[1]:
#    two=st.checkbox('2')
#with checks[2]:
#    three=st.checkbox('3')
#with checks[3]:
#    four=st.checkbox('4')


checks1 = st.columns(10)
checks2 = st.columns(10)
checks3 = st.columns(10)
checks4 = st.columns(10)
checkboxes = {}

for i in range(10):   
    with checks1[i]:
        checkboxes[str(i)]=st.checkbox(str(i+1))
        
for i in range(10):
    with checks2[i]:
        checkboxes[str(i+10)]=st.checkbox(str(i+10+1))

for i in range(10):
    with checks3[i]:
        checkboxes[str(i+20)]=st.checkbox(str(i+20+1))
        
for i in range(7):
    with checks4[i]:
        checkboxes[str(i+30)]=st.checkbox(str(i+30+1))
        
        
    
    
    
    

progress= sum(checkboxes.values()) * 100/37
my_bar = st.progress(progress, text="Progress!")



why = st.Page("why_play.py", title="1) Why play Paladins of the West Kingdom?", icon=":material/thumb_up:")
worker_placement = st.Page("worker_placement.py", title="2) What is a worker placement game?", icon = ":material/thumb_up:")
aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
setup = st.Page("setup.py", title="4) Game setup", icon=":material/thumb_up:")
workers = st.Page("workers.py", title="5) The Workers", icon=":material/thumb_up:")
townsfolk = st.Page("townsfolk.py", title="6) The Townsfolk", icon=":material/thumb_up:")
invaders = st.Page("invaders.py", title="7) The Invaders", icon=":material/thumb_up:")
silver_bronze = st.Page("silver_bronze.py", title="8) Silver and Bronze", icon=":material/thumb_up:")
provisions = st.Page("provisions.py", title="9) Provisions", icon=":material/thumb_up:")
tax = st.Page("tax.py", title="10) Tax", icon=":material/thumb_up:")
debt = st.Page("debt.py", title="11) Debt", icon=":material/thumb_up:")
attributes = st.Page("attributes.py", title="12) Attributes", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
#aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")


pg = st.navigation([why,
                    worker_placement,
                    aim,
                    setup,
                    workers,
                    townsfolk,
                    invaders,
                    silver_bronze,
                    provisions,
                    tax,
                    debt,
                    attributes])
pg.run()



