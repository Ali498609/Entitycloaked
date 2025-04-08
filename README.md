## EntityCloaked

**EntityCloaked** is an open-source privacy-preserving tool that leverages deep learning and computer vision to automatically detect human faces in images and overlay them with custom graphics (like emoji or illustrations) for anonymization purposes. 
The goal is to protect the identities of individuals captured in photos, especially in datasets or public content.

---

## 🚀 Motivation

This project was born out of a real need: the creator developed a dataset for ISL (Indian Sign Language) research but faced privacy concerns regarding sharing images that revealed their face. 
The manual process of editing each image was tedious, and existing free tools either lacked the required functionality or were locked behind paywalls.

Inspired by this challenge, **EntityCloaked** was created — not just for personal use but as a public good. Many content creators, researchers, 
and developers face similar issues when sharing data or publishing media that contains identifiable individuals. This tool aims to solve that.

---

## 🧠 Features

- 👨‍🔬 **Face Detection** using a YOLOv11-based custom-trained model.
- 🌈 **Automatic Overlay** (e.g., emoji, blurred png) on top of detected faces.
- 👁️ **Preserves image quality** while anonymizing.
- 📂 **Batch Processing**: Process an entire folder of images in one go.
- 🌐 **Fully Offline**: No internet or third-party services needed.
- 🔒 **Privacy Focused**: No data leaves your machine.

---

## 🛠 How It Works

1. The user provides a folder of images they want to anonymize.
2. A YOLOv11 model detects human faces.
3. A custom overlay image (e.g., emoji or blurred pngs) is resized and positioned over each detected face.
4. The edited image is saved to a separate output folder.

---

## 🧰 Requirements

- Python 3.8+
- [Ultralytics YOLOv11](https://github.com/ultralytics/ultralytics)
- Pillow
- Torch
- Download best.pt(train on public dataset in kaggle) model from releases tab

## Install dependencies:
```bash
pip install ultralytics pillow torch
python script.py <input_folder> <output_folder>

# Make sure your model path and overlay image are correctly set in the script:
model = YOLO("path/to/best.pt")
overlay = Image.open("overlay.png").convert("RGBA")
```

## 🤝 Ideal Use Cases

* Preparing datasets for machine learning research while preserving privacy.

* Vloggers or content creators editing public footage.

* Teachers/students sharing class recordings or group photos.

* Surveillance video anonymization.

## 🛠️ Contributing

Pull requests and suggestions are welcome! If you have ideas to improve performance, UI, or want to add new overlay options — open an issue or contribute directly.

## 🚫 Disclaimer

This tool is designed for ethical use only. Please ensure that anonymization is compliant with local laws and that you have the right to modify and share the images.

## 📚 License

-This project is open-source and available under the MIT License.

-Made with ❤️ for privacy-conscious creators.
## Details

Project Name: EntityCloaked

Author: Shaik Alisha

Purpose: Making facial privacy accessible to everyone.
