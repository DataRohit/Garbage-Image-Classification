import os
import streamlit as st
import plotly.express as px
from helpers import predictor

def app():
    st.write("# Garbage Image Classification")

    st.write("## Sample Images")

    col1, col2, col3 = st.columns(3)
    col1.image(os.path.join(os.getcwd(), "streamlit-app", "images", "cardboard.jpg"), caption='0 : Cardboard')
    col2.image(os.path.join(os.getcwd(), "streamlit-app", "images", "glass.jpg"), caption='1 : Glass')
    col3.image(os.path.join(os.getcwd(), "streamlit-app", "images", "metal.jpg"), caption='2 : Metal')

    col4, col5, col6 = st.columns(3)
    col4.image(os.path.join(os.getcwd(), "streamlit-app", "images", "paper.jpg"), caption='3 : Paper')
    col5.image(os.path.join(os.getcwd(), "streamlit-app", "images", "plastic.jpg"), caption='4 : Plastic')
    col6.image(os.path.join(os.getcwd(), "streamlit-app", "images", "trash.jpg"), caption='5 : Trash')

    st.write("## Upload Image in .jpg format")
    uploaded_image = st.file_uploader("", type=["jpg"])

    st.write("## Uploaded Image")

    if uploaded_image:
        st.image(uploaded_image)

        button = st.button("Make Prediction", key=None)

        if button:
            prediction, predicted_class = predictor.predict(uploaded_image)

            labels = {0: 'cardboard', 1: 'glass', 2: 'metal', 3: 'paper', 4: 'plastic', 5: 'trash'}

            classes=[]
            prob=[]
            for i,j in enumerate (prediction[0], 0):
                classes.append(labels[i].capitalize())
                prob.append(round(j*100,2))

            fig = px.bar(x=classes, y=prob,
                         text=prob, color=classes,
                         labels={"x":"Material", "y":"Probability(%)"})

            st.markdown("#### Probability Distribution Bar Chart", True)
            st.plotly_chart(fig)

            st.markdown(f"#### I am `{max(prob)}%` sure that the material in the image is `{predicted_class.capitalize()}`", True)
            
    else:
        st.write("#### No Image Found. Pls Upload the Image.")