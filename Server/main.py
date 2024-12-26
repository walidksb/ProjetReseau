from flask import Flask, jsonify, request
from flask_cors import CORS  # Pour gérer les requêtes CORS depuis React

app = Flask(__name__)
CORS(app)  # Permet à React d'effectuer des requêtes vers Flask

@app.route('/api/analyze', methods=['POST'])
def analyze_image():
    # Traitement de l'image ou des données
    data = request.get_json()
    result = {"message": "Image analysée", "status": "success"}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
