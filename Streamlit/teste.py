# Tutorial de Streamlit no youtube
# https://www.youtube.com/watch?v=_9WiB2PDO7k&list=PLJ39kWiJXSixyRMcn3lrbv8xI8ZZoYNZU

import streamlit as st

# Text;Title
st.title("Streamlit Tutorials")

# Header/Subheader
st.header("This is a header")
st.subheader("This is a subheader")

# Text
st.text("Hello Streamlit")

# Markdown
st.markdown("### This is a Markdown")

# Error/Colorful Text
st.success("Sucessful")
st.info("Information!")
st.warning("This is a warning")
st.error("This is an error Danger")
st.exception("NameError('name three not defined')")