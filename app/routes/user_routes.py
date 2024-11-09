from flask import Blueprint, request, jsonify
from app.services.user_service import create_user, get_user, update_user, delete_user, get_all_users

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/', methods=['GET'])
def list_users():
    users = get_all_users()
    return jsonify(users), 200


@user_bp.route('/<user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = get_user(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(user), 200


@user_bp.route('/', methods=['POST'])
def create_new_user():
    data = request.get_json()
    user = create_user(data)
    if 'error' in user:
        return jsonify(user), 400
    return jsonify(user), 201


@user_bp.route('/<user_id>', methods=['PUT'])
def update_user_info(user_id):
    data = request.get_json()
    updated_user = update_user(user_id, data)
    if not updated_user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(updated_user), 200


@user_bp.route('/<user_id>', methods=['DELETE'])
def delete_user_account(user_id):
    result = delete_user(user_id)
    if not result:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'message': 'User deleted'}), 200
