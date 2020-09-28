import os
from settings import dot_env_values
basedir = os.path.abspath(os.path.dirname(__file__))
user = dot_env_values['user']
password = dot_env_values['password']
db_name = dot_env_values['db_name']


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@localhost/{}'\
        .format(user, password, db_name)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
