import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
load_dotenv()

class Config():
    SQLALCHEMY_DATABASE_URI=os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS=os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
    JWT_SECRET_KEY=os.getenv("FLASK_JWT_SECRET_KEY")
    SECRET_KEY=os.getenv("FLASK_SECRET_KEY")

db=SQLAlchemy()
jwt=JWTManager()