# AgroVision AI

AgroVision AI is a Streamlit-based plant disease detection project for leaf image screening. The app loads a trained EfficientNetV2-S checkpoint, accepts a leaf image from file upload or camera capture, and returns the predicted crop, disease, confidence score, care advice, and suggested treatment.

This repository is focused on inference and deployment. It includes the production Streamlit app, the trained model checkpoint, and the helper utilities needed to preprocess images and run predictions.

## What The App Does

- predicts supported plant disease classes from a leaf image
- shows crop name and disease name in a cleaner readable format
- displays model confidence for the current prediction
- provides short care guidance and treatment suggestions
- supports both upload and camera input
- lists the supported dataset classes so users know the model scope
- includes light mode and dark mode in the UI

## Supported Dataset Scope

This model is trained only on the PlantVillage-style classes stored in the checkpoint. The app is designed for the following crop groups:

- Pepper (bell)
- Potato
- Tomato

If a user uploads a leaf outside the supported training classes, the model will still return the closest known class, but that result may not be reliable.

## Prediction Pipeline

The inference flow is:

1. The user uploads a leaf image or captures one from the browser camera.
2. The image is converted to RGB and then prepared for OpenCV and PyTorch processing.
3. Albumentations resizes the image to `192 x 192`, normalizes it, and converts it to a tensor.
4. The EfficientNetV2-S classifier runs inference on the processed tensor.
5. The top predicted label is mapped to:
   - crop
   - disease
   - confidence
   - care advice
   - suggested treatment
6. The result is displayed in the Streamlit app.

## Tech Stack

- Streamlit
- PyTorch
- timm
- Albumentations
- OpenCV
- NumPy
- Pillow

## Project Structure

```text
Agrovision-ai/
|-- .streamlit/
|   `-- config.toml
|-- assets/
|-- best_fast_model.pth
|-- DEPLOYMENT.md
|-- LICENSE
|-- packages.txt
|-- README.md
|-- requirements.txt
|-- streamlit_app.py
`-- utils.py
```

## Main Files

- `streamlit_app.py`
  Main Streamlit interface, theme handling, upload and camera flow, and prediction display.

- `utils.py`
  Model loading, image preprocessing, class parsing, and inference helpers.

- `best_fast_model.pth`
  Trained checkpoint used by the app for prediction.

- `requirements.txt`
  Python dependencies for local use and Streamlit Community Cloud deployment.

- `packages.txt`
  Linux system packages needed during deployment. Currently includes `libgl1`.

## Local Setup

### Requirements

- Python 3.12 or 3.13 recommended
- Git
- Git LFS

### Clone And Install

```bash
git clone https://github.com/MohammedAzam004/Leaf-detection.git
cd Leaf-detection
git lfs install
git lfs pull
python -m venv .venv
```

### Activate The Environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run The App

```bash
streamlit run streamlit_app.py
```

## Deployment

This project is prepared for Streamlit Community Cloud deployment.

Basic deployment flow:

1. Push the repository to GitHub.
2. Open Streamlit Community Cloud.
3. Create a new app from this repository.
4. Set the entrypoint file to `streamlit_app.py`.
5. If needed, choose the Python version in Advanced settings.
6. Deploy the app.

For a more focused deployment guide, see [DEPLOYMENT.md](DEPLOYMENT.md).

## Security And Secrets

This project does not require any API keys for its current prediction flow.

Before pushing:

- keep `.env` files out of version control
- keep `.streamlit/secrets.toml` out of version control
- do not commit service-account files, private keys, or credential exports
- use Streamlit Community Cloud secrets only through the app settings when needed

The repository is configured so common environment and secret files are ignored by Git.

## Troubleshooting

Common issues:

- `Checkpoint not found`
  Make sure `best_fast_model.pth` exists in the repository root and Git LFS pulled it correctly.

- `ModuleNotFoundError`
  Reinstall dependencies with `pip install -r requirements.txt`.

- poor predictions
  Use a clear, close-up leaf image with good lighting and keep to supported crop classes.

- deployment dependency issues
  Confirm `requirements.txt` and `packages.txt` are in the repository root.

## Notes

- The model file is tracked with Git LFS.
- The app is intended for screening support, not final agricultural diagnosis.
- Treatment suggestions should be verified with local agriculture guidance before use.

## License

This project is distributed under the MIT License. See [LICENSE](LICENSE).
