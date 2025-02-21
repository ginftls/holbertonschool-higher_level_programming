#!/usr/bin/python3
"""Module for fetch_and_print_posts and fetch_and_save_posts methods"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database for storing users
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
    """Root endpoint to welcome users to the API"""
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
    """Returns the full user object for the specified username"""
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Adds a new user to the in-memory database"""
    # Get the JSON data from the request
    user_data = request.json

    # Check if username is provided
    if 'username' not in user_data:
        return jsonify({"error": "Username is required"}), 400

    # Extract username
    username = user_data['username']

    # Add the user to our in-memory database
    users[username] = user_data

    # Return confirmation with the user data
    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201


if __name__ == "__main__":
    app.run(debug=True)
