# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 11:51:36 2024

@author: jd_se
"""
import streamlit as st


st.set_page_config(page_title="POTWK Tutorial", page_icon=":european_castle:",
                   initial_sidebar_state='collapsed')

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
        
for i in range(3):
    with checks4[i]:
        checkboxes[str(i+30)]=st.checkbox(str(i+30+1))
          

progress= round(sum(checkboxes.values()) * 100/33)
my_bar = st.progress(progress, text="Your Progress:")



why = st.Page("why_play.py", title="1) Why play Paladins of the West Kingdom?", icon=":european_castle:")
worker_placement = st.Page("worker_placement.py", title="2) What is a worker placement game?", icon = ":european_castle:")
aim = st.Page("aim.py", title="3) What is the aim of the game?", icon=":european_castle:")
setup = st.Page("setup.py", title="4) Game Board Setup", icon=":european_castle:")
townsfolk = st.Page("townsfolk.py", title="5) The Townsfolk", icon=":european_castle:")
invaders = st.Page("invaders.py", title="6) The Invaders", icon=":european_castle:")
silver_bronze = st.Page("silver_bronze.py", title="7) Silver and Bronze", icon=":european_castle:")
provisions = st.Page("provisions.py", title="8) Provisions", icon=":european_castle:")
tax = st.Page("tax.py", title="9) Tax", icon=":european_castle:")
debt = st.Page("debt.py", title="10) Debt", icon=":european_castle:")
attributes = st.Page("attributes.py", title="11) Attributes", icon=":european_castle:")
workers = st.Page("workers.py", title="12) The Workers", icon=":european_castle:")
suspicion = st.Page("suspicion.py", title="13) Suspicion", icon=":european_castle:")
actions = st.Page("actions.py", title="14) Actions", icon=":european_castle:")
develop = st.Page("develop.py", title="15) The Develop Action", icon=":european_castle:")
hunt = st.Page("hunt.py", title="16) The Hunt Action", icon=":european_castle:")
trade = st.Page("trade.py", title="17) The Trade Action", icon=":european_castle:")
recruit = st.Page("recruit.py", title="18) The Recruit Action", icon=":european_castle:")
pray = st.Page("pray.py", title="19) The Pray Action", icon=":european_castle:")
conspire = st.Page("conspire.py", title="20) The Conspire Action", icon=":european_castle:")
commission = st.Page("commission.py", title="21) The Commission Action", icon=":european_castle:")
fortify = st.Page("fortify.py", title="22) The Fortify Action", icon=":european_castle:")
garrison = st.Page("garrison.py", title="23) The Garrison Action", icon=":european_castle:")
absolve = st.Page("absolve.py", title="24) The Absolve Action", icon=":european_castle:")
attack = st.Page("attack.py", title="25) The Attack Action", icon=":european_castle:")
convert = st.Page("convert.py", title="26) The Convert Action", icon=":european_castle:")
turns = st.Page("turns.py", title="27) Turns and Rounds", icon=":european_castle:")
paladins = st.Page("paladins.py", title="28) Paladins", icon=":european_castle:")
tavern = st.Page("tavern.py", title="29) Tavern Cards", icon=":european_castle:")
kings_orders = st.Page("kings_orders.py", title="30) The King's Orders", icon=":european_castle:")
kings_favours = st.Page("kings_favours.py", title="31) The King's Favours", icon=":european_castle:")
iconography = st.Page("iconography.py", title="32) Iconography", icon=":european_castle:")
scoring = st.Page("scoring.py", title="33) Scoring", icon=":european_castle:")



pg = st.navigation([why,
                    worker_placement,
                    aim,
                    setup,
                    townsfolk,
                    invaders,
                    silver_bronze,
                    provisions,
                    tax,
                    debt,
                    attributes,
                    workers,
                    suspicion,
                    actions,
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
                    convert,
                    turns,
                    paladins,
                    tavern,
                    kings_orders,
                    kings_favours,
                    iconography,
                    scoring
                
                    ])
pg.run()



