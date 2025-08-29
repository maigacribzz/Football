import streamlit as st
import pandas as pd
import base64

# ---- Loading assets ----
def set_bg_hack(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.
 
    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "png"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         
         </style>
         """,
         unsafe_allow_html=True
    )


set_bg_hack("./players.png")



# --- Initialize state for player data---
if "data" not in st.session_state:
    st.session_state.data = {"messi": 0,"neymar": 0, "ronaldo": 0}


st.title(":red[Messi vs Ronaldo Votes ⚽]", help="Click any button to select preferred player", width="stretch")

# --- Buttons for input ---
st.subheader(":blue[Select multiple clicks to populate barchart below]", divider="green")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Vote Messi 🐐"):
        st.session_state.data["messi"] += 1

with col2:
    if st.button("Vote Neymar 🔥"):
        st.session_state.data["neymar"] += 1

with col3:
    if st.button("Vote Ronaldo 🔥"):
        st.session_state.data["ronaldo"] += 1

# --- Display updated data ---
df = pd.DataFrame([st.session_state.data])
st.write(":red[Current Votes]")
st.dataframe(df)

# --- Bar chart ---
st.bar_chart(df.T)
