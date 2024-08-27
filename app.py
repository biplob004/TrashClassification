import streamlit as st
import torch
from torchvision import models
import torchvision.transforms as transform
from PIL import Image
import requests
from io import BytesIO

# Load the pre-trained model
model_path = 'resnet101.pth' 
model = torch.load(model_path) 
model.eval()  
model.to('cpu')

# Define image transformations
transformer = transform.Compose([
    transform.Resize((224, 224)),
    transform.ToTensor(),
    transform.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))
])

# Labels for classification
labels = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

# Streamlit application title and description
st.title("Trash Classification")
st.write("Upload an image of trash or paste an image URL, and the model will classify it.")

# File uploader for image input
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "webp"])

# Text input for image URL
image_url = st.text_input("Or paste an image URL here:")

predicted_class = None  # Initialize predicted_class variable

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
elif image_url:
    try:
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content)).convert('RGB')
    except Exception as e:
        st.error("Error loading image from URL. Please check the URL.")
        image = None
else:
    image = None

if image is not None:
    image_tensor = transformer(image).unsqueeze(0)  

    with torch.no_grad():  # Disable gradient calculation for inference
        outputs = model(image_tensor)
        _, predicted = torch.max(outputs, 1)

    predicted_class = labels[predicted.item()]

# Display the result with larger font above the image
if predicted_class:
    st.markdown(f"<h2 style='color: #4CAF50;'>Predicted class: {predicted_class}</h2>", unsafe_allow_html=True)

if image is not None:
    st.image(image, caption='Uploaded Image', use_column_width=True)

# Add some styling
st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f5;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)
