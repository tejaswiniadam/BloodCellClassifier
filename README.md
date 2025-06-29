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
3. **Upload your .h5 model if not present already**

4. **Install dependencies:**

!pip install flask flask-ngrok pyngrok opencv-python pillow
5. **Run the Flask app:**

from pyngrok import ngrok  
ngrok.set_auth_token("YOUR_AUTH_TOKEN")  # Get it from https://dashboard.ngrok.com/get-started/setup  
!python app.py
**🧪 How to Run Locally (Optional)**

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
python app.py
**🖼️ Sample UI**
**📤 Upload Page**
<img src="https://github.com/tejaswiniadam/BloodCellClassifier/main/assets/upload.jpg" width="500" alt="Upload Page">
**✅ Predicted Result**
<img src="https://github.com/tejaswiniadam/BloodCellClassifier/main/assets/predicted.jpg" width="500" alt="Prediction Result">
📌 These screenshots show how the user uploads a blood cell image and receives prediction results using the HematoVision interface.

📂 Folder Structure
├── app.py               # Flask app  
├── Blood_Cell.h5        # Trained model  
├── templates/           # HTML templates (if used)  
├── dataset/             # TRAIN/TEST folders (if applicable)  
├── requirements.txt     # Dependencies  
├── README.md            # Project documentation  
🚀 Deployment Suggestion
For full online deployment, use: Render, Railway
Or keep using Google Colab + ngrok for demo

📬 Contact
Made with ❤️ by Adam Tejaswini
📧 For queries, drop a mail: adamtejaswini1432@gmail.com
