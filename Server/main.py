from flask import Flask, jsonify, request
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS to allow communication with the React application

# Define a route for the home page
@app.route('/')
def home():
    return "Welcome to the Flask API for React Integration!"

# Example route to handle user data
@app.route('/api/user', methods=['POST'])
def create_user():
    data = request.get_json()
    return jsonify({"message": "User data received!", "user": data}), 201

# Example route to fetch some data
@app.route('/api/data', methods=['GET'])
def get_data():
    sample_data = {
        "id": 1,
        "name": "Sample Data",
        "description": "This is an example data fetched from Flask API."
    }
    return jsonify(sample_data)

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
