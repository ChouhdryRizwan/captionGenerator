import os
from PIL import Image, UnidentifiedImageError
import streamlit as st
from streamlit_option_menu import option_menu
from gemini_utility import gemini_pro_vision_response

# Get the working directory
working_dir = os.path.dirname(os.path.abspath(__file__))

# Streamlit page configuration
st.set_page_config(
    page_title="Caption Generator",
    page_icon="🤖",
    layout="centered",
)

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        'Caption',
        ['Image Captioning'],
        menu_icon='robot',
        icons=['chat-dots-fill', 'image-fill', 'textarea-t', 'patch-question-fill'],
        default_index=0
    )

# Image Captioning page
if selected == "Image Captioning":
    st.title("📷 Caption Generator")

    # Image uploader
    uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

    # Generate Caption button
    if st.button("Generate Caption"):
        if uploaded_image is None:
            st.error("Please upload an image file before generating a caption.")
        else:
            try:
                # Open and process the uploaded image
                image = Image.open(uploaded_image)

                # Display the image in a resized format
                col1, col2 = st.columns(2)
                with col1:
                    resized_img = image.resize((800, 500))
                    st.image(resized_img)

                # Define the default prompt for captioning
                default_prompt = "Write a pro level suitable caption with proper hashtags for social media."

                # Get the caption using Gemini AI
                caption = gemini_pro_vision_response(default_prompt, image)

                # Display the generated caption
                with col2:
                    st.info(caption)

            except UnidentifiedImageError:
                st.error("The uploaded file is not a valid image. Please upload a valid JPG, JPEG, or PNG file.")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")
