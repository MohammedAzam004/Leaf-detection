# AgroVision AI

AgroVision AI is a Streamlit app that predicts plant diseases from leaf images and shows basic care guidance for the detected class.

## Project files

- `streamlit_app.py` - Streamlit entrypoint
- `utils.py` - model loading, preprocessing, and prediction helpers
- `best_fast_model.pth` - trained checkpoint
- `requirements.txt` - Python dependencies for local run and Streamlit Cloud
- `packages.txt` - Linux package needed by OpenCV on Streamlit Cloud

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deploy on Streamlit Community Cloud

1. Push this repository to GitHub.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/).
3. Create a new app from your GitHub repository.
4. Set the main file path to `streamlit_app.py`.
5. In Advanced settings, choose the Python version only if you want to override the default. Streamlit Community Cloud currently defaults to Python 3.12.
6. Deploy the app.

## Notes

- Community Cloud uses the app settings screen for Python selection. `runtime.txt` is not needed here.
- The model file is already tracked with Git LFS. If deployment fails while loading the model, first confirm GitHub contains the real `.pth` file and not a broken LFS pointer.
- Camera mode depends on browser camera permission.
