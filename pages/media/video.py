import streamlit as st

# Title of the page
st.title("🎬 My Cinematic Gallery")
st.write("Welcome to my gallery. Check out my best cinematic work below.")


# Title of the page
st.title("🎬 My Cinematic Gallery")
st.write("Welcome to my gallery. Check out my best cinematic work below.")

# Replace with your actual video filename and extension (e.g., .mp4, .mov)
video_file_path = "0215.mp4"

# Open the video file in binary mode and display it
with open(video_file_path, "rb") as video_file:
    video_bytes = video_file.read()
    st.video(video_bytes)
