#!/usr/bin/python3
"""API Security and Authentication Techniques"""

from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
import datetime

app = Flask(__name__)

# Configure JWT
app.config['JWT_SECRET_KEY'] = 'super-secret-key-change-in-production'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(hours=1)
jwt = JWTManager(app)

# Setup basic auth
auth = HTTPBasicAuth()

# User database with hashed passwords
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# Basic auth verification function
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(
        users[username]['password'], password
    ):
        return username
    return None


# Basic auth error handler
@auth.error_handler
def auth_error():
    return jsonify({"error": "Unauthorized access"}), 401


# JWT error handlers - providing correct parameter signatures
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


# Routes
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"})


@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    data = request.get_json()
    username = data.get('username', None)
    password = data.get('password', None)

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    if username not in users or not check_password_hash(
        users[username]['password'], password
    ):
        return jsonify({"error": "Invalid credentials"}), 401

    # Create token with user info in the identity
    access_token = create_access_token(
        identity={
            "username": username,
            "role": users[username]['role']
        }
    )

    return jsonify({"access_token": access_token})


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    # The jwt_required decorator will handle the token validation
    # If it passes, we can proceed with the function
    return jsonify({"message": "JWT Auth: Access Granted"})


@app.route('/admin-only')
@jwt_required()
def admin_only():
    # Get the identity from the JWT token
    current_user = get_jwt_identity()

    # Check if the identity contains role information
    if isinstance(current_user, dict) and 'role' in current_user:
        role = current_user.get('role')
    else:
        # Handle the case where identity might not be structured as expected
        return jsonify({"error": "Invalid token format"}), 401

    # Check if the user has the admin role
    if role != 'admin':
        return jsonify({"error": "Admin access required"}), 403

    return jsonify({"message": "Admin Access: Granted"})


if __name__ == '__main__':
    app.run(debug=True)
