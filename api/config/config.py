import os
from decouple import config
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

import os
import re

url = config("DATABASE_URL") # config var
if url.startswith("postgres://"):
  url = url.replace("postgres://", "postgresql://", 1)
# rest of connection code using the connection string `url`

class Config:
  SECRET_KEY=config('SECRET_KEY', 'secret')
  JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
  JWT_REFRESH_TOKEN_EXPIRES = timedelta(minutes=30)
  JWT_SECRET_KEY = config('JWT_SECRET_KEY')
  
class DevConfig(Config):
  SQLALCHEMY_DATABASE_URL = "sqlite:///" + os.path.join(BASE_DIR,'db.sqlite3')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_ECHO = True
  DEBUG = True

class TestConfig(Config):
  TESTING = True
  SQLALCHEMY_DATABASE_URL = "sqlite://"
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_ECHO = True

class ProdConfig(Config):
  SQLALCHEMY_DATABASE_URL = url
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  DEBUG = config('DEBUG', cast = bool)

config_dict={
  'dev': DevConfig,
  'test': TestConfig,
  'prod': ProdConfig,
}
