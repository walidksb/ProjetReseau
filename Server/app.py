from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from model import analyze_image  # Import CNN analysis function
import threading

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)

# Create an API endpoint for analysis via HTTP
@app.route('/api/analyze', methods=['POST'])
def analyze_image_api():
    data = request.get_json()  # Expect image data in base64 format
    image_data = data['image']
    prediction = analyze_image(image_data)
    return jsonify({"prediction": prediction})

# SocketIO for real-time communication
@socketio.on('image_data')
def handle_image_data(data):
    print(f"Received image data: {data['image']}")
    result = analyze_image(data['image'])  # Analyze image with CNN
    emit('analysis_result', {'prediction': result})  # Send result back

# Multi-threading example: handling client requests in parallel
def run_socket():
    socketio.run(app, debug=True, host='0.0.0.0', port=5000, threaded=True)

if __name__ == '__main__':
    # Run Flask with threading support to handle requests concurrently
    threading.Thread(target=run_socket).start()
