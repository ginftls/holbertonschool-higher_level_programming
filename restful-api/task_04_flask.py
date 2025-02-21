#!/usr/bin/python3
"""Module for handling routes with Flask to respond to different endpoints"""

from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Initialize the in-memory users dictionary with the example data
users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}


@app.route('/')
def home():
    """Root endpoint that returns a welcome message"""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """Returns a list of all usernames stored in the API"""
    return jsonify(list(users.keys()))


@app.route('/status')
def get_status():
    """Returns the API status"""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Returns the full object corresponding to the provided username"""
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Handles POST requests to add a new user
    Returns 201 on success, 400 if username is missing
    """
    # Get JSON data from request
    user_data = request.get_json()

    # Check if username is provided
    if 'username' not in user_data:
        return jsonify({"error": "Username is required"}), 400

    # Add the user to the users dictionary
    username = user_data['username']
    users[username] = user_data

    # Return confirmation message with 201 status code
    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201


if __name__ == "__main__":
    app.run(debug=True)
