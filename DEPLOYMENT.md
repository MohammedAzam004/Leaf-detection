# Deployment Guide

This project is set up for deployment on Streamlit Community Cloud.

## Required Files

Make sure these files are present in the repository root:

- `streamlit_app.py`
- `requirements.txt`
- `packages.txt`
- `best_fast_model.pth`

## Before You Deploy

1. Confirm the model file is available in GitHub and Git LFS is working correctly.
2. Confirm `requirements.txt` contains the exact Python packages needed by the app.
3. Confirm `packages.txt` contains any Linux dependencies required during deployment.
4. Do not commit `.env`, `.env.*`, or `.streamlit/secrets.toml`.

## Deploy On Streamlit Community Cloud

1. Push the latest code to GitHub.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/).
3. Click **Create app**.
4. Choose your repository and branch.
5. Set the file path to `streamlit_app.py`.
6. Open **Advanced settings** if you want to choose the Python version or add secrets.
7. Deploy the app.

## Dependency Notes

- Python dependencies are installed from `requirements.txt`.
- Linux packages are installed from `packages.txt`.
- Streamlit recommends pinning the Streamlit version in `requirements.txt`.
- Use only one Python dependency file for the app.

## If Deployment Fails

### Model loading error

- verify `best_fast_model.pth` exists in the repository root
- verify Git LFS uploaded the real model file correctly

### Missing dependency error

- verify the package is listed in `requirements.txt`
- verify the repository root contains `requirements.txt`

### OpenCV import error

- keep `opencv-python-headless` in `requirements.txt`
- keep `libgl1` in `packages.txt`

### Python version mismatch

- redeploy the app and choose a supported Python version from Advanced settings

## Secrets

If you later add APIs or external services:

- store secrets in Streamlit Community Cloud app settings
- do not hardcode credentials in Python files
- do not commit `.env` or `secrets.toml` files

## References

Current Streamlit documentation used for this deployment guide:

- [Deploy your app on Community Cloud](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy)
- [App dependencies for Community Cloud](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies)
- [Manage your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app)
