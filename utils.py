from pathlib import Path
import re

import albumentations as A
import cv2
import numpy as np
import timm
import torch
import torch.nn.functional as F
from albumentations.pytorch import ToTensorV2


BASE_DIR = Path(__file__).resolve().parent
MODEL_CANDIDATES = (
    BASE_DIR / "best_fast_model.pth",
    BASE_DIR / "best_fast_model (1).pth",
)
MODEL_NAME = "tf_efficientnetv2_s.in21k"
IMG_SIZE = 192
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

CARE_GUIDANCE = {
    "Pepper__bell___Bacterial_spot": {
        "advice": "Remove badly infected leaves, avoid overhead watering, and sanitize tools.",
        "pesticide": "Copper-based bactericide if needed and locally approved.",
    },
    "Pepper__bell___healthy": {
        "advice": "No disease detected. Continue normal irrigation and monitoring.",
        "pesticide": "None",
    },
    "Potato___Early_blight": {
        "advice": "Remove infected leaves, improve airflow, and avoid keeping foliage wet.",
        "pesticide": "Mancozeb or chlorothalonil if locally approved.",
    },
    "Potato___Late_blight": {
        "advice": "Isolate infected plants quickly and reduce leaf wetness.",
        "pesticide": "Copper fungicide or metalaxyl mixture if locally approved.",
    },
    "Potato___healthy": {
        "advice": "No disease detected. Keep monitoring plants regularly.",
        "pesticide": "None",
    },
    "Tomato_Bacterial_spot": {
        "advice": "Remove infected leaves, avoid splashing water, and disinfect tools.",
        "pesticide": "Copper-based bactericide if needed and locally approved.",
    },
    "Tomato_Early_blight": {
        "advice": "Prune affected leaves and improve airflow around the plant.",
        "pesticide": "Mancozeb or chlorothalonil if locally approved.",
    },
    "Tomato_Late_blight": {
        "advice": "Separate infected plants and avoid wet foliage conditions.",
        "pesticide": "Copper fungicide or metalaxyl mixture if locally approved.",
    },
    "Tomato_Leaf_Mold": {
        "advice": "Lower humidity, improve ventilation, and remove infected leaves.",
        "pesticide": "Chlorothalonil if locally approved.",
    },
    "Tomato_Septoria_leaf_spot": {
        "advice": "Remove spotted leaves and mulch to reduce soil splash onto plants.",
        "pesticide": "Mancozeb or chlorothalonil if locally approved.",
    },
    "Tomato_Spider_mites_Two_spotted_spider_mite": {
        "advice": "Wash the undersides of leaves and monitor nearby plants closely.",
        "pesticide": "Insecticidal soap or miticide if locally approved.",
    },
    "Tomato__Target_Spot": {
        "advice": "Remove affected leaves and improve spacing and airflow.",
        "pesticide": "Azoxystrobin or chlorothalonil if locally approved.",
    },
    "Tomato__Tomato_YellowLeaf__Curl_Virus": {
        "advice": "Remove severely affected plants and control whiteflies to limit spread.",
        "pesticide": "No direct cure. Focus on whitefly control and sanitation.",
    },
    "Tomato__Tomato_mosaic_virus": {
        "advice": "Remove infected plants and disinfect hands and tools after handling.",
        "pesticide": "No direct cure. Focus on sanitation and resistant seedlings.",
    },
    "Tomato_healthy": {
        "advice": "No disease detected. Continue normal crop care and monitoring.",
        "pesticide": "None",
    },
}

GUIDANCE_ALIASES = {
    "Pepper,_bell___Bacterial_spot": "Pepper__bell___Bacterial_spot",
    "Pepper,_bell___healthy": "Pepper__bell___healthy",
    "Tomato___Early_blight": "Tomato_Early_blight",
    "Tomato___Late_blight": "Tomato_Late_blight",
    "Tomato___healthy": "Tomato_healthy",
}

VAL_TFMS = A.Compose(
    [
        A.Resize(IMG_SIZE, IMG_SIZE),
        A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
        ToTensorV2(),
    ]
)


def get_model_path():
    for candidate in MODEL_CANDIDATES:
        if candidate.exists():
            return candidate
    return MODEL_CANDIDATES[0]


def normalize_id2label(raw_id2label):
    if raw_id2label is None:
        raise ValueError("Checkpoint is missing 'id2label'.")

    if isinstance(raw_id2label, dict):
        return {int(idx): str(label) for idx, label in raw_id2label.items()}

    if isinstance(raw_id2label, (list, tuple)):
        return {idx: str(label) for idx, label in enumerate(raw_id2label)}

    raise TypeError("Checkpoint 'id2label' must be a dict, list, or tuple.")


def load_checkpoint(path=None, device=DEVICE, model_name=MODEL_NAME):
    model_path = Path(path) if path is not None else get_model_path()
    if not model_path.exists():
        raise FileNotFoundError(
            f"Checkpoint not found at {model_path}. Keep best_fast_model.pth in the project root."
        )

    checkpoint = torch.load(model_path, map_location=device)
    id2label = normalize_id2label(checkpoint.get("id2label"))
    state_dict = checkpoint["model"] if "model" in checkpoint else checkpoint

    model = timm.create_model(
        model_name,
        pretrained=False,
        num_classes=len(id2label),
    ).to(device)
    model.load_state_dict(state_dict)
    model.eval()
    return model, id2label


def prettify_text(value):
    cleaned = value.replace("__", " ").replace("_", " ")
    cleaned = cleaned.replace("YellowLeaf", "Yellow Leaf")
    cleaned = cleaned.replace("Pepper bell", "Pepper (bell)")
    cleaned = cleaned.replace("Two spotted", "Two-spotted")
    return re.sub(r"\s+", " ", cleaned).strip()


def parse_label(label):
    if "___" in label:
        crop, disease = label.split("___", 1)
    elif "_" in label:
        crop, disease = label.split("_", 1)
    else:
        crop, disease = label, "healthy"

    return prettify_text(crop), prettify_text(disease)


def preprocess_image_bgr(bgr_img):
    image_rgb = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)
    transformed = VAL_TFMS(image=image_rgb)["image"].unsqueeze(0)
    return transformed


def get_care_guidance(label):
    canonical_label = GUIDANCE_ALIASES.get(label, label)
    return CARE_GUIDANCE.get(
        canonical_label,
        {
            "advice": (
                "Review this result with a local agriculture expert before treatment."
            ),
            "pesticide": "Use only locally approved products if treatment is needed.",
        },
    )


def predict_tensor(model, tensor, id2label, device=DEVICE):
    tensor = tensor.to(device)
    with torch.no_grad():
        output = model(tensor)
        probabilities = F.softmax(output, dim=1).cpu().numpy()[0]

    predicted_id = int(np.argmax(probabilities))
    confidence = float(probabilities[predicted_id])
    label = id2label[predicted_id]
    crop, disease = parse_label(label)
    guidance = get_care_guidance(label)

    return {
        "label": label,
        "crop": crop,
        "disease": disease,
        "confidence": confidence,
        "advice": guidance["advice"],
        "pesticide": guidance["pesticide"],
    }


def predict_bgr_image(model, bgr_img, id2label, device=DEVICE):
    tensor = preprocess_image_bgr(bgr_img)
    return predict_tensor(model, tensor, id2label, device=device)
