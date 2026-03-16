# 🤗 Deploy to Hugging Face Spaces

## Why Hugging Face Spaces?

✅ **Free hosting** for ML applications  
✅ **Handles large models** (no Git LFS issues)  
✅ **Python 3.11 support** (no compatibility issues)  
✅ **GPU acceleration** available (optional)  
✅ **Great for AI/ML** community visibility  
✅ **Auto-deployment** from GitHub  

---

## 🚀 Quick Deploy (5 Minutes)

### Step 1: Create Hugging Face Account

1. Go to [huggingface.co](https://huggingface.co/)
2. Click **Sign Up** (or sign in with GitHub)
3. Verify your email

### Step 2: Create a New Space

1. Go to [huggingface.co/spaces](https://huggingface.co/spaces)
2. Click **"Create new Space"**
3. Fill in details:
   - **Space name:** `agrovision-ai` (or your choice)
   - **License:** MIT
   - **Select SDK:** Streamlit
   - **Space hardware:** CPU basic (free) or upgrade for GPU
   - **Visibility:** Public (or Private)
4. Click **"Create Space"**

### Step 3: Connect to GitHub (Recommended)

**Option A: GitHub Sync (Easiest)**

1. In your new Space, click **"Settings"**
2. Scroll to **"Repository sync"**
3. Click **"Connect a Repository"**
4. Select your GitHub repo: `MohammedAzam004/Leaf-detection`
5. Enable **"Sync on every commit"**
6. Click **"Connect"**

✅ **Done!** Your app will auto-deploy whenever you push to GitHub.

**Option B: Manual Upload**

1. Clone the Hugging Face Space repo:
   ```bash
   git clone https://huggingface.co/spaces/yourusername/agrovision-ai
   cd agrovision-ai
   ```

2. Copy your files:
   ```bash
   # Copy all files from your project
   copy path\to\Agrovision-ai\* .
   ```

3. Create `README.md` header (important!):
   ```yaml
   ---
   title: AgroVision AI
   emoji: 🌿
   colorFrom: green
   colorTo: blue
   sdk: streamlit
   sdk_version: 1.31.0
   python_version: 3.11
   app_file: streamlit_app.py
   pinned: false
   license: mit
   ---

   # 🌿 AgroVision AI

   AI-powered plant disease detection system...
   (rest of your README)
   ```

4. Commit and push:
   ```bash
   git add .
   git commit -m "Deploy AgroVision AI"
   git push
   ```

### Step 4: Verify Deployment

1. Go to your Space URL: `https://huggingface.co/spaces/yourusername/agrovision-ai`
2. Wait 2-3 minutes for build (watch the logs)
3. Test your app:
   - Upload a leaf image
   - Try camera mode
   - Verify predictions work

---

## 📝 Configuration Files

### Required: README.md Header

Add this YAML header at the top of your README.md:

```yaml
---
title: AgroVision AI
emoji: 🌿
colorFrom: green
colorTo: blue
sdk: streamlit
sdk_version: 1.31.0
python_version: 3.11
app_file: streamlit_app.py
pinned: false
license: mit
tags:
  - agriculture
  - plant-disease
  - computer-vision
  - pytorch
  - efficientnet
---
```

### Files Needed

Your repository already has everything needed:

```
✅ streamlit_app.py          # Main app
✅ utils.py                   # Functions
✅ requirements.txt           # Dependencies
✅ packages.txt               # System deps
✅ best_fast_model.pth       # Model (will be uploaded)
✅ .streamlit/config.toml    # Config
```

---

## 🐛 Troubleshooting

### Build Fails

**Problem:** Dependencies fail to install

**Solution:**
1. Check build logs in your Space
2. Verify `python_version: 3.11` in README header
3. Ensure `requirements.txt` is valid

### Model File Too Large

**Problem:** "File too large to upload"

**Solution:**
1. Hugging Face supports files up to 50GB
2. For very large files, use Git LFS:
   ```bash
   git lfs install
   git lfs track "*.pth"
   git add .gitattributes
   git add best_fast_model.pth
   git commit -m "Add model with LFS"
   ```

### App Crashes on Startup

**Problem:** App shows error on load

**Solutions:**
- Check model file is present: `best_fast_model.pth`
- Verify paths in `utils.py` are correct
- Check logs for specific errors

### Slow Performance

**Solution:** Upgrade to GPU hardware:
1. Go to Space Settings
2. **"Change hardware"** → Select GPU
3. Note: GPU spaces use your credits

---

## 💡 Advanced Options

### Add GPU Acceleration

1. Go to your Space → **Settings**
2. **"Change hardware"**
3. Select **"T4 small"** or higher
4. Enjoy faster inference! 🚀

### Custom Domain

1. Go to Space Settings
2. **"Domain"** section
3. Add your custom domain
4. Follow DNS configuration steps

### Private Space

1. Space Settings → **"Visibility"**
2. Select **"Private"**
3. Only you can access the app

### Add a README Card

Make your Space look professional:

```markdown
---
title: AgroVision AI
emoji: 🌿
colorFrom: green
colorTo: blue
sdk: streamlit
sdk_version: 1.31.0
python_version: 3.11
app_file: streamlit_app.py
---

# 🌿 AgroVision AI

![Demo](https://via.placeholder.com/800x400?text=App+Screenshot)

## About

Detect plant diseases instantly using AI. Upload a leaf image and get:
- Disease identification
- Confidence score
- Treatment recommendations
- Pesticide suggestions

## Features

- 91-98% accuracy
- 8+ crop types supported
- Real-time processing
- Camera & upload modes

## How to Use

1. Upload a clear leaf image
2. Wait 1 second for analysis
3. Read the diagnosis and treatment advice

## Technology

- PyTorch 2.0 & EfficientNetV2-S
- Trained on PlantVillage dataset
- OpenCV image processing
```

---

## 🔗 Useful Links

- **Your Space:** `https://huggingface.co/spaces/yourusername/agrovision-ai`
- **HF Spaces Docs:** https://huggingface.co/docs/hub/spaces
- **Streamlit on HF:** https://huggingface.co/docs/hub/spaces-sdks-streamlit
- **HF Community:** https://discuss.huggingface.co/

---

## ✅ Checklist

Before deploying, ensure:

- [ ] Hugging Face account created
- [ ] Space created with Streamlit SDK
- [ ] README.md has YAML header with `python_version: 3.11`
- [ ] All files present: app, utils, requirements, model
- [ ] GitHub sync enabled (optional but recommended)
- [ ] Tested locally: `streamlit run streamlit_app.py`

---

## 🆘 Need Help?

- **Build failing?** Check the build logs in your Space
- **Model not loading?** Verify file paths in `utils.py`
- **Python version issues?** Ensure README header has `python_version: 3.11`
- **Still stuck?** Ask on [HF Forum](https://discuss.huggingface.co/)

---

**🎉 Deploy in 5 minutes and share your AI app with the world!**

Happy Deploying! 🚀🌿
