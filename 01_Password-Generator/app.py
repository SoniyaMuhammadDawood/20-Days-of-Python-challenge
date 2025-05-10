import streamlit as st
import random
import string

# Function to generate password
def generate_password(length, use_digits, use_characters):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_characters:
        characters += string.punctuation

    return "".join(random.choice(characters) for _ in range(length))

# Initialize Session State for Password History
if "password_history" not in st.session_state:
    st.session_state.password_history = []

# UI for app
st.set_page_config(page_title="Password Generator", page_icon="🎰", layout="centered")
st.title("🔐 Password Generator App")


st.markdown(
    """
    <style>
    /* Main Page Background */
    .stApp {
        background-color: #91DDCF; 
    }
    
    /* Sidebar Background */
    [data-testid="stSidebar"] {
        background-color: #64CCC5;  
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Header
st.sidebar.header("**📜 Your Password History**")

# User input controls
length = st.slider("**Select password range**:", max_value=28, min_value=8, value=12)
use_digits = st.checkbox("**Include Digits (0-9)**")
use_characters = st.checkbox("**Include Special Characters (!@#$%)**")

# Generate Password Button
if st.button("**Generate Password**"):
    password = generate_password(length, use_digits, use_characters)
    st.success(f"**Your password**: `{password}` ")

    # Store the password in history (only last 10)
    st.session_state.password_history.insert(0, password)
    st.session_state.password_history = st.session_state.password_history[:10]

# Display Password History in Sidebar
if st.session_state.password_history:
    for idx, pwd in enumerate(st.session_state.password_history):
        st.sidebar.markdown(
            f"<p style='word-wrap:break-word; background-color: #FBF3B9; padding: 5px;' >{idx+1}. {pwd} </p>", 
            unsafe_allow_html=True
        )
