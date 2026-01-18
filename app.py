import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Intelligent Video Surveillance & Activity Recognition",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for clearer academic styling
st.markdown("""
<style>
.main-header {
    font-size: 2.6rem;
    font-weight: 700;
    color: #111827;
    margin-bottom: 0.5rem;
}
.sub-header {
    font-size: 1.15rem;
    color: #374151;
    margin-bottom: 2rem;
}
.section-header {
    font-size: 1.6rem;
    font-weight: 700;
    color: #1f2937;
    margin-top: 2.5rem;
    margin-bottom: 1.2rem;
    border-bottom: 3px solid #2563eb;
    padding-bottom: 0.4rem;
}
.info-box {
    background-color: #eef2ff;
    padding: 1.4rem;
    border-radius: 0.5rem;
    border-left: 5px solid #2563eb;
    margin: 1.2rem 0;
    color: #1f2937;
}
.placeholder-box {
    background-color: #fffbeb;
    padding: 1.4rem;
    border-radius: 0.5rem;
    border-left: 5px solid #d97706;
    margin: 1.2rem 0;
    color: #1f2937;
}
.stButton>button {
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## System Configuration")
    st.markdown("---")

    st.slider(
        "Detection Confidence Threshold",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.05
    )

    st.checkbox("Enable Object Tracking", value=True)
    st.checkbox("Enable Activity Recognition", value=True)

    st.markdown("---")
    st.markdown("## About This System")
    st.markdown("""
    This application demonstrates a **classical computer vision–based**
    intelligent surveillance framework.

    **Core Capabilities:**
    - Moving object detection  
    - Multi-object tracking  
    - Activity recognition  
    """)

# Main header
st.markdown(
    '<div class="main-header">Intelligent Video Surveillance & Activity Recognition</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="sub-header">Automated detection, tracking, and activity analysis from surveillance videos</div>',
    unsafe_allow_html=True
)

# Overview
st.markdown('<div class="section-header">System Overview</div>', unsafe_allow_html=True)
st.markdown("""
This project implements a **three-stage classical computer vision pipeline**:

1. **Moving Object Detection** – Identifies foreground objects in surveillance footage  
2. **Object Tracking** – Maintains object identities across frames  
3. **Activity Recognition** – Classifies human motion patterns over time  

The system is designed for **offline CCTV surveillance footage** and is suitable
for security monitoring, behavioral analysis, and academic research.
""")

# Input section
st.markdown('<div class="section-header">Input Data</div>', unsafe_allow_html=True)
tab1, tab2 = st.tabs(["Video Upload", "Image Upload"])

with tab1:
    video_file = st.file_uploader(
        "Upload surveillance video",
        type=["mp4", "avi", "mov"]
    )
    if video_file:
        st.video(video_file)
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("""
        **Video loaded successfully.**

        Planned processing steps:
        - Frame extraction and preprocessing  
        - Foreground motion detection  
        - Object tracking across frames  
        - Activity recognition  
        """)
        st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    image_file = st.file_uploader(
        "Upload image frame",
        type=["jpg", "jpeg", "png"]
    )
    if image_file:
        image = Image.open(image_file)
        st.image(image, use_container_width=True)

# Processing pipeline
st.markdown('<div class="section-header">Processing Pipeline</div>', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("### Moving Object Detection")
    st.markdown('<div class="placeholder-box">', unsafe_allow_html=True)
    st.markdown("""
    **Status:** Awaiting implementation  

    Detects moving objects using foreground segmentation.

    **Planned Methods:**
    - Gaussian Mixture Models (background subtraction)  
    - Frame differencing  
    - Optical flow for motion analysis  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown("### Object Tracking")
    st.markdown('<div class="placeholder-box">', unsafe_allow_html=True)
    st.markdown("""
    **Status:** Awaiting implementation  

    Tracks detected objects across frames with persistent IDs.

    **Planned Methods:**
    - Kalman filtering  
    - Hungarian algorithm (data association)  
    - SORT (Simple Online Realtime Tracking)  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with c3:
    st.markdown("### Activity Recognition")
    st.markdown('<div class="placeholder-box">', unsafe_allow_html=True)
    st.markdown("""
    **Status:** Awaiting implementation  

    Classifies activities using motion and spatio-temporal features.

    **Activity Classes:**
    - Walking  
    - Running  
    - Standing  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:#374151;'>"
    "Intelligent Video Surveillance & Activity Recognition | Academic Project"
    "</div>",
    unsafe_allow_html=True
)
