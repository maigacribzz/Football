import random
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, request
import streamlit as st


data = {"messi":0,"ronaldo":0}

bar_charts = st.dataframe(data)
count =0
user_input = st.form(key=f"userinput{str(count)}")
user_input = st.text_input("Enter your text:")


with user_input:
    empty_input = st.empty()
    submit_button = st.form_submit_button("Submit")
with  bar_charts:
    empty_barchar = st.empty()
##df_inital = pd.DataFrame()

while True:
    print(data)
    with empty_input:
        user_name = st.text_input("enter 0 for ronaldo or 1 for messi",key=f"userinput{str(count)}")
        import time
        time.sleep(3)
        import streamlit as st

    with empty_input:
        empty_input.form(key=f"userinput{str(count)}")
        
    #user_name = str(random.randint(0,3))
        if user_input== "0":
            data['ronaldo'] = data['ronaldo'] +1
        elif user_input=="1":
            data['messi'] = data['messi'] + 1
    
    df = pd.DataFrame([data])
    #combined_df = pd.concat([df_inital,df])
    print(df)
    with empty_barchar:
        empty_barchar.write(df)
    #df_inital = combined_df
    count+=1