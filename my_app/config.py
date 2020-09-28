import os
basedir = os.path.abspath(os.path.dirname(__file__))
user='postgres'
password='1'
db_name='postgres'

class Config(object):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://{}:{}@localhost/{}'.format(user,password,db_name)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
