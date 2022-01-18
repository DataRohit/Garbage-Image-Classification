import streamlit as st
import os

def app():
    st.title("Garbage Image Classification")

    st.subheader("Objective :")
    st.markdown("The main Objective of this project is to use `Machine Learning` and `Deep learning` to categorize the garbage image into 6 different classes namely :", True)
    
    col1, col2, col3 = st.columns(3)
    col1.markdown("1. Cardboard", True)
    col2.markdown("2. Glass", True)
    col3.markdown("3. Metal", True)

    col4, col5, col6 = st.columns(3)
    col4.markdown("4. Paper", True)
    col5.markdown("5. Plastic", True)
    col6.markdown("6. Trash", True)

    st.markdown("<hr/>", True)

    st.subheader("Motivation :")
    st.markdown("This Project is created for the <b>Hack4Good Competition</b> presented by <b>IEEE CIS SBC - GHRCE.</b>", True)
    st.markdown("Visit the Hack4Good Home page [Hack4Good](https://hack4good.ieee-cis-sbc.org/)", True)

    st.markdown("<hr/>", True)

    st.subheader("Role :")
    st.markdown("This is an `Individual Project` built with the help from multiple resourses Kaggle being one of them.", True)
    st.markdown("It took me over 5 days to successfully build and deploy this this `End-To-End Project` to production.", True)

    st.markdown("<hr/>", True)

    st.subheader("Data :")
    st.markdown("The Data used in this project is available on Kaggle.")
    st.markdown("Visit Kaggle for Data [Kaggle Data](https://www.kaggle.com/asdasdasasdas/garbage-classification)", True)
    st.markdown("The approximate size of the Data is 43MB. It contains `2,527 Images categorized in 6 classes.`", True)

    st.markdown("<hr/>", True)

    st.subheader("Tech Used :")
    st.markdown("This is a `Python` based Garbage Image Classification project.", True)
    st.markdown("It involves use of multiple Python Packages. Most Important of which are :", True)

    col1, col2, col3 = st.columns(3)
    col1.markdown("`1. Google Colab`", True)
    col2.markdown("`2. Keras`", True)
    col3.markdown("`3. Numpy`", True)

    st.markdown("<hr/>", True)

    st.subheader("Description :")
    st.markdown("This Project uses `Fine Tuned InceptionV3 Model` which is a Pre-Trained CNN Model from Keras.", True)
    st.markdown("It Gave the `Highest Accuracy of 96%` while classifying image from test set.", True)

    st.markdown("<hr/>", True)

    st.subheader("Folder Structure")
    st.image(os.path.join(os.getcwd(), "streamlit-app", "images", "folders.jpg"), caption="Basic Folder Structure")
    st.markdown("This is the Basic Folder Structure for the project. Full folder structure and filed are available in my github repository.", True)

    st.markdown("<hr/>", True)

    st.subheader("Code :")
    st.markdown("Full code and files for this project are availabe on my github repository [GitHub Repo](https://github.com/DataRohit/Garbage-Image-Classification)", True)
    