import streamlit as st
import cv2
from keras.models import load_model
from PIL import Image
import numpy as np
from skimage.io import imread, imsave
from skimage.util import img_as_ubyte
from roboflow import Roboflow
import subprocess

# Placeholder YOLO function
def yolo(image_path):
    st.write("YOLO function executed on the image at path:", image_path)

# Function to execute a Python file
def execute_python_file(file_path):
    try:
        completed_process = subprocess.run(['python', file_path], capture_output=True, text=True)
        if completed_process.returncode == 0:
            st.write("Execution successful.")
            st.write("Output:")
            st.write(completed_process.stdout)
        else:
            st.write(f"Error: Failed to execute '{file_path}'.")
            st.write("Error output:")
            st.write(completed_process.stderr)
    except FileNotFoundError:
        st.write(f"Error: The file '{file_path}' does not exist.")

# File path to the external Python file
file_path = 'esti.py'
execute_python_file(file_path)

# Displaying an image
img = imread("images.jpg")
st.image(img, caption="Prediction Image")

# Function to start processing
def start(file):
    if file:
        # Load and display the uploaded image
        image = Image.open(file)
        st.write("Input image received")
        st.image(image, caption="Uploaded Image")

        # Convert the image to uint8 format for further processing
        img_ubyte = img_as_ubyte(np.array(image))
        img_path = 'images.jpg'
        imsave(img_path, img_ubyte)

        # Call the YOLO function on the saved image
        yolo(img_path)

# Title and description
st.title("Food Calorie Estimator")
st.subheader("Upload your Food Image")

# File uploader for the image input
file = st.file_uploader("Enter the image", type=["jpg", "jpeg", "png"])

# Check if file is uploaded and start processing
if file:
    st.info("File uploaded successfully.")
    try:
        start(file)
    except Exception as e:
        st.write(f"An error occurred: {e}")

# Button to run YOLO function on the processed image if uploaded
button = st.button('Enter')
if button and file:
    yolo('images.jpg')
