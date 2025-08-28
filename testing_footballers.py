import streamlit as st
import pandas as pd

# --- Initialize state ---
if "data" not in st.session_state:
    st.session_state.data = {"messi": 0, "ronaldo": 0}

st.title("Messi vs Ronaldo Votes ⚽")

# --- Input form ---
with st.form("user_form"):
    user_input = st.text_input("Enter 0 for Ronaldo or 1 for Messi")
    submit_button = st.form_submit_button("Submit")

# --- Process input ---
if submit_button:
    if user_input == "0":
        st.session_state.data["ronaldo"] += 1
    elif user_input == "1":
        st.session_state.data["messi"] += 1
    else:
        st.warning("Please enter either 0 (Ronaldo) or 1 (Messi).")

# --- Display updated data ---
df = pd.DataFrame([st.session_state.data])
st.write("### Current Votes")
st.dataframe(df)

# Optional: Show a bar chart
st.bar_chart(df.T)
