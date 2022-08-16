from flask import Flask, render_template, request
import util.py

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the image from post request
        img = base64_to_pil(request.json)
        # Save the image to ./uploads
        # img.save("./uploads/image.png")
        # Make prediction
        preds = model_predict(img, model)
        # Process your result for human
        pred_proba = "{:.3f}".format(np.amax(preds))    # Max probability
        pred_class = decode_predictions(preds, top=1)   # ImageNet Decode
        result = str(pred_class[0][0][1])               # Convert to string
        result = result.replace('_', ' ').capitalize()
        # Serialize the result, you can add additional fields
        return jsonify(result=result, probability=pred_proba)
    return None

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)
