#!/usr/bin/python3
"""API Security and Authentication Techniques"""

from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash
from functools import wraps
import datetime as dt

# Setup Flask application
app = Flask(__name__)

# Configure the secret key for signing and verifying tokens
SECRET_KEY = 'your-secure-secret-key-here'
app.config['JWT_SECRET_KEY'] = SECRET_KEY

# Initialize JWT manager
jwt = JWTManager(app)

# User data structure with hashed passwords, username, and role
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("user1"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("admin1"),
        "role": "admin"
    }
}


# Custom error handlers
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


# Basic authentication route (/basic-protected)
@app.route('/basic-protected', methods=['GET'])
def basic_auth_protected():
    # Implement basic authentication logic here if needed
    # For this example, we'll only return a message when credentials are valid
    return jsonify({"message": "Basic Auth: Access Granted"})


# JWT-based login route (/login)
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if user exists and password is correct
    if username not in users or not /
    generate_password_hash(password) == users[username]['password']:
        return jsonify({"error": "Invalid credentials"}), 401

    # Generate JWT token for user
    payload = {
        'exp': dt.datetime.utcnow() + dt.timedelta(days=1),
        'sub': users[username]['username'],
        'iat': dt.datetime.utcnow(),
        'role': users[username]['role']
    }

    tokens = jwt.encode(payload, SECRET_KEY, lazy=False)
    access_token = tokens.decode('utf-8')

    return jsonify({"access_token": access_token})


# JWT authentication protected routes
@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_auth_protected():
    # Check if token is valid and present in headers
    if 'access_token' not in request.headers:
        return handle_unauthorized_error(request)

    # Retrieve user information from token
    user = get_jwt_identity()

    # Return a message indicating successful access
    return jsonify({"message": "JWT Auth: Access Granted"})


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    user = get_jwt_identity()

    if user['role'] != 'admin':
        return handle_unauthorized_error(request)

    # Return a message indicating access granted to admin users
    return jsonify({"message": "Admin Access: Granted"})


# Error handling decorators for custom error handlers
def auth_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'access_token' not in request.headers:
            return handle_unauthorized_error(request)
        return f(*args, **kwargs)

    return wrapper


# Example usage of a custom error handler
@app.route('/invalid-token', methods=['POST'])
@auth_required
def invalid_token():
    # Return an error response if token is expired or invalid
    return jsonify({"error": "Token is expired or invalid"}), 401


if __name__ == '__main__':
    app.run(debug=True)
