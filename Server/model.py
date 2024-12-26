import tensorflow as tf
from tensorflow.keras.models import load_model
import base64
import numpy as np
from PIL import Image
import io

# Load a pre-trained model (ensure the model file is available)
model = load_model('path_to_your_model.h5')

def analyze_image(image_data):
    # Decode the base64 image
    image_bytes = base64.b64decode(image_data)
    image = Image.open(io.BytesIO(image_bytes))

    # Pre-process image for CNN
    image = image.resize((224, 224))  # Resize image to the required input size
    image = np.array(image) / 255.0  # Normalize pixel values to [0, 1]
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    
    # Predict using the CNN model
    prediction = model.predict(image)
    return prediction.tolist()  # Convert numpy array to list for JSON serialization
