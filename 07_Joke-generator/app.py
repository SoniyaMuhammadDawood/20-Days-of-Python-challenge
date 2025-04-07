import streamlit as st
import requests
import base64
import os


def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return encoded

# --- Set background image using base64 ---
def set_background(image_file):
    base64_img = get_base64_image(image_file)
    page_bg = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{base64_img}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

# --- Random joke function ---
def random_joke_generator():
    """Fetch a random joke from API"""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']}  \n\n{joke_data['punchline']}"
        else: 
            return "Failed to fetch a joke. Please try again later."
    except: 
        return "Why did the programmer quit his job?\nBecause he didn't get arrays!"

# --- Main app ---
def main():
    set_background("image.png")  # Make sure this file exists in the same folder
    st.title("🎭 Random Joke Generator")
    st.write("Click the button below to generate a random joke")

    if st.button("Tell me a Joke!"):
        joke = random_joke_generator()
        st.success(joke)

    st.divider()

    st.markdown(
        """<div style="text-align:center;">
        <p>🃏 Joke from Official Joke API</p>
        <p>Built with 💞 by Soniya using Streamlit</p>
        </div>""",
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
