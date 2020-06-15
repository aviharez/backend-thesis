import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object) :
    HOST = "remotemysql.com"
    DATABASE = "CIvte6ww4R"
    USERNAME = "CIvte6ww4R"
    PASSWORD = "qZLXwzRDvO"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DATABASE
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True