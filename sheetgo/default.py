import os
from distutils import util


class Config:
    DEBUG = util.strtobool(os.environ.get('DEBUG', 'True'))
    SECRET_KEY = os.environ.get('SECRET_KEY', 'z6Ct_d2Wy0ZcZZVUYD3beI5ZCSsFrR6-f3ZDyn_MW00')
