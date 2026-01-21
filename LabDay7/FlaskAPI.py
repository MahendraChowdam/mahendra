from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store
users = [
    {"id": 1, "name": "Mahendra", "email": "mahendra@gmail.com"},
    {"id": 2, "name": "Ravi", "email": "ravi@gmail.com"}
]

# ---------------------------
# GET /users -> Get all users
# ---------------------------
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200


# ------------------------------------
# GET /users/<id> -> Get user by ID
# ------------------------------------
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user['id'] == user_id:
            return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404


# ---------------------------
# POST /users -> Create user
# ---------------------------
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_user = {
        "id": users[-1]['id'] + 1 if users else 1,
        "name": data['name'],
        "email": data['email']
    }

    users.append(new_user)
    return jsonify(new_user), 201


# ---------------------------
# Run the Flask app
# ---------------------------
if __name__ == '__main__':
    app.run(debug=True)
