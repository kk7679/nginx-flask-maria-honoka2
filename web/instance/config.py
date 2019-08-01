import os

DB_USER = 'adminuser'
DB_PASS = 'zaq1xsw2'
DB_HOST = 'db'
DB_NAME = 'sample01'
db_uri = "mysql+pymysql://{0}:{1}@{2}/{3}?charset=utf8".format(DB_USER, DB_PASS, DB_HOST, DB_NAME)

SQLALCHEMY_DATABASE_URI = db_uri
DEBUG = True
SECRET_KEY = os.urandom(24)