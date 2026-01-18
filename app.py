import streamlit as st
from PIL import Image

st.set_page_config(page_title="Industrial Defect Detection", layout="centered")

st.title("Industrial Defect Detection")
st.write("Frontend Interface for Surface Inspection System")

uploaded_file = st.file_uploader(
    "Upload an industrial surface image or video",
    type=["jpg", "png", "jpeg", "mp4", "mov", "avi"]
)

if uploaded_file is not None:
    file_type = uploaded_file.type

    if "image" in file_type:
        image = Image.open(uploaded_file)
        st.subheader("Uploaded Image")
        st.image(image, use_column_width=True)

        st.subheader("Processed Output (Placeholder)")
        st.info("Backend image processing will be integrated here.")
        st.image(image, use_column_width=True)

    elif "video" in file_type:
        st.subheader("Uploaded Video")
        st.video(uploaded_file)

        st.subheader("Processed Output (Placeholder)")
        st.info("Video processing pipeline will be integrated here.")
