import streamlit as st

st.set_page_config(
    page_title="Memory Profiling",
    page_icon = "📜"
)

st.sidebar.success("Select a tool or a page to jump to.")
st.title("Welcome")
st.markdown("Upload and get a detailed report on your Python app's memory usage!")
st.subheader("Memory Usage by Line")
st.markdown("Returns a line-by-line analysis of memory usage and increment of the Python script")
st.subheader("Plotting Memory Usage")
st.markdown("Returns a time-memory usage plot")
st.write("More fearures will be added in near future!")
