import streamlit as st
import requests


st.set_page_config(page_title="Random Joke Generator", page_icon="😄", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right,#b6fbff, #6dd5ed );
    }
    </style>
    """,
    unsafe_allow_html=True
)


def random_joke_generator():
    """Fetch a random joke from api"""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']}  \n \n {joke_data['punchline']}"
        else: 
            return "Failed to fetch a joke, Please try again later"
    except: 
        return "Why did the programmer quite his job? \n because he didn't get arrays!"

def main():
    st.title("*🎭Random Joke Generator*")
    st.write("**Click the button brlow to generate a random joke**")

    if st.button("**Tell me a Joke!**"):
        joke = random_joke_generator()
        st.info(joke)
    st.divider()

    st.markdown(
        """ <div style="text-align:center;"
        <p> <b> Joke from official joke api <b/> </p>
        <p><b> Build with 💞 by soniya using streamlit </b> </p>
            </div> 
""",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main() 