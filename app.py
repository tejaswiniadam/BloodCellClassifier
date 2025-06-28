from flask import Flask, request, render_template
from pyngrok import ngrok
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from PIL import Image
import io
import base64

# Load the trained model
model = load_model("Blood_Cell.h5")
class_labels = ['eosinophil', 'lymphocyte', 'monocyte', 'neutrophil']

# Initialize Flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def upload_predict():
    result = ""
    img_data = ""
    if request.method == "POST":
        file = request.files['file']
        if file:
            image = Image.open(io.BytesIO(file.read()))
            image_rgb = image.convert("RGB")
            resized = image_rgb.resize((224, 224))
            image_np = np.array(resized)
            image_np = preprocess_input(image_np.reshape(1, 224, 224, 3))

            prediction = model.predict(image_np)
            class_idx = np.argmax(prediction)
            result = class_labels[class_idx]

            buffered = io.BytesIO()
            image_rgb.save(buffered, format="JPEG")
            img_data = base64.b64encode(buffered.getvalue()).decode()

            return render_template("result.html", result=result, img_data=img_data)

    return render_template("home.html")

# Start ngrok tunnel and Flask app
public_url = ngrok.connect(5000)
print(f"🔗 Public URL: {public_url}")
app.run()
