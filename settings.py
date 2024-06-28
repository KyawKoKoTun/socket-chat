from flask import Config
from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB')
    SECRET_KEY = os.environ.get('SECRET')
    SESSION_TYPE = 'filesystem'
