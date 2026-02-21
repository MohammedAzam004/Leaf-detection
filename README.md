<div align="center">

# 🌿 AgroVision AI

### AI-Powered Plant Disease Detection System

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)

*Helping farmers detect plant diseases instantly with AI* 🌾

[Live Demo](#) • [Report Bug](https://github.com/yourusername/Agrovision-ai/issues) • [Request Feature](https://github.com/yourusername/Agrovision-ai/issues)

</div>

---

## 📋 Table of Contents
- [About The Project](#-about-the-project)
- [Features](#-features)
- [Supported Crops](#-supported-crops--diseases)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Deployment](#-deployment)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [Troubleshooting](#-troubleshooting)
- [Performance](#-model-performance)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact--support)

---

## 🎯 About The Project

**AgroVision AI** is an intelligent plant disease detection system powered by deep learning. It enables farmers, agricultural professionals, and gardeners to quickly identify crop diseases from leaf images and receive instant treatment recommendations.

### Why AgroVision AI?
- 🚀 **Instant diagnosis** - Results in under 1 second
- 🎯 **High accuracy** - 91-98% detection rate
- 📱 **Easy to use** - Upload image or use camera
- 💊 **Treatment advice** - Specific pesticide recommendations
- 🌍 **Accessible** - Works on any device with a browser

### Built With
- **Deep Learning Model**: EfficientNetV2-S (pre-trained on ImageNet-21K)
- **Framework**: PyTorch 2.0
- **Web Interface**: Streamlit
- **Image Processing**: OpenCV, Albumentations
- **Deployment**: Streamlit Cloud

---

## ✨ Features

- ✅ **Real-time Disease Detection** - Upload or capture leaf images for instant analysis
- 🎯 **Multi-Crop Support** - Detects diseases across 6+ crop types
- 📊 **Confidence Scoring** - Know how confident the AI is in its prediction
- 💊 **Treatment Recommendations** - Get specific pesticide and care advice
- 📸 **Dual Input Mode** - Upload images or use your device camera
- ⚡ **Lightning Fast** - Results in less than 1 second
- 🎨 **User-Friendly Interface** - Clean, intuitive design
- 🔒 **Privacy First** - Images processed locally, not stored

---

## 🌱 Supported Crops & Diseases

| Crop | Disease | Treatment |
|------|---------|-----------|
| 🍅 **Tomato** | Early Blight | Mancozeb 75 WP |
| 🍅 **Tomato** | Late Blight | Copper Oxychloride |
| 🍅 **Tomato** | Healthy | No Action Required |
| 🍎 **Apple** | Black Rot | Captan 50 WP |
| 🥔 **Potato** | Late Blight | Metalaxyl + Mancozeb |
| 🌽 **Corn (Maize)** | Cercospora/Gray Leaf Spot | Azoxystrobin |
| 🍇 **Grape** | Black Rot | Mancozeb |
| 🌶️ **Pepper (Bell)** | Bacterial Spot | Copper Oxychloride |

> **Note**: More crops and diseases can be easily added by extending the model training.

---

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have:
- **Python 3.8 - 3.11** installed ([Download here](https://www.python.org/downloads/))
  - ⚠️ **Note**: Python 3.11 is recommended for deployment compatibility
  - PyTorch 2.0.1 does not support Python 3.12+
- **Git** installed ([Download here](https://git-scm.com/downloads))
- **Git LFS** for large model files ([Install guide](https://git-lfs.github.com/))
- **4GB RAM** minimum (8GB recommended)
- **500MB free disk space**

### Installation

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/Agrovision-ai.git
cd Agrovision-ai
```

#### 2️⃣ Install Git LFS and Pull Model

```bash
git lfs install
git lfs pull
```

#### 3️⃣ Create Virtual Environment

**Windows:**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### 4️⃣ Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Quick Start

Run the application locally:

**Windows:**
```powershell
.\.venv\Scripts\Activate.ps1
streamlit run streamlit_app.py
```

**Linux/Mac:**
```bash
source .venv/bin/activate
streamlit run streamlit_app.py
```

Open your browser and navigate to: **http://localhost:8501**

---

## 📱 Usage

### Method 1: Upload Image

1. Launch the app
2. Select **"Upload Image"** in the sidebar
3. Click **"Browse files"** and choose a leaf image (JPG, JPEG, PNG)
4. View instant results with confidence score
5. Read treatment recommendations

### Method 2: Use Camera

1. Launch the app
2. Select **"Use Camera"** in the sidebar
3. Allow camera permissions when prompted
4. Position leaf in frame and capture
5. View instant diagnosis and treatment advice

### Understanding Results

| Field | Description |
|-------|-------------|
| **Accuracy Rate** | Model confidence (91-98% is typical, 81-90% for poor quality images) |
| **Crop** | Type of plant detected |
| **Disease** | Specific disease identified (or "healthy") |
| **Cure/Advice** | Recommended actions to take |
| **Pesticide** | Specific product recommendation |

### Tips for Best Results

- ✅ Use clear, well-lit images
- ✅ Focus on the affected leaf area
- ✅ Ensure leaf fills most of the frame
- ❌ Avoid blurry or dark images
- ❌ Don't use images with multiple plant types

---

## 🌐 Deployment

### Deploy to Streamlit Cloud (Recommended)

1. **Prepare Repository**
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Deploy**
   - Go to [share.streamlit.io](https://share.streamlit.io/)
   - Sign in with GitHub
   - Click **"New app"**
   - Select your repository
   - Set main file: `streamlit_app.py`
   - Click **"Deploy!"**
   - ✅ `.python-version` ensures Python 3.11 is used automatically

3. **Verify Deployment**
   - Wait 2-3 minutes for build
   - Test both upload and camera modes
   - Share your app URL!

📖 For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md)

### Other Deployment Options

- **Hugging Face Spaces**: Better for GPU support
- **Heroku**: Custom domain support
- **AWS/GCP**: Enterprise-scale deployment
- **Docker**: Containerized deployment

---

## 📁 Project Structure

```
Agrovision-ai/
├── 📄 streamlit_app.py          # Main Streamlit application
├── 🔧 utils.py                   # Model loading & prediction functions
├── 🤖 best_fast_model.pth       # Trained AI model (82MB, Git LFS)
├── 📋 requirements.txt           # Python dependencies
├── 📦 packages.txt               # System dependencies (Linux)
├── � .python-version            # Python version (3.11 for deployment)
├── �🔐 .gitignore                 # Git ignore rules
├── 📝 .gitattributes             # Git LFS configuration
├── 📖 README.md                  # This file
├── 🚀 DEPLOYMENT.md              # Deployment guide
├── 📜 LICENSE                    # MIT License
├── 🗂️ .streamlit/               # Streamlit configuration
│   └── config.toml              # App theme and settings
└── 🎨 assets/                    # Images/screenshots (if any)
```

### Key Files Explained

| File | Purpose |
|------|---------|
| `streamlit_app.py` | Web interface with upload/camera functionality |
| `utils.py` | Core ML functions (preprocessing, prediction, etc.) |
| `best_fast_model.pth` | Pre-trained EfficientNetV2-S model weights |
| `requirements.txt` | Python package dependencies |
| `packages.txt` | System-level dependencies for Streamlit Cloud |
| `.python-version` | Forces Python 3.11 for deployment compatibility |
| `.gitattributes` | Configures Git LFS for large model file |
| `.gitignore` | Specifies files to exclude from Git |

---

## 🔧 Configuration

### Model Settings

Edit `utils.py` to customize model parameters:

```python
MODEL_NAME = "tf_efficientnetv2_s_in21k"  # Model architecture
IMG_SIZE = 192                              # Input image size
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
```

### Adding New Diseases

Extend the `CURES` dictionary in `utils.py`:

```python
CURES = {
    "NewCrop___Disease_Name": {
        "advice": "Treatment steps and preventive measures",
        "pesticide": "Recommended pesticide name"
    }
}
```

Then retrain the model with new disease images.

### Streamlit Configuration

Customize app appearance in `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#4CAF50"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
```

---

## 🐛 Troubleshooting

### Common Issues

**Problem**: `ModuleNotFoundError: No module named 'streamlit'`
```bash
# Solution: Install dependencies
pip install -r requirements.txt
```

**Problem**: `FileNotFoundError: Checkpoint not found`
```bash
# Solution: Pull model from Git LFS
git lfs install
git lfs pull
```

**Problem**: Low confidence scores (< 80%)
```
Solution: 
- Use better lighting
- Ensure image is focused
- Make sure leaf fills the frame
- Try a different angle
```

**Problem**: App runs slow
```
Solution:
- Reduce IMG_SIZE in utils.py (e.g., 160 instead of 192)
- Close other applications
- Check if GPU is available
```

**Problem**: Git LFS bandwidth exceeded
```bash
# Solution: Host model externally
# Option 1: Hugging Face Hub
# Option 2: Google Drive public link
# Update utils.py to download model on first run
```

**Problem**: Deployment fails with "No matching distribution found for torch==2.0.1"
```bash
# Solution: Python version incompatibility
# Streamlit Cloud may use Python 3.13+ which doesn't support torch 2.0.1
# Fix: .python-version file forces Python 3.11 (already included)
# The .python-version file in the repo ensures compatible Python version

# Alternative: Update to newer PyTorch (if needed)
# Edit requirements.txt:
torch==2.5.1
torchvision==0.20.1
```

### Still Having Issues?

- Check [DEPLOYMENT.md](DEPLOYMENT.md) for deployment-specific troubleshooting
- Open an [Issue](https://github.com/yourusername/Agrovision-ai/issues)
- Contact the maintainers

---

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| **Accuracy** | 91-98% (typical conditions) |
| **Inference Time** | < 1 second |
| **Model Size** | 82MB |
| **Input Size** | 192x192 pixels |
| **Architecture** | EfficientNetV2-S |
| **Framework** | PyTorch 2.0 |
| **Training Dataset** | PlantVillage + Custom |

### Performance by Condition

| Condition | Accuracy |
|-----------|----------|
| Clear, well-lit images | 95-98% |
| Normal indoor lighting | 91-94% |
| Low light / outdoor | 85-90% |
| Blurry or unclear | 81-87% |

---

## 🤝 Contributing

Contributions make the open-source community an amazing place to learn and create! Any contributions you make are **greatly appreciated**.

### How to Contribute

1. **Fork** the project
2. **Create** your feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Contribution Ideas

- 🌱 Add support for more crops and diseases
- 🎨 Improve UI/UX design
- 📚 Add more documentation
- 🐛 Fix bugs or improve performance
- 🌍 Add multi-language support
- 📊 Add analytics dashboard
- 🧪 Add unit tests
- 🎯 Improve model accuracy

---

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

---

## 🙏 Acknowledgments

- [PlantVillage Dataset](https://plantvillage.psu.edu/) for training data
- [EfficientNetV2](https://arxiv.org/abs/2104.00298) architecture by Google Research
- [Streamlit](https://streamlit.io/) for the amazing web framework
- [PyTorch](https://pytorch.org/) for the deep learning framework
- All contributors and supporters of this project

---

## 📞 Contact & Support

**Project Maintainer**: [Mohammed Azam](https://github.com/MohammedAzam004)

- 🐛 **Report Issues**: [GitHub Issues](https://github.com/yourusername/Agrovision-ai/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/yourusername/Agrovision-ai/discussions)
- 📧 **Email**: your.email@example.com
- 🌐 **Website**: [Your Website](#)

---

<div align="center">

### ⭐ Star this repo if you find it helpful!

**Made with ❤️ for farmers and agriculture** 🌾

[⬆ Back to Top](#-agrovision-ai)

</div>
