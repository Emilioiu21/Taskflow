from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Base de datos en memoria
users = [
    {"id": 1, "name": "Admin"},
    {"id": 2, "name": "Juan"},
]
next_id = 3


@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "message": "TaskFlow API v1.0"}), 200


@app.route('/api/users', methods=['GET'])
def list_users():
    return jsonify(users), 200


@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for u in users:
        if u['id'] == user_id:
            return jsonify(u), 200
    return jsonify({"error": "User not found"}), 404


@app.route('/api/users', methods=['POST'])
def create_user():
    global next_id
    data = request.get_json(force=True)
    name = data.get('name') if isinstance(data, dict) else None
    if not name:
        return jsonify({"error": "Field 'name' is required"}), 400
    user = {"id": next_id, "name": name}
    users.append(user)
    next_id += 1
    return jsonify(user), 201


@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json(force=True)
    for u in users:
        if u['id'] == user_id:
            name = data.get('name') if isinstance(data, dict) else None
            if name:
                u['name'] = name
            return jsonify(u), 200
    return jsonify({"error": "User not found"}), 404


@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    for u in users:
        if u['id'] == user_id:
            users = [x for x in users if x['id'] != user_id]
            return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
