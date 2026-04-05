# Streamlit Deployment

## Recommended setup

- Repository root contains `streamlit_app.py`, `requirements.txt`, `packages.txt`, and `best_fast_model.pth`.
- Deploy from GitHub to Streamlit Community Cloud.
- Use the Advanced settings dialog in Streamlit Community Cloud if you want to change the Python version from the default.

## Deployment steps

1. Commit and push the latest code to GitHub.
2. Open [https://share.streamlit.io/](https://share.streamlit.io/).
3. Click **New app**.
4. Select this repository and branch.
5. Set **Main file path** to `streamlit_app.py`.
6. Review Advanced settings if needed, then deploy.

## If deployment fails

- Dependency install failure:
  Check that Streamlit Cloud is using `requirements.txt` from the repo root.
- Model loading failure:
  Confirm `best_fast_model.pth` exists in the repository and Git LFS uploaded it correctly.
- OpenCV import failure:
  Keep `opencv-python-headless` in `requirements.txt` and `libgl1` in `packages.txt`.
