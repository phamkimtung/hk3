# config.py
import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:02032005@localhost:5432/web'    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:02032005@localhost:5432/postgres'

    SECRET_KEY = os.urandom(24)  # Khóa bí mật cho JWT
