# Story for children ia App

This web application allows users to upload images containing animals, food plates,dinosaur. Normally it will allow you to detect the content of image and generate legend and a fun storry for children.
<img width="356" alt="capture" src="https://github.com/taiebrafik1998/story_creator_ia/assets/84631421/61317e0c-103c-4200-a353-a8d5a298db3a">

## overview

The app utilizes computer  models for image to text  detection (Salesforce/blip-image-captioning-large)  to generat text from the images. add to that, it employs a  general model that create a fun storry for childreen .

## screen shoot of app
<img width="924" alt="first" src="https://github.com/taiebrafik1998/story_creator_ia/assets/84631421/8e908ff5-f159-4303-ab40-3ec5397d43e9">

<img width="406" alt="second" src="https://github.com/taiebrafik1998/story_creator_ia/assets/84631421/9ca525bb-c99d-4875-8b11-a2f9e202c403">


## Features

- Upload images containing animals object of nature 
- Detect the content  in the uploaded images.
- generate text from the detected image.

## Installation

To run the app locally, follow these steps:

 Clone the repository:

    ```
    git clone https://github.com/taiebrafik1998/story_creator_ia.git
    ```

Navigate to the project 

Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```
run this command 

```
    docker run -d -v ollama:/root/.ollama -p 9004:9004 --name ollama ollama/ollama
    docker exec -it ollama ollama run llama2
    ```

## Runing app
the application use stream lite so to run it you will need to:

```
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

You can test the app [huggingface.co](https://huggingface.co/spaces/rafik-taieb98/story_telling) on the Hugging Face Spaces platform.




---

---

