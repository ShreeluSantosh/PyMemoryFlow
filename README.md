# GUIMemoryProfile

This is a Streamlit web app which utilizes memory_profiler Python module to help developers visualize memory usage and locate memory leaks.

# How it works

The developer can upload a Python file to the web app. The file is analyzed and executed in a sandbox environment to get more insights into full-time mmeory usage. 

Currently, there are two tools available:

- Line-by-line memory usage
- Plotting memory usage over time

I plan to add more new features in near future!

# Modules and Libraries used:
- streamlit
- streamlit_extras
- memory_profiler
- matplotlib
- os
- subprocess

# How to Run

- install the required modules from requirements.txt
- run the root file (Introduction.py)
