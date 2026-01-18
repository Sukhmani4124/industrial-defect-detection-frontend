import streamlit as st
from PIL import Image
import io

# Page configuration
st.set_page_config(
    page_title="Intelligent Video Surveillance & Activity Recognition",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling with improved contrast
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #f8fafc;
        margin-bottom: 0.5rem;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    .sub-header {
        font-size: 1.1rem;
        color: #cbd5e1;
        margin-bottom: 2rem;
        font-weight: 400;
    }
    .section-header {
        font-size: 1.5rem;
        font-weight: 700;
        color: #e2e8f0;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 3px solid #3b82f6;
        padding-bottom: 0.5rem;
    }
    .info-box {
        background-color: #1e3a5f;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #60a5fa;
        margin: 1rem 0;
        color: #e2e8f0;
    }
    .placeholder-box {
        background-color: #3d2e1f;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #fbbf24;
        margin: 1rem 0;
        color: #f3f4f6;
    }
    .stButton>button {
        width: 100%;
    }
    h4 {
        color: #f1f5f9;
        font-weight: 600;
    }
    p {
        color: #cbd5e1;
    }
    .stMarkdown {
        color: #cbd5e1;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### System Configuration")
    st.markdown("---")
    
    detection_threshold = st.slider(
        "Detection Confidence Threshold",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.05,
        help="Minimum confidence score for object detection"
    )
    
    tracking_enabled = st.checkbox(
        "Enable Object Tracking",
        value=True,
        help="Track detected objects across video frames"
    )
    
    activity_recognition = st.checkbox(
        "Enable Activity Recognition",
        value=True,
        help="Recognize activities such as walking, running, standing"
    )
    
    st.markdown("---")
    st.markdown("### About This System")
    st.markdown("""
    This system demonstrates an intelligent video surveillance framework 
    capable of detecting moving objects, tracking their trajectories, 
    and recognizing human activities in real-time.
    
    **Key Features:**
    - Moving object detection
    - Multi-object tracking
    - Activity classification
    - Real-time processing capability
    """)

# Main content
st.markdown('<div class="main-header">Intelligent Video Surveillance & Activity Recognition</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">An automated system for detecting, tracking, and recognizing activities in surveillance videos</div>', unsafe_allow_html=True)

# System overview
st.markdown('<div class="section-header">System Overview</div>', unsafe_allow_html=True)
st.markdown("""
This project implements a comprehensive video surveillance system that performs three primary tasks:

1. **Moving Object Detection**: Identifies and localizes moving objects within the surveillance footage
2. **Object Tracking**: Maintains temporal consistency by tracking detected objects across video frames
3. **Activity Recognition**: Classifies human activities into categories such as Walking, Running, and Standing

The system is designed for real-time processing of surveillance camera feeds and can be deployed 
in various scenarios including security monitoring, traffic management, and behavioral analysis.
""")

# File upload section
st.markdown('<div class="section-header">Input Data</div>', unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Video Upload", "Image Upload"])

with tab1:
    st.markdown("Upload surveillance video footage for processing.")
    
    video_file = st.file_uploader(
        "Select a video file",
        type=["mp4", "avi", "mov"],
        help="Supported formats: MP4, AVI, MOV"
    )
    
    if video_file is not None:
        st.markdown("**Preview:**")
        st.video(video_file)
        
        file_details = {
            "Filename": video_file.name,
            "File size": f"{video_file.size / (1024 * 1024):.2f} MB",
            "File type": video_file.type
        }
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Filename", file_details["Filename"])
        with col2:
            st.metric("Size", file_details["File size"])
        with col3:
            st.metric("Type", file_details["File type"])
        
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("""
        **Video loaded successfully.** The system will process this video through the following pipeline:
        - Frame extraction and preprocessing
        - Moving object detection in each frame
        - Trajectory tracking across frames
        - Activity classification based on motion patterns
        """)
        st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown("Upload a single frame or image for static analysis.")
    
    image_file = st.file_uploader(
        "Select an image file",
        type=["jpg", "jpeg", "png"],
        help="Supported formats: JPG, JPEG, PNG"
    )
    
    if image_file is not None:
        image = Image.open(image_file)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.image(image, caption="Uploaded Image", use_container_width=True)
        
        with col2:
            st.markdown("**Image Properties:**")
            st.write(f"Dimensions: {image.size[0]} x {image.size[1]} px")
            st.write(f"Format: {image.format}")
            st.write(f"Mode: {image.mode}")
        
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("""
        **Image loaded successfully.** Static object detection will be performed on this frame.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

# Processing pipeline section
st.markdown('<div class="section-header">Processing Pipeline</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### Moving Object Detection")
    st.markdown('<div class="placeholder-box">', unsafe_allow_html=True)
    st.markdown("""
    **Status:** Awaiting implementation
    
    This module identifies and localizes objects that are in motion within the video frames. 
    It separates moving foreground objects from the static background, enabling the system 
    to focus computational resources on areas of interest. Detected objects are highlighted 
    with bounding boxes for visualization.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown("#### Object Tracking")
    st.markdown('<div class="placeholder-box">', unsafe_allow_html=True)
    st.markdown("""
    **Status:** Awaiting implementation
    
    This module maintains the identity of detected objects across consecutive video frames. 
    It assigns unique identifiers to each object and follows their movement throughout the 
    video sequence, creating trajectory paths that show where objects have moved over time.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown("#### Activity Recognition")
    st.markdown('<div class="placeholder-box">', unsafe_allow_html=True)
    st.markdown("""
    **Status:** Awaiting implementation
    
    This module analyzes the motion patterns and behaviors of tracked objects to classify 
    their activities. The system recognizes different types of human activities such as 
    walking, running, and standing based on movement characteristics and temporal features.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Results section
st.markdown('<div class="section-header">Analysis Results</div>', unsafe_allow_html=True)

if video_file is not None or image_file is not None:
    results_tab1, results_tab2, results_tab3 = st.tabs([
        "Detection Results",
        "Tracking Results",
        "Activity Classification"
    ])
    
    with results_tab1:
        st.markdown('<div class="placeholder-box">', unsafe_allow_html=True)
        st.markdown("""
        **Detection results will be displayed here.**
        
        Expected output:
        - Annotated frames with bounding boxes
        - Detection confidence scores
        - Object count per frame
        - Detection statistics
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with results_tab2:
        st.markdown('<div class="placeholder-box">', unsafe_allow_html=True)
        st.markdown("""
        **Tracking results will be displayed here.**
        
        Expected output:
        - Object trajectories overlaid on video
        - Tracking IDs and paths
        - Velocity and direction vectors
        - Tracking performance metrics
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with results_tab3:
        st.markdown('<div class="placeholder-box">', unsafe_allow_html=True)
        st.markdown("""
        **Activity recognition results will be displayed here.**
        
        Expected output:
        - Activity labels per tracked object
        - Confidence scores for each activity
        - Temporal activity timeline
        - Activity distribution statistics
        """)
        st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("Upload a video or image file to see analysis results.")

# Performance metrics section
st.markdown('<div class="section-header">System Performance</div>', unsafe_allow_html=True)

metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:
    st.metric(
        label="Processing Speed",
        value="Pending",
        help="Frames processed per second"
    )

with metric_col2:
    st.metric(
        label="Detection Accuracy",
        value="Pending",
        help="Percentage of correctly detected objects"
    )

with metric_col3:
    st.metric(
        label="Tracking Stability",
        value="Pending",
        help="Average tracking duration per object"
    )

with metric_col4:
    st.metric(
        label="Classification Accuracy",
        value="Pending",
        help="Activity recognition accuracy"
    )

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #94a3b8; font-size: 0.9rem;'>
    Intelligent Video Surveillance & Activity Recognition System | Academic Research Project
</div>
""", unsafe_allow_html=True)
