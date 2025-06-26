code = '''
from flask import Flask, request, render_template_string
from pyngrok import ngrok
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from PIL import Image
import io

model = load_model("/content/Blood_Cell.h5")
class_labels = ['eosinophil', 'lymphocyte', 'monocyte', 'neutrophil']

app = Flask(__name__)

html = """
<!doctype html>
<html>
<head>
    <title>HematoVision - Blood Cell Classifier</title>
    <style>
        body { font-family: Arial; background-color: #f4f6f8; text-align: center; }
        .header { background-color: #e74c3c; color: white; padding: 20px; font-size: 24px; font-weight: bold; }
        .section { margin-top: 20px; }
        .section h2 { color: #e74c3c; }
        .result-img { width: 250px; border-radius: 10px; }
    </style>
</head>
<body>
    <div class="header">Welcome to the HematoVision</div>
    <div class="section">
        <h2>About Blood Cells</h2>
        <p>Blood cells are vital components of our body, playing essential roles in immunity, oxygen transport, and clotting.</p>
    </div>
    <div class="section">
        <h2>Predict Blood Cell Type</h2>
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file"><br><br>
            <input type="submit" value="Predict">
        </form>
    </div>
    {% if result %}
    <div class="section">
        <h3>Predicted Cell Type: {{ result }}</h3>
        <img src="data:image/jpeg;base64,{{ img_data }}" class="result-img">
    </div>
    {% endif %}
</body>
</html>
"""

import base64
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
            image.save(buffered, format="JPEG")
            img_data = base64.b64encode(buffered.getvalue()).decode()
    return render_template_string(html, result=result, img_data=img_data)

public_url = ngrok.connect(5000)
print(f"🔗 Public URL: {public_url}")

app.run()
'''

# Save to file
with open("app.py", "w") as f:
    f.write(code)
