# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 11:51:36 2024

@author: jd_se
"""
import streamlit as st


st.set_page_config(page_title="POTWK Tutorial", page_icon=":material/thumb_up:")

st.title("Paladins of the West Kingdom: Bitesize How to Play")

st.write ("Check off chapters to fill the progress bar!")

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
          

progress= round(sum(checkboxes.values()) * 100/37)
my_bar = st.progress(progress, text="Your Progress:")



why = st.Page("why_play.py", title="1) Why play Paladins of the West Kingdom?", icon=":material/thumb_up:")
worker_placement = st.Page("worker_placement.py", title="2) What is a worker placement game?", icon = ":material/thumb_up:")
aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":material/thumb_up:")
setup = st.Page("setup.py", title="4) Game Board Setup", icon=":material/thumb_up:")
workers = st.Page("workers.py", title="5) The Workers", icon=":material/thumb_up:")
townsfolk = st.Page("townsfolk.py", title="6) The Townsfolk", icon=":material/thumb_up:")
invaders = st.Page("invaders.py", title="7) The Invaders", icon=":material/thumb_up:")
silver_bronze = st.Page("silver_bronze.py", title="8) Silver and Bronze", icon=":material/thumb_up:")
provisions = st.Page("provisions.py", title="9) Provisions", icon=":material/thumb_up:")
tax = st.Page("tax.py", title="10) Tax", icon=":material/thumb_up:")
debt = st.Page("debt.py", title="11) Debt", icon=":material/thumb_up:")
attributes = st.Page("attributes.py", title="12) Attributes", icon=":material/thumb_up:")
develop = st.Page("develop.py", title="13) The Develop Action", icon=":material/thumb_up:")
hunt = st.Page("hunt.py", title="14) The Hunt Action", icon=":material/thumb_up:")
trade = st.Page("trade.py", title="15) The Trade Action", icon=":material/thumb_up:")
recruit = st.Page("recruit.py", title="16) The Recruit Action", icon=":material/thumb_up:")
pray = st.Page("pray.py", title="17) The Pray Action", icon=":material/thumb_up:")
conspire = st.Page("conspire.py", title="18) The Conspire Action", icon=":material/thumb_up:")
commission = st.Page("commission.py", title="19) The Commission Action", icon=":material/thumb_up:")
fortify = st.Page("fortify.py", title="20) The Fortify Action", icon=":material/thumb_up:")
garrison = st.Page("garrison.py", title="21) The Garrison Action", icon=":material/thumb_up:")
absolve = st.Page("absolve.py", title="22) The Absolve Action", icon=":material/thumb_up:")
attack = st.Page("attack.py", title="23) The Attack Action", icon=":material/thumb_up:")
convert = st.Page("convert.py", title="24) The Convert Action", icon=":material/thumb_up:")
turns = st.Page("turns.py", title="25) Turns and Rounds", icon=":material/thumb_up:")
paladins = st.Page("paladins.py", title="26) Paladins", icon=":material/thumb_up:")
tavern = st.Page("tavern.py", title="27) Tavern Cards", icon=":material/thumb_up:")
kings_orders = st.Page("kings_orders.py", title="28) The King's Orders", icon=":material/thumb_up:")
kings_favours = st.Page("kings_favours.py", title="29) The King's Favours", icon=":material/thumb_up:")
iconography = st.Page("iconography.py", title="30) Iconography", icon=":material/thumb_up:")
scoring = st.Page("scpring.py", title="31) Scoring", icon=":material/thumb_up:")
actions = st.Page("actions.py", title="32) Actions", icon=":material/thumb_up:")



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
                    attributes,
                    develop,
                    hunt,
                    trade,
                    recruit,
                    pray,
                    conspire,
                    commission,
                    fortify,
                    garrison,
                    absolve,
                    attack,
                    convert
                
                    ])
pg.run()



