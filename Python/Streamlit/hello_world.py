import streamlit as st

st.write("# Hello World")

st.write("To run this streamlit - just run")
st.write("```python\n" + "streamlist run hello_world.py\n" + "```")

st.write("# Advanced stuff")

countries = st.multiselect(
    "Choose countries", 
    ["China", "United States of America", "Israel", "Spain"], 
    ["Israel", "United States of America"]
)
