import streamlit as st    # For creating web interface
import pandas as pd       # For data manipulation
import datetime           # For handling dates
import csv                # For creating and writing CSV file
import os                 # For file operations

# Set up the page configuration
st.set_page_config(page_title="Mood Tracker", page_icon="🎭", layout="centered")

# Gradient background style
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #fbc2eb, #a6c1ee);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Define the file name for storing mood data
MOOD_FILE = "mood_log.csv"

# Function to read mood data from CSV file
def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date", "Mood"])
    try:
        data = pd.read_csv(MOOD_FILE)
        if "Date" not in data.columns or "Mood" not in data.columns:
            return pd.DataFrame(columns=["Date", "Mood"])
        return data
    except Exception:
        return pd.DataFrame(columns=["Date", "Mood"])

# Function to add a new mood entry to the CSV file
def save_mood_data(date, mood):
    file_exists = os.path.exists(MOOD_FILE)
    with open(MOOD_FILE, "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date", "Mood"])  # write headers if file is new
        writer.writerow([date, mood])

# App title
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
    data["Date"] = pd.to_datetime(data["Date"], errors='coerce')
    data = data.dropna(subset=["Date"])

    # Count frequency of each mood
    mood_count = data.groupby("Mood").count()["Date"]
    st.bar_chart(mood_count)

# Footer
st.markdown("---")
st.write("**Made with 💖 by Soniya ✨**")
