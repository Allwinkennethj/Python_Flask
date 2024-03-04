from flask import Flask
from flask_cors import CORS
from config import Config
from api.user.view import user
from api.admin.view import admin

def create_app():
    app=Flask(__name__)
    app.register_blueprint(user)
    app.register_blueprint(admin)
    app.config.from_object(Config)
    CORS(app,origin=True)
    return app