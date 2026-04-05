import cv2
import numpy as np
import streamlit as st
from PIL import Image

from utils import load_checkpoint, predict_bgr_image


st.set_page_config(page_title="AgroVision AI", layout="centered")
st.title("AgroVision AI")
st.caption(
    "Upload a leaf image or use your camera to detect common plant diseases "
    "and review basic care guidance."
)


@st.cache_resource(show_spinner=False)
def load_model_once():
    return load_checkpoint()


def analyze_image(model, id2label, image: Image.Image):
    rgb_image = image.convert("RGB")
    bgr_image = cv2.cvtColor(np.array(rgb_image), cv2.COLOR_RGB2BGR)
    return predict_bgr_image(model, bgr_image, id2label)


try:
    with st.spinner("Loading model..."):
        MODEL, ID2LABEL = load_model_once()
except FileNotFoundError as exc:
    st.error(f"Model file not found: {exc}")
    st.stop()
except Exception as exc:
    st.error(f"Unable to load the model: {exc}")
    st.stop()


st.sidebar.header("Input")
input_mode = st.sidebar.radio("Choose image source", ("Upload image", "Camera"))

selected_image = None
if input_mode == "Upload image":
    uploaded_file = st.file_uploader(
        "Upload a leaf image",
        type=["jpg", "jpeg", "png"],
    )
    if uploaded_file is not None:
        selected_image = Image.open(uploaded_file)
else:
    st.info("Allow camera access in your browser before capturing an image.")
    captured_file = st.camera_input("Capture a leaf image")
    if captured_file is not None:
        selected_image = Image.open(captured_file)


if selected_image is not None:
    st.image(selected_image, caption="Selected image", use_container_width=True)

    try:
        with st.spinner("Analyzing image..."):
            result = analyze_image(MODEL, ID2LABEL, selected_image)

        st.subheader("Prediction")
        st.metric("Confidence", f"{result['confidence'] * 100:.1f}%")
        st.write(f"**Crop:** {result['crop']}")
        st.write(f"**Disease:** {result['disease']}")
        st.write(f"**Care advice:** {result['advice']}")
        st.write(f"**Suggested treatment:** {result['pesticide']}")
        st.caption(
            "Use this result as an initial screening only. Confirm treatment "
            "choices with a local agriculture expert before applying them."
        )
    except Exception as exc:
        st.error(f"Unable to process the selected image: {exc}")
        st.info("Try another clear leaf image with good lighting.")
else:
    st.info("Upload a leaf image or use the camera to start a prediction.")
