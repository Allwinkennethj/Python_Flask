from flask import jsonify

def success_response(message="Success",status_code=200):
    response={
        "message":message,
        "status_code":status_code
    }
    return jsonify(response),status_code

def failure_response(message="Failure",status_code=500):
    response = {
        "message": message,
        "status_code": status_code
    }
    return jsonify(response), status_code
