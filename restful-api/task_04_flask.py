#!/usr/bin/python3
"""Module for fetch_and_print_posts and fetch_and_save_posts methods"""

from flask import Flask, jsonify, request

# Initialize Flask application
app = Flask(__name__)

# In-memory database for storing users - preloaded with sample data
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
    # Extract just the usernames as a list
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route('/status')
def get_status():
    """Returns the API status"""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Returns the full user object for the specified username
    or an error if the user doesn't exist
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Adds a new user to the users dictionary
    Requires JSON with at least a username field
    """
    # Ensure the request contains JSON data
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    # Get the user data from the request
    user_data = request.get_json()

    # Validate required fields
    if 'username' not in user_data:
        return jsonify({"error": "Username is required"}), 400

    username = user_data['username']

    # Create the complete user object
    new_user = {
        "username": username,
        "name": user_data.get("name", ""),
        "age": user_data.get("age", 0),
        "city": user_data.get("city", "")
    }

    # Store the user in our dictionary
    users[username] = new_user

    # Return success message with 201 Created status code
    return jsonify({
        "message": "User added",
        "user": new_user
    }), 201


if __name__ == "__main__":
    app.run(debug=True)
