import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.let_it_rain import rain

st.set_page_config(page_title="Home | PyMemoryFlow", page_icon = "📜")
st.title("PyMemoryFlow 📜")
tab1, tab2, tab3 = st.tabs(["Welcome", "Tools", "About"])

with tab1:
   st.header("Welcome")
   st.write("Upload and get a detailed report on your Python app's memory usage!")
   expander = st.expander("Why Memory Profiling?")
   expander.write("Memory leaks are considered one of the menaces app developers face while developing their Python-based applications, especially given the language's high memory consumption.")
   expander.write("According to OWASP, a memory leak is an unintentional form of memory consumption whereby the developer fails to free an allocated block of memory when no longer needed. The consequences of such an issue depend on the application itself.")

   expander = st.expander("Why PyMemoryFlow?")
   expander.write("This interactive web app, allows the programmers wishing to evaluate their Python code's memory usage, to have it analyzed.")
   expander.write("The web app generates a line-by-line analysis of the program, and also includes a 'Download Report' feature.")

with tab2:
   st.header("Available Tools:")
   col1, col2 = st.columns(2)
   with col1:
    st.subheader("1. Line-by-line Memory Usage")
    st.write("Returns a line-by-line analysis of memory usage and increment of the Python script")
    if st.button("Use it!"):
      switch_page("line by line memory usage")
   with col2:
    st.subheader("2. Plotting Memory Usage")
    st.write("Generates a time-memory usage plot")
    if st.button("Get plot here!"):
      switch_page("plotting memory usage")

   st.subheader("More features will be added in near future!")
with tab3:
  st.header("About the tool:")
  st.write("This web app uses the following techn stack:")
  st.write("1. Python")
  st.write("2. Streamlit")
  st.write("3. matplotlib")
  st.write("4. memory_profiler - a Python library")
