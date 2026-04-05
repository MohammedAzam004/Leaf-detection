from collections import defaultdict

import cv2
import numpy as np
import streamlit as st
from PIL import Image

from utils import load_checkpoint, parse_label, predict_bgr_image


THEMES = {
    "Dark mode": {
        "bg": "#0b1120",
        "bg_alt": "#121a2b",
        "sidebar": "#0f1728",
        "card": "rgba(15, 23, 42, 0.82)",
        "card_soft": "rgba(19, 29, 51, 0.72)",
        "text": "#e8eef7",
        "muted": "#98a7bd",
        "accent": "#38bdf8",
        "accent_2": "#34d399",
        "border": "rgba(148, 163, 184, 0.18)",
        "hero_a": "rgba(15, 23, 42, 0.94)",
        "hero_b": "rgba(22, 78, 99, 0.85)",
        "shadow": "rgba(2, 6, 23, 0.34)",
        "upload_bg": "#f8fafc",
        "upload_text": "#102033",
        "upload_muted": "#5b6778",
        "upload_button_bg": "#ffffff",
        "upload_button_border": "rgba(15, 23, 42, 0.14)",
    },
    "Light mode": {
        "bg": "#f1f6fb",
        "bg_alt": "#fbfdff",
        "sidebar": "#f7fafc",
        "card": "rgba(255, 255, 255, 0.94)",
        "card_soft": "rgba(248, 251, 255, 0.98)",
        "text": "#112033",
        "muted": "#5f6e82",
        "accent": "#0f766e",
        "accent_2": "#0369a1",
        "border": "rgba(15, 23, 42, 0.10)",
        "hero_a": "rgba(255, 255, 255, 0.98)",
        "hero_b": "rgba(222, 244, 247, 0.98)",
        "shadow": "rgba(15, 23, 42, 0.10)",
        "upload_bg": "#ffffff",
        "upload_text": "#102033",
        "upload_muted": "#617083",
        "upload_button_bg": "#ffffff",
        "upload_button_border": "rgba(15, 23, 42, 0.12)",
    },
}


st.set_page_config(page_title="AgroVision AI", layout="wide")


@st.cache_resource(show_spinner=False)
def load_model_once():
    return load_checkpoint()


def analyze_image(model, id2label, image: Image.Image):
    rgb_image = image.convert("RGB")
    bgr_image = cv2.cvtColor(np.array(rgb_image), cv2.COLOR_RGB2BGR)
    return predict_bgr_image(model, bgr_image, id2label)


def format_display_text(value):
    formatted = value.title()
    formatted = formatted.replace("(Bell)", "(bell)")
    formatted = formatted.replace("Healthy", "Healthy")
    formatted = formatted.replace("Leaf Mold", "Leaf Mold")
    formatted = formatted.replace("Target Spot", "Target Spot")
    return formatted


def build_supported_class_groups(id2label):
    groups = defaultdict(list)
    for class_id in sorted(id2label):
        raw_label = id2label[class_id]
        crop, disease = parse_label(raw_label)
        groups[format_display_text(crop)].append(
            {
                "disease": format_display_text(disease),
                "raw_label": raw_label,
            }
        )
    return dict(groups)


def inject_theme_css(theme):
    st.markdown(
        f"""
<style>
:root {{
    --bg: {theme["bg"]};
    --bg-alt: {theme["bg_alt"]};
    --sidebar: {theme["sidebar"]};
    --card: {theme["card"]};
    --card-soft: {theme["card_soft"]};
    --text: {theme["text"]};
    --muted: {theme["muted"]};
    --accent: {theme["accent"]};
    --accent-2: {theme["accent_2"]};
    --border: {theme["border"]};
    --hero-a: {theme["hero_a"]};
    --hero-b: {theme["hero_b"]};
    --shadow: {theme["shadow"]};
    --upload-bg: {theme["upload_bg"]};
    --upload-text: {theme["upload_text"]};
    --upload-muted: {theme["upload_muted"]};
    --upload-button-bg: {theme["upload_button_bg"]};
    --upload-button-border: {theme["upload_button_border"]};
}}

.stApp {{
    background:
        radial-gradient(circle at top left, rgba(56, 189, 248, 0.08) 0%, transparent 24%),
        radial-gradient(circle at top right, rgba(52, 211, 153, 0.08) 0%, transparent 22%),
        linear-gradient(180deg, var(--bg) 0%, var(--bg-alt) 100%);
}}

.stApp,
.stApp p,
.stApp li,
.stApp label,
.stApp span,
.stApp div,
.stApp h1,
.stApp h2,
.stApp h3 {{
    color: var(--text);
}}

section[data-testid="stSidebar"] {{
    background: var(--sidebar);
    border-right: 1px solid var(--border);
}}

section[data-testid="stSidebar"] * {{
    color: var(--text) !important;
}}

section[data-testid="stSidebar"] [data-baseweb="radio"] {{
    background: transparent !important;
}}

section[data-testid="stSidebar"] [data-baseweb="radio"] > div {{
    color: var(--text) !important;
}}

section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {{
    color: var(--text) !important;
}}

section[data-testid="stSidebar"] label[data-baseweb="radio"] span {{
    color: var(--text) !important;
}}

div[data-testid="stFileUploaderDropzone"],
div[data-testid="stCameraInput"] {{
    background: var(--card-soft);
    border: 1px dashed var(--border);
    border-radius: 18px;
}}

div[data-testid="stFileUploaderDropzone"] {{
    background: var(--upload-bg) !important;
    border: 1px solid var(--upload-button-border) !important;
    border-radius: 18px !important;
}}

div[data-testid="stFileUploaderDropzone"] > div,
div[data-testid="stFileUploaderDropzone"] > div > div,
div[data-testid="stFileUploaderDropzone"] > div > div > div {{
    background: var(--upload-bg) !important;
}}

div[data-testid="stFileUploaderDropzone"] * {{
    color: var(--upload-text) !important;
    opacity: 1 !important;
}}

div[data-testid="stFileUploaderDropzone"] small,
div[data-testid="stFileUploaderDropzone"] span,
div[data-testid="stFileUploaderDropzone"] p {{
    color: var(--upload-text) !important;
}}

div[data-testid="stFileUploaderDropzone"] small {{
    color: var(--upload-muted) !important;
}}

div[data-testid="stFileUploaderDropzone"] p:first-of-type,
div[data-testid="stFileUploaderDropzone"] span:first-of-type {{
    color: var(--upload-text) !important;
    font-weight: 600 !important;
}}

div[data-testid="stFileUploaderDropzone"] svg {{
    stroke: var(--accent-2) !important;
    fill: transparent !important;
}}

div[data-testid="stFileUploaderDropzone"] button {{
    background: var(--upload-button-bg) !important;
    color: var(--upload-text) !important;
    border: 1px solid var(--upload-button-border) !important;
    box-shadow: none !important;
}}

div[data-testid="stFileUploaderDropzone"] button:hover {{
    border-color: var(--accent-2) !important;
    color: var(--accent-2) !important;
}}

div[data-testid="stMetric"] {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 0.8rem 0.9rem;
    box-shadow: 0 14px 30px var(--shadow);
}}

div[data-testid="stImage"] img {{
    border-radius: 18px;
    border: 1px solid var(--border);
    box-shadow: 0 18px 36px var(--shadow);
}}

button[kind="primary"] {{
    background: linear-gradient(135deg, var(--accent) 0%, var(--accent-2) 100%);
    border: none;
}}

.hero {{
    background: linear-gradient(135deg, var(--hero-a) 0%, var(--hero-b) 100%);
    border: 1px solid var(--border);
    border-radius: 24px;
    padding: 2rem;
    box-shadow: 0 22px 48px var(--shadow);
    margin-bottom: 1rem;
}}

.hero-badge {{
    display: inline-block;
    padding: 0.32rem 0.72rem;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid var(--border);
    margin-right: 0.5rem;
    margin-bottom: 0.5rem;
    font-size: 0.86rem;
}}

.hero-kicker {{
    color: var(--accent);
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    font-size: 0.8rem;
}}

.hero-title {{
    font-size: 2.4rem;
    line-height: 1.05;
    margin: 0.45rem 0 0.7rem;
}}

.hero-copy {{
    max-width: 760px;
    color: var(--muted);
    line-height: 1.65;
    margin-bottom: 1rem;
}}

.surface {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 22px;
    padding: 1.15rem 1.2rem;
    box-shadow: 0 16px 32px var(--shadow);
}}

.surface + .surface {{
    margin-top: 1rem;
}}

.eyebrow {{
    color: var(--accent);
    font-size: 0.8rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
}}

.section-title {{
    margin: 0.25rem 0 0.45rem;
    font-size: 1.28rem;
}}

.muted {{
    color: var(--muted);
    line-height: 1.6;
}}

.scope-box {{
    background: var(--card-soft);
    border: 1px solid var(--border);
    border-left: 4px solid var(--accent);
    border-radius: 18px;
    padding: 1rem 1rem 0.95rem;
}}

.scope-box strong {{
    display: block;
    margin-bottom: 0.35rem;
}}

.result-card {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 22px;
    padding: 1.2rem;
    box-shadow: 0 16px 32px var(--shadow);
}}

.result-title {{
    margin: 0 0 0.9rem;
    font-size: 1.18rem;
}}

.result-block {{
    background: var(--card-soft);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 0.9rem 1rem;
    margin-bottom: 0.75rem;
}}

.result-label {{
    font-size: 0.76rem;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 0.22rem;
}}

.result-value {{
    font-size: 1rem;
    line-height: 1.55;
}}

.dataset-card {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 1rem;
    box-shadow: 0 14px 28px var(--shadow);
    height: 100%;
}}

.dataset-card h3 {{
    margin-top: 0;
    margin-bottom: 0.8rem;
    font-size: 1.08rem;
}}

.dataset-item {{
    padding: 0.7rem 0;
    border-bottom: 1px solid var(--border);
}}

.dataset-item:last-child {{
    border-bottom: none;
    padding-bottom: 0;
}}

.dataset-name {{
    font-weight: 600;
    margin-bottom: 0.28rem;
}}

.dataset-code {{
    font-size: 0.8rem;
    color: var(--accent);
    word-break: break-word;
}}

.guide-list {{
    margin: 0;
    padding-left: 1.2rem;
}}

.guide-list li {{
    margin-bottom: 0.55rem;
    color: var(--muted);
}}
</style>
        """,
        unsafe_allow_html=True,
    )


def render_hero(class_count, theme_name):
    return f"""
<section class="hero">
    <div class="hero-kicker">Plant Disease Screening</div>
    <h1 class="hero-title">AgroVision AI</h1>
    <p class="hero-copy">
        A clean interface for predicting plant disease from supported leaf images.
        This app is trained only on the PlantVillage classes included in this
        project, so users should upload leaves from those classes for reliable results.
    </p>
    <span class="hero-badge">{class_count} trained classes</span>
    <span class="hero-badge">Pepper, Potato, Tomato</span>
    <span class="hero-badge">{theme_name}</span>
</section>
"""


def render_scope_box():
    return """
<section class="scope-box">
    <strong>Important</strong>
    This model only knows the supported dataset classes shown in the app. If a user uploads
    some other crop or disease, the model will still choose the closest known class, which
    can make the result inaccurate.
</section>
"""


def render_result_card(result):
    return f"""
<section class="result-card">
    <h3 class="result-title">Prediction Summary</h3>
    <div class="result-block">
        <div class="result-label">Crop</div>
        <div class="result-value">{result["crop"]}</div>
    </div>
    <div class="result-block">
        <div class="result-label">Disease</div>
        <div class="result-value">{result["disease"]}</div>
    </div>
    <div class="result-block">
        <div class="result-label">Care Advice</div>
        <div class="result-value">{result["advice"]}</div>
    </div>
    <div class="result-block" style="margin-bottom: 0;">
        <div class="result-label">Suggested Treatment</div>
        <div class="result-value">{result["pesticide"]}</div>
    </div>
</section>
"""


def render_dataset_card(crop_name, items):
    parts = [f'<section class="dataset-card"><h3>{crop_name}</h3>']
    for item in items:
        parts.append(
            f"""
<div class="dataset-item">
    <div class="dataset-name">{item["disease"]}</div>
    <div class="dataset-code">{item["raw_label"]}</div>
</div>
            """
        )
    parts.append("</section>")
    return "".join(parts)


st.sidebar.header("Display")
theme_name = st.sidebar.radio("Theme", ("Dark mode", "Light mode"), index=1)
inject_theme_css(THEMES[theme_name])

st.sidebar.header("Input")
input_mode = st.sidebar.radio("Image source", ("Upload image", "Camera"))

try:
    with st.spinner("Loading model..."):
        model, id2label = load_model_once()
except FileNotFoundError as exc:
    st.error(f"Model file not found: {exc}")
    st.stop()
except Exception as exc:
    st.error(f"Unable to load the model: {exc}")
    st.stop()

supported_groups = build_supported_class_groups(id2label)

st.markdown(render_hero(len(id2label), theme_name), unsafe_allow_html=True)

tab_analyze, tab_supported = st.tabs(["Analyze leaf", "Supported dataset"])

with tab_analyze:
    col_left, col_right = st.columns([1.2, 0.8], gap="large")

    with col_left:
        st.markdown(
            """
<section class="surface">
    <div class="eyebrow">Image Analysis</div>
    <h2 class="section-title">Upload a clear leaf image</h2>
    <p class="muted">
        Use a close-up image with good lighting and a visible leaf surface. The
        model performs best when the image belongs to one of the trained classes
        shown in the supported dataset section.
    </p>
</section>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(render_scope_box(), unsafe_allow_html=True)

        selected_image = None
        if input_mode == "Upload image":
            uploaded_file = st.file_uploader(
                "Upload a leaf image",
                type=["jpg", "jpeg", "png"],
            )
            if uploaded_file is not None:
                selected_image = Image.open(uploaded_file)
        else:
            st.markdown(
                """
<section class="surface">
    <div class="eyebrow">Camera Capture</div>
    <h2 class="section-title">Capture a supported leaf</h2>
    <p class="muted">
        Keep the leaf centered, avoid blur, and allow browser camera permission
        before taking the picture.
    </p>
</section>
                """,
                unsafe_allow_html=True,
            )
            captured_file = st.camera_input("Capture a leaf image")
            if captured_file is not None:
                selected_image = Image.open(captured_file)

        if selected_image is not None:
            st.image(selected_image, caption="Selected image", use_container_width=True)

    with col_right:
        st.markdown(
            """
<section class="surface">
    <div class="eyebrow">Quick Guide</div>
    <h2 class="section-title">For better predictions</h2>
    <ul class="guide-list">
        <li>Upload only leaves from the trained Pepper, Potato, or Tomato classes.</li>
        <li>Use a single leaf image instead of a wide farm scene.</li>
        <li>Avoid dark, blurry, or low-resolution images.</li>
        <li>Use the result as screening support, not final diagnosis.</li>
    </ul>
</section>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
<section class="surface">
    <div class="eyebrow">Model Scope</div>
    <h2 class="section-title">Known classes only</h2>
    <p class="muted">
        The classifier was trained on PlantVillage labels only. Unsupported leaves
        may still return a prediction, but that output may not be trustworthy.
    </p>
</section>
            """,
            unsafe_allow_html=True,
        )

    if selected_image is not None:
        try:
            with st.spinner("Analyzing image..."):
                result = analyze_image(model, id2label, selected_image)

            metric_col, result_col = st.columns([0.32, 0.68], gap="large")
            with metric_col:
                st.metric("Confidence", f"{result['confidence'] * 100:.1f}%")
            with result_col:
                st.markdown(render_result_card(result), unsafe_allow_html=True)

            st.caption(
                "Use this result as an initial screening only. Confirm important treatment "
                "decisions with a local agriculture expert."
            )
        except Exception as exc:
            st.error(f"Unable to process the selected image: {exc}")
            st.info("Try another clear leaf image with better lighting and focus.")
    else:
        st.info("Choose an input source and provide a supported leaf image to start analysis.")

with tab_supported:
    st.markdown(
        """
<section class="surface">
    <div class="eyebrow">Supported Dataset</div>
    <h2 class="section-title">Classes used to train this checkpoint</h2>
    <p class="muted">
        These are the exact dataset classes the model understands. If someone opens
        your project, they can check these names first and then upload a matching leaf image.
    </p>
</section>
        """,
        unsafe_allow_html=True,
    )

    crop_names = list(supported_groups.keys())
    dataset_columns = st.columns(len(crop_names), gap="large")
    for column, crop_name in zip(dataset_columns, crop_names):
        with column:
            st.markdown(
                render_dataset_card(crop_name, supported_groups[crop_name]),
                unsafe_allow_html=True,
            )
