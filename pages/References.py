import streamlit as st
from streamlit_extras.let_it_rain import rain 

st.set_page_config(
    page_title="References",page_icon = "📜")

st.sidebar.success("Select a tool or a page to jump to.")
st.title("References")

st.write("memory profiler - https://pypi.org/project/memory-profiler/")

def example():
    rain(
        emoji="😄",
        font_size=50,
        falling_speed=5,
        animation_length="infinite",
    )
example()
