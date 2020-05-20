import streamlit as st
import face_recognition as fr
import time
from PIL import Image
import os

# Set the headers
description = """ # Real-time Face Detection Project
In this project, I use OpenCV and Viola-Jones Algorithm to build a simple face detection system that works in real-time.
The models seek to detect faces, eyes and mouth.
"""
model_description = None

st.markdown(description)

# ---------- Side bar ----------#
st.sidebar.header("Select the input type")
input_type = st.sidebar.radio('', ['Image demo', 'Image upload', 'Video from webcam'])

st.sidebar.header("Select the model")
model = st.sidebar.radio('', ['Viola–Jones'])
st.sidebar.markdown("*** More models comming soon ... ***")

st.sidebar.header("About")
st.sidebar.info("""\
        * Create by: [Patrick Alves](https://www.linkedin.com/in/cpatrickalves/)

        * source code: [GitHub](https://github.com/cpatrickalves/cv-realtime-face-detection)
    """)

# Get the model
if model == 'Viola–Jones':
    detect = fr.detect_from_img_file

    model_description = """
    ---
    ### Viola–Jones object detection framework

    The Viola–Jones object detection framework is the first object detection framework to provide competitive object detection rates
    in real-time proposed in 2001 by Paul Viola and Michael Jones.
    * Although it can be trained to detect a variety of object classes, it was motivated primarily by the problem of face detection.
    * To make the task more manageable, Viola–Jones requires full view frontal upright faces.

    <div style="text-align: right"> source: <a href="https://en.wikipedia.org/wiki/Viola%E2%80%93Jones_object_detection_framework">Wikipedia</a> </div>

    ---
    """

st.markdown(model_description, unsafe_allow_html=True)

# --------- Image demo ------------#
if input_type == 'Image demo':

    st.markdown('### Image demo')

    # Get the list of images available
    images = os.listdir('images')
    # filter the output images
    images = [img for img in images if 'output' not in img]
    # Get selection
    image = st.radio('Choose image:', options=images)

    selected_image = Image.open(f'images/{image}')
    st.image(selected_image, use_column_width=True)

    if st.button('Detect faces'):
        result = detect(f'images/{image}')
        output_image = Image.open(result)
        st.image(output_image, use_column_width=True)


# --------- Image upload ------------#
if input_type == 'Image upload':

    uploaded = 'uploads/file.jpg'
    # Clean uploads folder
    if os.path.exists(uploaded):
        os.remove(uploaded)

    st.markdown('### Image demo')
    # Allow file upload
    uploaded_file = st.file_uploader("", type=['jpg', 'jpeg', 'png'])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        image.save(uploaded)

    # Detect faces
    if st.button('Detect faces'):
        result = detect(uploaded)
        output_image = Image.open(result)
        st.image(output_image, use_column_width=True)


# --------- Video from webcam ------------#
if input_type == 'Video from webcam':

    st.markdown('## Comming soon ...')