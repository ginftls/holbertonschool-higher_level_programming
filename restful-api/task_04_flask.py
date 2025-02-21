#!/usr/bin/python3
"""Module for handling routes with Flask to respond to different endpoints"""

from flask import Flask, jsonify, request

# Initialize Flask application
app = Flask(__name__)

# Initialize in-memory users dictionary
# Note: Example in instructions shows users without username field,
# but expected output shows users with username field
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
    """Handle root endpoint"""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """Return a list of all usernames"""
    return jsonify(list(users.keys()))


@app.route('/status')
def get_status():
    """Return API status"""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Return user data for the specified username"""
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user via POST request"""
    # Get request data as JSON
    user_data = request.get_json()

    # Check if username is provided
    if 'username' not in user_data:
        return jsonify({"error": "Username is required"}), 400

    # Get username from the data
    username = user_data['username']

    # Store the user in our dictionary
    users[username] = user_data

    # Return confirmation with 201 Created status
    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201


if __name__ == "__main__":
    app.run(debug=True)
