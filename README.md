## Fruit Leaf Prediction Web Application

This project is a **Fruit Leaf Prediction Web Application** that allows users to upload an image of a fruit leaf, and the application will predict the type of fruit based on the leaf image using a pre-trained deep learning model. The application is built using **Flask** (a Python web framework) for handling user requests and **TensorFlow** for the machine learning model. The model is trained to classify images of fruit leaves, and it predicts fruit categories like **Apple**, **Berry**, **Fig**, **Guava**, **Orange**, **Palm**, **Persimmon**, and **Tomato**.

The application provides a simple web interface where users can upload fruit leaf images and receive real-time predictions. It is designed to handle common image formats, such as `.jpg`, `.jpeg`, `.png`, and `.gif`.

### How it Works:
1. **User Uploads an Image**: The user selects an image file of a fruit leaf from their local system via a simple HTML form.
2. **Flask Server**: The Flask server receives the image and saves it temporarily in the `uploads` directory.
3. **Image Preprocessing**: The image is processed by resizing it, normalizing the pixel values, and preparing it for the model input.
4. **Model Prediction**: A pre-trained **TensorFlow** model (saved as `model.h5`) is used to predict the type of fruit based on the leaf image.
5. **Prediction Result**: Once the model makes a prediction, the result is sent back to the web page, where the predicted fruit class is displayed.

### Features:
- **Leaf Image Upload**: Users can upload an image of a fruit leaf to predict its associated fruit type.
- **Real-time Prediction**: The model makes predictions and displays the results instantly.
- **Simple UI**: The app provides a clean and intuitive user interface for easy interaction.
- **Error Handling**: The app includes validation for file types and handles errors gracefully, providing helpful feedback to the user.
