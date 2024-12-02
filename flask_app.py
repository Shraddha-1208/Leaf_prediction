import os
import numpy as np
import tensorflow as tf
from flask import Flask, request, render_template, jsonify
from tensorflow.keras.preprocessing import image

# Initialize Flask app
app = Flask(__name__)

# Ensure 'uploads' directory exists
if not os.path.exists('./uploads'):
    os.makedirs('./uploads')

# Load the pre-trained model
model = tf.keras.models.load_model('model.h5')

# Load class names from the training data
class_names = ['Apple', 'Berry', 'Fig', 'Guava', 'Orange', 'Palm', 'Persimmon', 'Tomato']

# Allowed image extensions
allowed_extensions = {'jpg', 'jpeg', 'png', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for predicting class of uploaded image
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the uploaded file
        img_file = request.files['image']

        # Validate the file type
        if not allowed_file(img_file.filename):
            return jsonify({'error': 'Invalid file type. Please upload an image.'})

        # Save the uploaded file
        img_path = './uploads/' + img_file.filename
        img_file.save(img_path)

        # Load and preprocess the image
        img = image.load_img(img_path, target_size=(150, 150))  # Resize the image
        img_array = image.img_to_array(img)  # Convert image to array
        img_array = img_array / 255.0  # Normalize image
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        # Make prediction
        prediction = model.predict(img_array)

        # Get predicted class index
        predicted_class_index = np.argmax(prediction, axis=1)

        # Map the index to the class name
        predicted_class_name = class_names[predicted_class_index[0]]

        # Remove the uploaded file
        os.remove(img_path)

        # Return the prediction result
        return jsonify({'prediction': predicted_class_name})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
