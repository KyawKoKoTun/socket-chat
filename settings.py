from flask import Config
from datetime import timedelta


class Settings(Config):
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db?check_same_thread=False'
    SQLALCHEMY_DATABASE_URI = 'postgresql://admin:aAdVsLOxWiICT3bu6H5yaLIpoK6miI3J@dpg-cg6sv5pmbg5ab7lu5470-a.oregon-postgres.render.com/socket_chat'
    SECRET_KEY = '740d9e58782809e59424751c9b5279af09e707febe831fec78ff1e2571f52b89'
    SESSION_TYPE = 'filesystem'
