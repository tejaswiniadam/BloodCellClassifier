# 🩸 Hematovision 
## 🔬 Blood Cell Classification Web App  


## 📁 Dataset

The dataset used is from [Kaggle: Blood Cell Images](https://www.kaggle.com/datasets/paultimothymooney/blood-cells)  
It contains four types of blood cell images organized into `TRAIN` and `TEST` folders.

## 🧠 Model Details

- **Base Model**: MobileNetV2 (pretrained on ImageNet)
- **Image Size**: 224x224
- **Training Tool**: TensorFlow / Keras
- **Final Format**: `Blood_Cell.h5` (saved model)

## 🖥️ Web App Features

- Upload a blood cell image
- Get real-time predictions
- Clean UI with header and background (HTML/CSS styled)

### 🛠️ How to Run This Project in Google Colab

1. **Upload the dataset ZIP to your Colab Drive**

2. **Clone this repo**:  
   ```bash
   !git clone https://github.com/your-username/your-repo-name.git
   ```

3. **Upload your `.h5` model** if not present already

4. **Install dependencies**:  
   ```bash
   !pip install flask flask-ngrok pyngrok opencv-python pillow
   ```

5. **Run the Flask app**:  
   ```python
   from pyngrok import ngrok  
   ngrok.set_auth_token("YOUR_AUTH_TOKEN")  # Get it from https://dashboard.ngrok.com/get-started/setup  
   !python app.py
   ```
   
## 🧪 How to Run Locally (Optional)
- git clone https://github.com/your-username/your-repo-name.git
- cd your-repo-name
- pip install -r requirements.txt
- python app.py
## 🖼️ Sample UI
<!-- You can upload an image in GitHub repo and update this path -->

### 📂 Folder Structure
```
├── app.py              # Flask app  
├── Blood_Cell.h5       # Trained model  
├── templates/          # HTML templates (if used)  
├── dataset/            # TRAIN/TEST folders (if applicable)  
├── README.md           # Project description  
```

### 🚀 Deployment Suggestion

For full online deployment, use: **Render**, **Railway**  
Or keep using **Google Colab + ngrok** for demo  

---

### 📬 Contact

Made with ❤️ by **Adam Tejaswini**  
📧 For queries, drop a mail: [adamtejaswini1432@gmail.com](mailto:adamtejaswini1432@gmail.com)


