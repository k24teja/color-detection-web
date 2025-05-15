from flask import Flask, render_template, request
import cv2
import os
from werkzeug.utils import secure_filename
from color_recognition_api import color_histogram_feature_extraction, knn_classifier

UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    uploaded_img_path = None

    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            uploaded_img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(uploaded_img_path)

            image = cv2.imread(uploaded_img_path)

            color_histogram_feature_extraction.color_histogram_of_test_image(image)
            prediction = knn_classifier.main('training.data', 'test.data')

    return render_template('index.html', prediction=prediction, image_path=uploaded_img_path)

if __name__ == '__main__':
    app.run(debug=True)
