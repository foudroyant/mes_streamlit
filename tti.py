import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import textwrap
from io import BytesIO

# Titre de l'application
st.title("Convertisseur de texte en image")

# Stocker le compteur d'images dans l'état de Streamlit
if "image_counter" not in st.session_state:
    st.session_state.image_counter = 0  # Initialiser le compteur

# Saisir le texte
user_text = st.text_area("Saisissez votre texte (max 100 caractères) :", max_chars=100)

# Vérifier si l'utilisateur a entré du texte
if user_text:
    # Largeur maximale du texte par ligne
    max_line_length = 30  # Ajustez selon la taille de l'image

    # Créer une image blanche
    image_width, image_height = 600, 400
    image = Image.new("RGB", (image_width, image_height), color="white")
    draw = ImageDraw.Draw(image)

    # Définir la police (remplacez le chemin de la police par une police existante sur votre système)
    try:
        font = ImageFont.truetype("arial.ttf", size=24)  # Arial par défaut
    except IOError:
        font = ImageFont.load_default()  # Police par défaut si Arial n'est pas disponible

    # Diviser le texte en plusieurs lignes si nécessaire
    wrapped_text = textwrap.fill(user_text, width=max_line_length)

    # Calculer la position pour centrer le texte
    text_width, text_height = draw.textbbox((0, 0), wrapped_text, font=font)[2:4]
    x = (image_width - text_width) // 2
    y = (image_height - text_height) // 2

    # Dessiner le texte sur l'image
    draw.multiline_text((x, y), wrapped_text, fill="black", font=font, align="center")

    # Afficher l'image générée
    st.subheader("Image générée contenant votre texte :")
    st.image(image)

    # Incrémenter le compteur d'images
    st.session_state.image_counter += 1
    image_name = f"text_image_{st.session_state.image_counter}.png"

    # Sauvegarder l'image dans un format compatible
    buffered = BytesIO()
    image.save(buffered, format="PNG")  # Sauvegarde au format PNG
    buffered.seek(0)

    # Bouton pour télécharger l'image avec un nom unique
    st.download_button(
        "Télécharger l'image",
        data=buffered,
        file_name=image_name,
        mime="image/png",
    )
