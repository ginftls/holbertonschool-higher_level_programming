#!/usr/bin/env python3
"""
A Flask-based REST API for managing user data.
Implements all CRUD operations with proper error handling and response formats.
"""

from flask import Flask, jsonify, request
from http import HTTPStatus

# Initialize Flask application
app = Flask(__name__)

# In-memory storage for users
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


@app.route("/")
def home():
    """Root endpoint returning welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Return list of all usernames."""
    return jsonify(list(users.keys()))


@app.route("/status")
def get_status():
    """Return API status."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Return user details for given username."""
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), HTTPStatus.NOT_FOUND


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user to the system."""
    data = request.get_json()

    # Check if username is provided
    if not data or "username" not in data:
        return jsonify({
            "error": "Username is required"
        }), HTTPStatus.BAD_REQUEST

    # Create new user entry
    username = data["username"]
    new_user = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    # Add to users dictionary
    users[username] = new_user

    # Return success response
    return jsonify({
        "message": "User added",
        "user": new_user
    }), HTTPStatus.CREATED


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
