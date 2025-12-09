"""
Create a Flask application with an /api route.
When this route is accessed, it should return a JSON list.
The data should be stored in a backend file, read from it, and sent as a response.
"""

from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')

@app.route("/api", methods=['GET'])

def get_backend_data():
    try:
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"})

if __name__ == '__main__':
    app.run(debug=True)