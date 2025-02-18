from flask import Flask, jsonify, request, json


app = Flask(__name__)


users = {}


@app.route('/')
def home():
    """Return a welcome message for the API."""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_username():
    """Return a list of usernames."""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """Return the status of the API."""
    return "OK"


@app.route('/users/<username>')
def name(username):
    """Return user profile for the given username."""
    profile = users.get(username)
    if profile:
        return jsonify(profile)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user to the users dictionary."""
    user_data = request.get_json()
    username = user_data.get('username')

    if not username:
        return jsonify({"error": "Username is required"}), 400
    else:
        users[username] = user_data
        return jsonify({"message": "User added", "user": user_data}), 201


if __name__ == "__main__":
    app.run(debug=True)
