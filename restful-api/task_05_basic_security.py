#!/usr/bin/python3
"""API Security and Authentication Techniques"""

import json
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
import datetime as dt
from functools import wraps

# Generate a secure secret key (replace with a strong random string)
SECRET_KEY = 'your-secure-secret-key'

users = {
    "user1": {"username": "user1", "role": "user"},
    "admin1": {"username": "admin1", "role": "admin"}
}

app = Flask(__name__)
jwt = JWTManager(app)


# Custom decorators for JWT handling
def jwt_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'access_token' not in request.headers:
            return jsonify({"error": "Unauthorized"}), 401

        try:
            token = jwt.decode(request.headers.get('access_token'))
            current_user = get_jwt_identity()

            if not current_user or 'role' not in current_user:
                return jsonify({"error": "Unauthorized"}), 401
        except Exception as e:
            return jsonify({"error": str(e)}), 500

        return f(*args, **kwargs)
    return wrapper


def handle_unauthorized():
    return jsonify({"error": "Unauthorized"}), 401


def handle_invalid_token():
    return jsonify({"error": "Invalid token"}), 401


def handle_expired_token():
    return jsonify({"error": "Token expired"}), 401


def handle_revoked_token():
    return jsonify({"error": "Token revoked"}), 401


def handle_needs_fresh_token():
    return jsonify({"message": "Fresh token required"}), 401


@app.route('/api/login', methods=['POST'])
@jwt_required
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return handle_unauthorized()

    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 401

    # Assuming perfect match for this example
    if user['password'] == password:
        current_time = dt.datetime.utcnow()

        # Generate JWT with user info
        token = jwt.dumps({
            'access_token': generate_token(),
            'exp': current_time + dt.timedelta(hours=1),
            'identity': {
                'user_id': username,
                'role': user['role']
            }
        })

        return {"access_token": token.decode('UTF-8')}, 200

    else:
        return handle_unauthorized()
    # Return proper error response for invalid password


@app.route('/api/protected', methods=['GET'])
@jwt_required
def protected():
    user_data = get_jwt_identity()

    if not user_data or 'role' not in user_data:
        return handle_unauthorized()

    role = user_data['role']

    # Example action specific to your application here

    return jsonify({"status": f"Protected Resource - Role: {role}"}), 200


@app.route('/api/token-refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh_token():
    if 'refresh_token' not in request.headers:
        return handle_unauthorized()

    try:
        token = jwt.decode(
            getattr(request, 'headers', {}).get('refresh_token')
        )
        new_token = jwt.dumps({
            'access_token': generate_token(),
            'exp': dt.utcnow() + dt.timedelta(hours=1),
            'identity': {
                'user_id': username,
                'role': user['role']
            }
        })

        return {"access_token": new_token.decode('UTF-8')}, 200
    except Exception as e:
        return handle_unauthorized(), 500
