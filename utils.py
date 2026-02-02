# utils.py
import os
import cv2
import torch
import timm
import numpy as np
import torch.nn.functional as F
import albumentations as A
from albumentations.pytorch import ToTensorV2


MODEL_PATH = os.path.join(os.path.dirname(__file__), "best_fast_model (1).pth")
MODEL_NAME = "tf_efficientnetv2_s_in21k"
IMG_SIZE = 192
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


CURES = {
 "Tomato___Early_blight":{"advice":"Remove infected leaves; rotate crops.","pesticide":"Mancozeb 75 WP"},
 "Tomato___Late_blight":{"advice":"Destroy infected plants; avoid wetness.","pesticide":"Copper oxychloride"},
 "Tomato___healthy":{"advice":"No action needed.","pesticide":"None"},
 "Apple___Black_rot":{"advice":"Prune cankers; remove mummified fruit.","pesticide":"Captan 50 WP"},
 "Potato___Late_blight":{"advice":"Destroy haulms; ensure drainage.","pesticide":"Metalaxyl + Mancozeb"},
 "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot":{"advice":"Rotate crops; use tolerant hybrids.","pesticide":"Azoxystrobin"},
 "Grape___Black_rot":{"advice":"Prune infected shoots; remove mummified berries.","pesticide":"Mancozeb"},
 "Pepper,_bell___Bacterial_spot":{"advice":"Avoid overhead irrigation; rotate crops.","pesticide":"Copper oxychloride"}
}


VAL_TFMS = A.Compose([
    A.Resize(IMG_SIZE, IMG_SIZE),
    A.Normalize(mean=(0.485,0.456,0.406), std=(0.229,0.224,0.225)),
    ToTensorV2()
])


def load_checkpoint(path=MODEL_PATH, device=DEVICE, model_name=MODEL_NAME):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Checkpoint not found at {path}. Place best_fast_model.pth in project root.")
    ckpt = torch.load(path, map_location=device)
    id2label = ckpt.get("id2label", None)
    if id2label is None:
       
        id2label = ckpt.get("id2label", None)
    num_classes = len(id2label) if id2label else ckpt.get("num_classes", None)
  
    model = timm.create_model(model_name, pretrained=False, num_classes=len(id2label)).to(device)
    model.load_state_dict(ckpt["model"])
    model.eval()
    return model, id2label

def parse_label(label):
    if "___" in label:
        crop, disease = label.split("___", 1)
    elif "__" in label:
        crop, disease = label.split("__", 1)
    elif "_" in label:
        parts = label.split("_", 1)
        crop = parts[0]
        disease = parts[1] if len(parts) > 1 else "healthy"
    else:
        crop, disease = label, "healthy"
    return crop, disease

def preprocess_image_bgr(bgr_img):

    img_rgb = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)
    transformed = VAL_TFMS(image=img_rgb)["image"].unsqueeze(0)
    return transformed

def predict_tensor(model, tensor, id2label, device=DEVICE):
    tensor = tensor.to(device)
    with torch.no_grad():
        out = model(tensor)
        probs = F.softmax(out, dim=1).cpu().numpy()[0]
    pid = int(np.argmax(probs))
    conf = float(probs[pid])
    label = id2label[pid]
    crop, disease = parse_label(label)
    rec = CURES.get(label, {"advice":"Consult agronomist.","pesticide":"Refer to local guide."})
    return {
        "label": label,
        "crop": crop,
        "disease": disease,
        "confidence": conf,
        "advice": rec["advice"],
        "pesticide": rec["pesticide"]
    }


def predict_bgr_image(model, bgr_img, id2label, device=DEVICE):
    t = preprocess_image_bgr(bgr_img)
    return predict_tensor(model, t, id2label, device=device)
