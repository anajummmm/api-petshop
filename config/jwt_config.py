import jwt
from flask import request, jsonify
from functools import wraps

SECRET_KEY = 'taylor swift'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')
        if not token:
            return jsonify({'message': 'token nao fornecido!'}), 401
        try:
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except:
            return jsonify({'message': 'token invalido!'}), 401
        return f(*args, **kwargs)
    return decorated

def generate_token():
    return jwt.encode({}, SECRET_KEY, algorithm="HS256")
