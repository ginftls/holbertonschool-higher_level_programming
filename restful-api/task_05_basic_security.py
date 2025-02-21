#!/usr/bin/python3
'''API Security and Authentication Techniques'''
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity, jwt_required, JWTManager,
)

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


app = Flask(__name__)
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    """Verify the username and password against the stored user data."""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@app.route("/")
def home():
    """Return a welcome message."""
    return "Welcome to the Flask API!"


@app.route("/basic-protected", methods=['GET'])
@auth.login_required
def basic_protected():
    """Return a message if basic authentication is successful."""
    return "Basic Auth: Access Granted"


app.config["JWT_SECRET_KEY"] = "my_secret_key"
jwt = JWTManager(app)


@app.route("/login", methods=["POST"])
def login():
    """Authenticate user and return a JWT if successful."""
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400

    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Bad username or password"}), 401


@app.route("/jwt-protected", methods=['GET'])
@jwt_required()
def jwt_protected():
    """Return a message if JWT authentication is successful."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=['GET'])
@jwt_required()
def admin_only():
    """Return a message if the current user is an admin."""
    current_user = get_jwt_identity()

    if current_user not in users:
        return jsonify({"error": "User not found"}), 404

    if users[current_user]['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle unauthorized access attempts."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid token errors."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handle expired token errors."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handle revoked token errors."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handle cases where a fresh token is required."""
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run()
