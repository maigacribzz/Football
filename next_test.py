import streamlit as st
import pandas as pd

# --- Initialize state ---
if "data" not in st.session_state:
    st.session_state.data = {"messi": 0, "ronaldo": 0}

st.title("Messi vs Ronaldo Votes ⚽")

# --- Buttons for input ---
col1, col2 = st.columns(2)

with col1:
    if st.button("Vote Messi 🐐"):
        st.session_state.data["messi"] += 1

with col2:
    if st.button("Vote Ronaldo 🔥"):
        st.session_state.data["ronaldo"] += 1

# --- Display updated data ---
df = pd.DataFrame([st.session_state.data])
st.write("### Current Votes")
st.dataframe(df)

# --- Bar chart ---
st.bar_chart(df.T)
