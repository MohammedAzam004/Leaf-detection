# 🚀 Streamlit Cloud Deployment Guide

## Pre-Deployment Checklist

### ✅ Files Prepared
- `requirements.txt` - Updated with deployment-friendly versions
- `packages.txt` - Linux system dependencies for OpenCV
- `.gitattributes` - Git LFS configuration for large model files
- Error handling added to streamlit_app.py

### 📝 Next Steps

#### 1. Rename Model File (Important!)
```bash
# Rename the model file to remove spaces and parentheses
mv "best_fast_model (1).pth" best_fast_model.pth
```

#### 2. Check Model File Size
```bash
# Check if model is larger than 100MB
dir "best_fast_model (1).pth"
```

**If larger than 100MB:**
- Install Git LFS: `git lfs install`
- Track model: `git lfs track "*.pth"`
- Add and commit normally

**Alternative for very large models:**
- Upload to Hugging Face Hub or Google Drive
- Download in code using `@st.cache_resource`

#### 3. Push to GitHub
```bash
git add .
git commit -m "Prepare for Streamlit deployment"
git push
```

#### 4. Deploy on Streamlit Cloud
1. Go to https://share.streamlit.io/
2. Sign in with GitHub
3. Click "New app"
4. Select your repository
5. Set main file path: `streamlit_app.py`
6. Click "Deploy!"

### ⚙️ Configuration Options

**For CPU-only deployment (recommended for smaller models):**
- Current requirements.txt already uses standard PyTorch
- Streamlit Cloud will use CPU by default

**For GPU acceleration (if available):**
- Not typically available on free Streamlit Cloud tier
- Consider using Hugging Face Spaces with GPU

### 🔧 Troubleshooting

**Memory Error:**
- Reduce IMG_SIZE in utils.py (currently 192)
- Use model quantization/pruning

**Import Errors:**
- Verify all packages in requirements.txt
- Check packages.txt for system dependencies

**Model Loading Issues:**
- Ensure model file is in repository root
- Check Git LFS is properly configured
- Verify MODEL_PATH in utils.py

### 📊 Performance Tips

1. **Model is cached** via `@st.cache_resource` ✅
2. **Use spinner** for loading feedback ✅
3. **Error handling** prevents crashes ✅

### 🌐 Local Testing Before Deploy
```bash
# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Run locally
streamlit run streamlit_app.py
```

Test both upload and camera modes!

### 📱 Post-Deployment
- Share your app URL
- Monitor logs in Streamlit Cloud dashboard
- Update model by pushing new .pth file
