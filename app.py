import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Intelligent Video Surveillance",
    layout="centered"
)

st.title("Intelligent Video Surveillance & Activity Recognition")
st.write(
    "Frontend Interface for Surveillance Video Analysis using "
    "Classical Computer Vision Techniques"
)

uploaded_file = st.file_uploader(
    "Upload a surveillance video or image",
    type=["mp4", "mov", "avi", "jpg", "png", "jpeg"]
)

if uploaded_file is not None:
    file_type = uploaded_file.type

    if "video" in file_type:
        st.subheader("Uploaded Surveillance Video")
        st.video(uploaded_file)

        st.subheader("Analysis Output (Placeholder)")
        st.info(
            "Moving object detection, tracking, and activity "
            "recognition results will be displayed here."
        )

        st.markdown("""
        **Planned Outputs:**
        - Bounding boxes around moving objects  
        - Object tracking paths across frames  
        - Activity labels (Walking, Running, Standing)
        """)

    elif "image" in file_type:
        image = Image.open(uploaded_file)
        st.subheader("Uploaded Frame/Image")
        st.image(image, use_column_width=True)

        st.subheader("Analysis Output (Placeholder)")
        st.info(
            "Object detection and activity inference "
            "results will be displayed here."
        )
