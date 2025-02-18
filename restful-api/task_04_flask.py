#!/usr/bin/env python3
"""
A simple REST API built with Flask.

This API provides endpoints for managing user data with basic CRUD operations:
- GET /: Welcome message
- GET /data: List all usernames
- GET /status: API status
- GET /users/<username>: Get specific user details
- POST /add_user: Add a new user
"""

from flask import Flask, jsonify, request
from http import HTTPStatus
from typing import Dict, Any, List, Union, Tuple

# Initialize Flask application
app = Flask(__name__)

# In-memory storage for users
users: Dict[str, Dict[str, Any]] = {
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
def home() -> str:
    """Root endpoint that returns a welcome message.

    Returns:
        str: Welcome message
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data() -> Tuple[Dict[str, List[str]], int]:
    """Endpoint that returns a list of all usernames.

    Returns:
        Tuple[Dict, int]: List of usernames and HTTP status code
    """
    usernames = list(users.keys())
    return jsonify(usernames), HTTPStatus.OK


@app.route("/status")
def get_status() -> str:
    """Endpoint that returns API status.

    Returns:
        str: Status message
    """
    return "OK"


@app.route("/users/<username>")
def get_user(username: str) -> Tuple[Dict[str, Any], int]:
    """Endpoint that returns details for a specific user.

    Args:
        username (str): Username to look up

    Returns:
        Tuple[Dict, int]: User data and HTTP status code
    """
    if username in users:
        return jsonify(users[username]), HTTPStatus.OK
    return jsonify({"error": "User not found"}), HTTPStatus.NOT_FOUND


@app.route("/add_user", methods=["POST"])
def add_user() -> Tuple[Dict[str, Any], int]:
    """Endpoint to add a new user.

    Expected JSON payload:
    {
        "username": "alice",
        "name": "Alice",
        "age": 25,
        "city": "San Francisco"
    }

    Returns:
        Tuple[Dict, int]: Response message and HTTP status code
    """
    data = request.get_json()

    # Validate required username field
    if not data or "username" not in data:
        return jsonify({
            "error": "Username is required"
        }), HTTPStatus.BAD_REQUEST

    username = data["username"]

    # Create user object with all provided data
    new_user = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", 0),
        "city": data.get("city", "")
    }

    # Add user to storage
    users[username] = new_user

    return jsonify({
        "message": "User added",
        "user": new_user
    }), HTTPStatus.CREATED


def main() -> None:
    """Main function to run the Flask application."""
    app.run(host="127.0.0.1", port=5000)


if __name__ == "__main__":
    main()
