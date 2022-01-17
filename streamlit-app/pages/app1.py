import streamlit as st
def app():
    st.title("Welcome To Project Description of Garbage Image Classification")

    st.subheader("Objective :")
    st.write("The main Objective of this project is to use Machine Learning and Deep learning to categorize the garbage image into 6 different classes namely :")
    
    col1, col2, col3 = st.columns(3)
    col1.markdown("1. Cardboard", True)
    col2.markdown("2. Glass", True)
    col3.markdown("3. Metal", True)

    col4, col5, col6 = st.columns(3)
    col4.markdown("4. Paper", True)
    col5.markdown("5. Plastic", True)
    col6.markdown("6. Trash", True)

    st.subheader("Motivation :")
    st.markdown("This Project is created for the <b>Hack4Good Competition</b> presented by <b>IEEE CIS SBC - GHRCE.</b>", True)
    st.markdown("Visit the Hack4Good Home page <a href='https://hack4good.ieee-cis-sbc.org/'>here</a></b>", True)

    st.subheader("Role :")
    st.write("This is an Individual Project built with the help from multiple resourses Kaggle being one of them.")
    st.write("It took me over 5 days to successfully build and deploy this this End-To-End Project to production.")

    st.subheader("Data :")
    st.write("The Data used in this project is available on Kaggle.")
    st.markdown("Visit Kaggle for Data <a href='https://www.kaggle.com/asdasdasasdas/garbage-classification'>here</a>", True)
    st.write("The approximate size of the Data is 43MB. It contains 2,527 Image categorized in 6 classes.")

    st.subheader("Tech Used :")
    st.write("This is a Python based Garbage Image Classification project.")
    st.write("It involves use of multiple Python Packages. Most Important of which are :")

    col1, col2, col3 = st.columns(3)
    col1.markdown("1. Google Colab", True)
    col2.markdown("2. Keras", True)
    col3.markdown("3. Numpy", True)
    