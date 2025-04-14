import streamlit as st
from datetime import datetime, date
from zoneinfo import ZoneInfo

# Expanded Time Zone List
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
    "Africa/Johannesburg",
    "America/Toronto",
    "America/Sao_Paulo",
    "Europe/Paris",
    "Asia/Singapore",
    "Pacific/Auckland",
    "Asia/Hong_Kong",
    "Europe/Moscow",
    "Asia/Seoul",
]

# Streamlit Page Config
st.set_page_config(page_title=" Time Zone App", page_icon="⏳", layout="centered")

# Styled Title with Emojis
st.markdown(
    "<h1 style='text-align: center;'>🕒🌎 Welcome to the Time Zone Converter App 🌍🕓</h1>",
    unsafe_allow_html=True
)

# Gradient Background Style
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #a8d89b, #dff6d7, #bfeeae);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Multiselect Dropdown for Current Time in Multiple Timezones
selected_timezone = st.multiselect("**🌐 Select Time Zones to View Current Time**", time_zone, default=("UTC", "Asia/Karachi"))

st.subheader("**🕒 Current Time in Selected Timezones**")
for tz in selected_timezone:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%m-%d-%Y, %I:%M:%S %p")
    st.write(f"**{tz}** : {current_time}")

# Time Converter Section
st.subheader("**🧭 Convert Time Into Another Timezone**")

# Time Input
current_time = st.time_input("**🕰 Select Current Time**", value=datetime.now().time())

# From and To Timezones
from_tz = st.selectbox("**🌍 From Timezone**", time_zone, index=0)
to_tz = st.selectbox("**🌏 To Timezone**", time_zone, index=1)

# Button to Convert
if st.button("**🔁 Convert Time**"):
    dt = datetime.combine(date.today(), current_time)
    dt = dt.replace(tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%m-%d-%Y, %I:%M:%S %p")
    st.success(f"✅ **Converted Time** ({from_tz} ➡ {to_tz}): {converted_time}")
