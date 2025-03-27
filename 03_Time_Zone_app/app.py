import streamlit as st
from datetime import datetime, date
from zoneinfo import ZoneInfo
import base64

time_zone = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

st.set_page_config(page_title="Time-zone-app", page_icon="🕰", layout="centered")
st.title("Time Zone App")

def get_base64_of_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()
# Add background image using st.image and CSS
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/png;base64,{get_base64_of_image("clock.png")});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

selected_timezone = st.multiselect("Select Time Zones", time_zone, default=("UTC", "Asia/Karachi"))

st.subheader("Selected Timezone")
for tz in selected_timezone:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%m-%d-%Y, %I:%M:%S %p")
    st.write(f"**{tz}** : {current_time}")

st.subheader("Convert Time Into Another Timezone")

# User selects time
current_time = st.time_input("Select Current Time", value=datetime.now().time())

# User selects from and to timezones
from_tz = st.selectbox("From Timezone", time_zone, index=0)
to_tz = st.selectbox("To Timezone", time_zone, index=1)

if st.button("Convert Time"):
    # Convert user input time to a full datetime object with today's date
    dt = datetime.combine(date.today(), current_time)
    
    # Assign source timezone
    dt = dt.replace(tzinfo=ZoneInfo(from_tz))
    
    # Convert to target timezone
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%m-%d-%Y, %I:%M:%S %p")

    st.success(f"Converted Time: {to_tz} → {converted_time}")
