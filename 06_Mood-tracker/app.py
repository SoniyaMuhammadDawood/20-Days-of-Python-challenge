import streamlit as st    # For creating web interface
import pandas as pd       # For data manipulating
import datetime           # For handling dates
import csv                # For creating and writing csv file
import os                 # For file operation


st.set_page_config(page_title="Mood Tracker", page_icon="🎭", layout="centered")

# Gradient background
st.markdown(
    f"""
    <style>
    .stApp {{
        background: linear-gradient(to right, #fbc2eb, #a6c1ee);
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Define the file name & storing the mood data
MOOD_FILE = "mood_log.csv"

# Function to read mood data from csv file
def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date", "Mood"])
    return pd.read_csv(MOOD_FILE)

# Function to add new mood entry to the csv file
def save_mood_data(date, mood):
    with open(MOOD_FILE, "a", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date, mood])


st.title("*📝 Mood Tracker 🌈*")

# Get today’s date
today = datetime.date.today()

# Mood selection
st.subheader("🌤️ **How are you feeling today?**")
mood = st.selectbox("**Select your mood**", ["😀 Happy", "😔 Sad", "😡 Angry", "😐 Neutral"])

# Button to save mood
if st.button(" **Log Mood**"):
    save_mood_data(today, mood)
    st.success("**✅ Mood logged successfully!**")

# Load existing mood data
data = load_mood_data()
if not data.empty:
    st.subheader("📊 Mood Trend Over Time")

    # Convert date string to datetime object
    data["Date"] = pd.to_datetime(data["Date"])
    # Count frequency of each mood
    mood_count = data.groupby("Mood").count()["Date"]
    st.bar_chart(mood_count)

# Footer
st.markdown("---")
st.write("**Made with 💖 by **Soniya** ..✨**")

