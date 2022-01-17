from pages import app1, app2

import streamlit as st
PAGES = {
    "Project Description": app1,
    "Model Demo": app2
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Navigate To", list(PAGES.keys()))
page = PAGES[selection]
page.app()