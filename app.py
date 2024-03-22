import streamlit as st
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import ollama
import streamlit as st
import textwrap


def main():
    # Chargez le modèle et le processeur
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

    st.title("Générateur de story of légendes d'images avec BLIP")

    # Widget Streamlit pour charger une image
    uploaded_image = st.file_uploader("Choisissez une image...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Affichez l'image chargée
        image = Image.open(uploaded_image).convert('RGB')
        st.image(image, caption='Image chargée', use_column_width=True)
        
        # Génération de légende conditionnelle
        text = "a photography of"
        if st.button("Générer la légende"):
            with st.spinner("Génération en cours..."):
                inputs = processor(image, text, return_tensors="pt")
                out = model.generate(**inputs)
                caption = processor.decode(out[0], skip_special_tokens=True)
                st.success(f"Légende: {caption}")
                output_text = st.empty()
                if caption:
                    m = 'generate story for children about '+ caption
                    stream =ollama.chat(
                    model='llama2',
                    messages=[{'role':'user','content':m}],
                    stream= True
                )
                    full_text = ""

                    for chunk in stream:
                        if 'message' in chunk:
                            # Utiliser st.write pour afficher le contenu du message dans l'interface Streamlit
                            full_text  += chunk['message']['content'] + " "
                            # Utiliser textwrap pour insérer des retours à la ligne après chaque 70 caractères
                            wrapped_text = textwrap.fill(full_text, width=70)
                            output_text.text(wrapped_text)

                        else:
                            st.write("Réponse inattendue:", chunk)
                        print(chunk['message']['content'],end='',flush=True)
                

if __name__ == "__main__":
    main()