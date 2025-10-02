import streamlit as st
import streamlit.components.v1 as components
import os

# Set page configuration to use the full width of the screen for an immersive experience.
st.set_page_config(layout="wide")

# This code constructs the absolute path to the 'index.html' file.
# It finds the directory where this 'app.py' script is located and then looks for 'index.html'
# in that same directory. This method is reliable for both local execution and deployment on Streamlit Cloud.
html_file_path = os.path.join(os.path.dirname(__file__), 'index.html')

# It's good practice to handle potential errors, like the HTML file being missing.
try:
    # Open and read the entire content of the HTML file.
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_code = f.read()
except FileNotFoundError:
    # If the file is not found, display a user-friendly error message in the app.
    st.error("Fatal Error: 'index.html' not found.")
    st.info("Please ensure the 'index.html' file is present in the same GitHub repository folder as this 'app.py' script.")
    # Stop the script execution if the file is missing.
    st.stop()

# Use Streamlit's 'components.html' function to render the HTML code within the app.
# We set a height and enable scrolling to ensure the entire page is accessible.
components.html(html_code, height=900, scrolling=True)

