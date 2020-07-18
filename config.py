import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object) :
    
    HOST = "us-cdbr-east-05.cleardb.net"
    DATABASE = "heroku_bdbde6549454283"
    USERNAME = "bf09fdcd61c909"
    PASSWORD = "85a775f5"

    # HOST = "localhost"
    # DATABASE = "fake_tweet"
    # USERNAME = "root"
    # PASSWORD = ""

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DATABASE
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True