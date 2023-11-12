# PyMemoryFlow

This is a Streamlit web app which utilizes memory_profiler Python module to help developers visualize memory usage and locate memory leaks.

# Contents

<a href=https://github.com/ShreeluSantosh/GUIMemoryProfile/edit/main/README.md#how-it-works>How it works</a><br>
<a href=https://github.com/ShreeluSantosh/GUIMemoryProfile/edit/main/README.md#modules-and-libraries-used>Modules and Libraries used</a><br>
<a href=https://github.com/ShreeluSantosh/GUIMemoryProfile/edit/main/README.md#how-to-run>How to Run</a>

# How it works

The developer can upload a Python file to the web app. The file is analyzed and executed in a sandbox environment to get more insights into full-time memory usage. 

Currently, there are two tools available:

- Line-by-line Memory Usage
![Screenshot 2023-11-06 125901](https://github.com/ShreeluSantosh/GUIMemoryProfile/assets/94289402/43918bea-3820-4cff-8b8c-6cbe6d0d9b8e)

- Plotting memory usage over time
![Screenshot 2023-11-06 125935](https://github.com/ShreeluSantosh/GUIMemoryProfile/assets/94289402/ad766c1b-cb84-45a6-beaf-4e3e5250db74)


EDIT (06.11.2023) - I have added an option to download results from the above two tools.

I plan to add more new features in near future!

# Modules and Libraries used:
- streamlit
- streamlit_extras
- memory_profiler
- matplotlib
- os
- subprocess

# How to Run

- Clone the repository
~~~
git clone https://github.com/ShreeluSantosh/PyMemoryFlow.git
~~~
- Install the required modules from requirements.txt
~~~
pip install -r requirements.txt
~~~
- Run the root file (Introduction.py)
~~~  
streamlit run Introduction.py
~~~
