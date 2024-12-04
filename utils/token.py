# utils/token.py
from flask_jwt_extended import create_access_token

def generate_access_token(identity):
    return create_access_token(identity=identity)
