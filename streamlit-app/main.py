from pages import app1, app2, app3

import streamlit as st
PAGES = {
    "Project Description": app1,
    "Model Demo": app2,
    "About Me": app3,
}

st.sidebar.title('Garbage Image Classification')
selection = st.sidebar.radio("Navigate To", list(PAGES.keys()))
page = PAGES[selection]
page.app()