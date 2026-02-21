import streamlit as st
from PIL import Image
import numpy as np
import cv2
from utils import load_checkpoint, preprocess_image_bgr, predict_bgr_image

st.set_page_config(page_title="AgroVision AI", layout="centered")
st.title("🌿 AgroVision AI — Plant Health Detector")
st.markdown("Upload a leaf image or use the camera to detect disease and see cure suggestions.")

@st.cache_resource(show_spinner=False)
def load_model_once():
    try:
        model, id2label = load_checkpoint()
        return model, id2label
    except FileNotFoundError as e:
        st.error(f"❌ Model file not found: {e}")
        st.stop()
    except Exception as e:
        st.error(f"❌ Error loading model: {e}")
        st.stop()

with st.spinner("Loading AI model..."):
    model, id2label = load_model_once()

mode = st.sidebar.radio("Mode", ["Upload Image", "Use Camera (experimental)"])
if mode == "Upload Image":
    uploaded = st.file_uploader("Upload a leaf image", type=["jpg","jpeg","png"])
    if uploaded:
        image = Image.open(uploaded).convert("RGB")
        st.image(image, caption="Input Image", use_column_width=True)
        
        try:
            bgr = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            res = predict_bgr_image(model, bgr, id2label)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Accuracy Rate", f"{res['confidence']*100:.1f}%")
            
            st.divider()
            st.markdown(f"**Crop:** {res['crop']}")
            st.markdown(f"**Disease:** {res['disease']}")
            st.markdown(f"**Cure / Advice:** {res['advice']}")
            st.markdown(f"**Recommended pesticide:** {res['pesticide']}")
        except Exception as e:
            st.error(f"❌ Error processing image: {e}")
            st.info("Please try with a different image.")

else:
    st.info("Camera mode uses browser camera. Works best in Streamlit sharing or local run with camera permission.")
    img_file_buffer = st.camera_input("Use camera to capture a leaf")
    if img_file_buffer:
        image = Image.open(img_file_buffer).convert("RGB")
        st.image(image, caption="Captured Image", use_column_width=True)
        
        try:
            bgr = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            res = predict_bgr_image(model, bgr, id2label)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Accuracy Rate", f"{res['confidence']*100:.1f}%")
            
            st.divider()
            st.markdown(f"**Crop:** {res['crop']}")
            st.markdown(f"**Disease:** {res['disease']}")
            st.markdown(f"**Cure / Advice:** {res['advice']}")
            st.markdown(f"**Recommended pesticide:** {res['pesticide']}")
        except Exception as e:
            st.error(f"❌ Error processing image: {e}")
            st.info("Please try capturing a different image.")
