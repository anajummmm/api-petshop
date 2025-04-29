from flask import Blueprint, jsonify
from config.jwt_config import generate_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():
    token = generate_token()
    return jsonify({'token': token})
