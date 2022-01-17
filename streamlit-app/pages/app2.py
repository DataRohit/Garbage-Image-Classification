import streamlit as st
from helpers import predictor

def app():
    st.write("# Garbage Image Classification")

    st.write("## Sample Images")

    col1, col2, col3 = st.columns(3)
    col1.image("https://i.ibb.co/XWq96B1/cardboard.jpg", caption='0 : Cardboard')
    col2.image("https://i.ibb.co/9Y3hscx/glass.jpg", caption='1 : Glass')
    col3.image("https://i.ibb.co/2ZHxnc7/metal.jpg", caption='2 : Metal')

    col4, col5, col6 = st.columns(3)
    col4.image("https://i.ibb.co/pbvjX4Y/paper.jpg", caption='3 : Paper')
    col5.image("https://i.ibb.co/Wczj3VH/plastic.jpg", caption='4 : Plastic')
    col6.image("https://i.ibb.co/GdxYMFp/trash.jpg", caption='5 : Trash')

    st.write("## Upload Image in .jpg format")
    uploaded_image = st.file_uploader("", type=["jpg"])

    st.write("## Uploaded Image")

    if uploaded_image:
        st.image(uploaded_image)

        button = st.button("Make Prediction", key=None)

        if button:
            predicted_class = predictor.predict(uploaded_image)
            st.markdown(f"<h4>{predicted_class.capitalize()} Detected!!</h4>", True)
    else:
        st.write("#### No Image Found. Pls Upload the Image.")