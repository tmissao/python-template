import os
from distutils.util import strtobool


class Config:
    FLASK_DEBUG = bool(strtobool(os.environ.get('FLASK_DEBUG', False)))
    FLASK_PORT = os.environ.get('FLASK_PORT', 5000)
    FLASK_HOST = os.environ.get('FLASK_HOST', "0.0.0.0")
