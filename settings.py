from flask import Config
from datetime import timedelta


class Settings(Config):
    db_user = 'kagyinet_admin'
    db_password = '6PA7L7)1Q8}('
    host = '67.211.222.34'
    db_name = 'kagyinet_database'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db?check_same_thread=False'
    # SQLALCHEMY_DATABASE_URI = f'mysql+mysqldb://{db_user}:{db_password}@{host}/{db_name}'
    #SQLALCHEMY_DATABASE_URI = 'postgresql://xkedplapsyckuy:ec466b14127fb63ec29324edfc4a1a2381acffe8c813bd84ad2f20b3a1078387@ec2-54-172-175-251.compute-1.amazonaws.com:5432/d8godpaeugasej'
    SECRET_KEY = '740d9e58782809e59424751c9b5279af09e707febe831fec78ff1e2571f52b89'
    # SESSION_PERMANENT = True
    # PERMANENT_SESSION_LIFETIME = timedelta(days=31)
    SESSION_TYPE = 'filesystem'