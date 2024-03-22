# License Plate Recognition App

This web application allows users to upload images containing animals, food plates,dinosaur. Normally it will allow you to detect the content of image and generate legend and a fun storry for children.

## overview

The app utilizes computer  models for image to text  detection (Salesforce/blip-image-captioning-large)  to extract text from the images. add to that, it employs a  general model that create a fun storry to convert the recognized text into audio, providing an accessible user experience.

## screen shoot of app

## Features

- Upload images containing animals object of nature 
- Detect the content  in the uploaded images.
- generate text from the detected image.

## Installation

To run the app locally, follow these steps:

 Clone the repository:

    ```bash
    git clone https://github.com/taiebrafik1998/story_creator_ia.git
    ```

Navigate to the project 

Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
run this command 

```bash
    docker run -d -v ollama:/root/.ollama -p 9004:9004 --name ollama ollama/ollama
    docker exec -it ollama ollama run llama2
    ```

## Usage

To run the app:

```bash
streamlit run app.py
```

## Librairie utiliser dans projet

The app relies on the following libraries:

- [llama2]
- [Pillow==10.2.0]
- [streamlit==1.32.2]
- [torch==2.2.1]
- [transformers](https://streamlit.io/)
- [PyTorch](https://pytorch.org/)
-

## huggingFace repo

You can test the app [ici](https://huggingface.co/spaces/rafik-taieb98/story_telling) on the Hugging Face Spaces platform.




---
title: Story Telling
emoji: 🌍
colorFrom: red
colorTo: blue
sdk: streamlit
sdk_version: 1.32.2
app_file: app.py
pinned: false
---

