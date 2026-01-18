import streamlit as st
import cv2
import numpy as np

st.set_page_config(page_title="Industrial Defect Detection", layout="centered")

st.title("Industrial Defect Detection")
st.write("Frontend Interface for Surface Inspection System")

uploaded_file = st.file_uploader(
    "Upload an industrial surface image",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    st.subheader("Uploaded Image")
    st.image(image, channels="BGR")

    st.subheader("Processed Output (Placeholder)")
    st.info("Backend image processing will be integrated here.")
    st.image(image, channels="BGR")
