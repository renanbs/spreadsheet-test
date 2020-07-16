import os
from distutils import util


class Config:
    DEBUG = util.strtobool(os.environ.get('DEBUG', 'True'))
