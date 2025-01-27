import streamlit as st
import pytesseract
from PIL import Image
import os

# Set up the Tesseract command path (ensure Tesseract is installed on your Mac)
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

# Title for the Streamlit app
st.title('Text Extraction from Image')

# File uploader
uploaded_file = st.file_uploader("Choose a JPG file", type=['jpg'])

if uploaded_file is not None:
    # Save the uploaded file as image.jpg
    with open("image.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success("File uploaded successfully and saved as image.jpg.")
    
    # Open the saved image
    image = Image.open("image.jpg")
    
    # Tesseract configuration
    myconfig = r"--oem 3 --psm 3"

    # Extract text from the image
    text = pytesseract.image_to_string(image, config=myconfig)
    
    # Display the extracted text
    st.text_area("Extracted Text", text)
    
    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_container_width=True)
