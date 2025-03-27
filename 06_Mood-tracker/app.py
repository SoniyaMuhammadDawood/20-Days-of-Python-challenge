import streamlit as st    # For creating web interface
import pandas as pd       # For data manupulating
import datetime           # For handling dates
import csv                # For creating and writing csv file
import os                 # For file operation
import base64


def get_base64_of_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()
# Add background image using st.image and CSS
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/png;base64,{get_base64_of_image("image.png")});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Define the file name & storing the mood data
MOOD_FILE = "mood_log.csv"


# Function to read mood data fro csv file
def load_mood_data():
    # Check if the file exixts
    if not os.path.exists(MOOD_FILE):
        # If no file exixts, create a empty dataframe with colunms
        return pd.DataFrame(columns=["Date", "Mood"])
    # Read the csv file & return the exixting data
    return pd.read_csv(MOOD_FILE)

# Function to add new mood entry to the csv file
def save_mood_data(date, mood):
    # Open file in append mode
    with open(MOOD_FILE, "a") as file:
        # Add csv writer
        writer = csv.writer(file)
        # add new mood entry to the csv file
        writer.writerow([date, mood])

st.title("Mood Tracker")

# Get today state
today = datetime.date.today()

st.subheader("How are your feeling today?")
mood = st.selectbox("Select your mood",["Happy", "Sad", "Angry", "Netural"])

if st.button("Log Mood"):
    # Save mood when button is clicked
    save_mood_data(today, mood)
    st.success("Mood logged out successfully!")

# Load exixting mood data
data = load_mood_data()
# If there is a data to display
if not data.empty:
    st.subheader("Mood Trend over Time")

    # Convert date string to datetime object
    data["Date"] = pd.to_datetime(data["Date"])
    # Count frequency to each mood
    mood_count = data.groupby("Mood").count()["Date"]
    st.bar_chart(mood_count)
    
    st.write("Build with 💖 by Soniya")



    