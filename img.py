import streamlit as st
from PIL import Image, ImageEnhance

# Titre de l'application
st.title("Application de traitement d'images")

# Section de chargement de l'image
uploaded_image = st.file_uploader("Téléchargez une image", type=["jpg", "jpeg", "png"])

if uploaded_image:
    # Ouvrir l'image
    image = Image.open(uploaded_image)
    
    # Afficher l'image d'origine
    st.subheader("Image d'origine")
    st.image(image, caption="Image téléchargée", use_column_width=True)
    
    # Appliquer un traitement simple (par exemple, ajuster la luminosité)
    enhancement_factor = st.slider("Ajustez la luminosité", 0.5, 3.0, 1.0)
    enhancer = ImageEnhance.Brightness(image)
    enhanced_image = enhancer.enhance(enhancement_factor)
    
    # Afficher l'image traitée
    st.subheader("Image après traitement")
    st.image(enhanced_image, caption="Image traitée", use_column_width=True)
