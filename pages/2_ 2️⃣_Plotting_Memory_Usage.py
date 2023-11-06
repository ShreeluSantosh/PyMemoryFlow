from streamlit_extras.sandbox import sandbox
import streamlit as st

st.set_page_config(page_title="Plot Memory Usage Profile", page_icon = "📜")
st.sidebar.success("Select a tool or a page to jump to.")
st.title("Plot Memory Usage Profile")

def embedded_app():
    from memory_profiler import memory_usage
    import matplotlib.pyplot as plt

    uploaded_file = st.file_uploader("Upload a Python file (.py)", type=['py'])

    def profile_memory(func_to_run, *args, **kwargs):
        mem_usage = memory_usage((func_to_run, args, kwargs), interval=0.1, timeout=None, include_children=True, retval=True)
        mem, retval = mem_usage[0], mem_usage[1]
        return mem, retval

    if uploaded_file:
        st.write("File Uploaded!")
        if st.button("Profile"):
            with st.spinner("Analyzing..."):
                file_content = uploaded_file.read().decode('utf-8')
                local_ns = {}
                exec(file_content, local_ns)
                
                if 'main' in local_ns:
                    mem_usage, retval = profile_memory(local_ns['main'])
                    with st.spinner("Plotting..."):
                        plt.figure(figsize=(8,4))
                        plt.plot(mem_usage, '-o')
                        plt.title('Memory usage over time')
                        plt.xlabel('Time step')
                        plt.ylabel('Memory usage (MiB)')
                        plt.grid(True)
                        st.pyplot(plt)
                        fn = "profile_plot.png"
                        plt.savefig(fn)

                        with open(fn, "rb") as img:
                            st.download_button(
                                label="Download plot",
                                data=img,
                                file_name=fn,
                                mime="image/png"
                            )                        
                else:
                    st.error("No 'main' function found in the uploaded script.")

with st.spinner("Creating sandbox..."):
    sandbox(embedded_app())  