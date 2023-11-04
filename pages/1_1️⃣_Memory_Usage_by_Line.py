from streamlit_extras.sandbox import sandbox
import streamlit as st
st.set_page_config(page_title="Line-by-Line Memory Usage", page_icon = "📜")
st.sidebar.success("Select a tool or a page to jump to.")
st.title("Line-by-Line Memory Usage")

def embedded_app():
    import os, subprocess

    def analyze(text_filename):
        command = f"py -m memory_profiler {text_filename}"
        process = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                
        st.code(process.stdout)

        if os.path.exists(text_filename):
            os.remove(text_filename)


    uploaded_file = st.file_uploader("Upload a Python file (.py)", type=['py'], accept_multiple_files=False)

    if uploaded_file:
        st.write("File Uploaded!")
        if st.button("Profile"):
            file_content = uploaded_file.read().decode('utf-8')
            updated_lines = []
            updated_lines.append("from memory_profiler import profile\n")
            
            for line in file_content.split("\n"):
                if line.lstrip().startswith('def'):
                    updated_lines.append("@profile")
                updated_lines.append(line)
            
            updated_content = "\n".join(updated_lines)
            
            text_filename = "updated_app.py"
            with open(text_filename, "w", encoding='utf-8') as text_file:
                text_file.write(updated_content)
            
            with st.spinner("Profiling..."):
                analyze(text_filename)

with st.spinner("Creating sandbox..."):
    sandbox(embedded_app())           