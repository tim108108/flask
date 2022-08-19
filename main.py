from flask import Flask, render_template, request, Response, send_file, jsonify
import os, sys, re, base64, cv2
import numpy as np
from PIL import Image
from io import BytesIO
sys.path.append(os.getcwd()+"/yolov5")
import detect

def base64_to_pil(img_base64):
    """
    Convert base64 image data to PIL image
    """
    image_data = re.sub('^data:image/.+;base64,', '', img_base64)
    pil_image = Image.open(BytesIO(base64.b64decode(image_data)))
    #img = cv2.cvtColor(pil_image, cv2.COLOR_BGR2RGB)
    return pil_image


def np_to_base64(img_np):
    """
    Convert numpy image (RGB) to base64 string
    """
    img = Image.fromarray(img_np.astype('uint8'), 'RGB')
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return u"data:image/png;base64," + base64.b64encode(buffered.getvalue()).decode("ascii")

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        img = base64_to_pil(request.json)
        # Save the image to ./uploads
        img.save("./uploads/image.png")
        # Make prediction
        preds = detect.run(source="./uploads/image.png", project="./uploads", name="./pred", exist_ok=True)
        pred_img = cv2.imread("./uploads/pred/image.png")
        return send_file(
            BytesIO(pred_img),
            mimetype="image/png")
    return None

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)
