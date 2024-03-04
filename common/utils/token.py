from config import jwt
from flask import jsonify

@jwt.unauthorized_loader
def unauthorized_loader():
    return jsonify({
        "message":"Request Doesn't contain a valid token",
        "error":"Authorization Error"
    })

