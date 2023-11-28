import streamlit as st
from st_pages import Page, show_pages

st.set_page_config(page_title="Home | IncidentCraft")

show_pages(
    [
        Page("Home.py", "Home", "🏠"),
        Page("pages/Identify.py", "Identify", "📃"),
        Page("pages/Protect.py", "Protect", "🔐"),
        Page("pages/Detect.py", "Detect", "🔍"),
        Page("pages/Respond.py", "Respond", "🔊"),
        Page("pages/Recover.py", "Recover", "📈"),
    ]
)

st.title("IncidentCraft")
tab1, tab2 = st.tabs(["Welcome", "Login"])

with tab1:
   st.header("Welcome")
with tab2:
   st.header("Login")