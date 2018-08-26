#Default config
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = False
    SECRET_KEY = "xb1xc3xb9xf1xc4xf3x94xf8xe3xb4x14xa1xdbx1axb9fx1dx8bxb9Oxd1xe7x9aPxd7xbbxe5"
    DEVELOPMENT = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    DEVELOPMENT = True

class ProductionConfig(BaseConfig):
    DEBUG = False
