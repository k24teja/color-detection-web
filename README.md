=======================================================
COLOR DETECTION USING MACHINE LEARNING (KNN + FLASK)
=======================================================

DESCRIPTION:
------------
This project implements a machine learning-based system for detecting dominant colors in images using a K-Nearest Neighbors (KNN) classifier. It includes a Flask web interface that allows users to upload an image and get the detected color name in real-time.

The model is trained using RGB histograms extracted from labeled training images of known colors. The classifier then compares features of the uploaded image with those of the training set to predict the closest color match.

FEATURES:
---------
- Uses RGB color histogram for feature extraction
- Implements a KNN algorithm for classification
- Supports 8 basic colors: red, yellow, green, orange, white, black, blue, and violet
- Provides a web interface for easy image upload and result display
- Real-time prediction of dominant color from an uploaded image

PROJECT STRUCTURE:
------------------
color_recognition_api/
├── knn_classifier.py                # KNN model implementation
├── color_histogram_feature_extraction.py  # Feature extraction logic
training_dataset/
├── red/, green/, blue/, etc.        # Folders with labeled training images
static/uploads/                      # Stores uploaded images
templates/
├── index.html                       # HTML interface for uploading and displaying results
app.py                               # Flask server code

REQUIREMENTS:
-------------
- Python 3.6+
- OpenCV (cv2)
- Flask
- PIL (Pillow)
- NumPy

INSTALLATION:
-------------
1. Clone the repository or copy the code files into a working directory.
2. Set up a Python virtual environment (optional but recommended):

   python -m venv venv
   source venv/bin/activate  (Linux/Mac)
   venv\Scripts\activate     (Windows)

3. Install required packages:

   pip install opencv-python flask numpy pillow

4. Place your training images in the respective folders under training_dataset/ (e.g., red, blue, green...).

USAGE:
------
1. Run the feature extractor to build training data:

   python color_recognition_api/color_histogram_feature_extraction.py

   This generates training.data used by the KNN classifier.

2. Launch the Flask app:

   python app.py

3. Open your browser and go to:

   http://127.0.0.1:5000/

4. Upload an image — the application will predict and display the dominant color.

HOW IT WORKS:
-------------
- The feature extractor calculates the histogram peaks of RGB channels.
- These peak values are saved as training data with color labels.
- When a new image is uploaded, the system extracts RGB peaks and compares them with training data using KNN (with Euclidean distance).
- The majority vote among the K=3 nearest neighbors determines the predicted color.

KNOWN ISSUES / LIMITATIONS:
---------------------------
- Classification is limited to the color categories provided in the training dataset.
- Performance may vary with lighting or background complexity.
- Model accuracy is dependent on quality and quantity of training images.

CREDITS:
--------
Developed by: [Your Name or Team Name]
Inspired by: Open-source image recognition projects and academic references in color detection.

LICENSE:
--------
This project is open-source and free to use under the MIT License.
