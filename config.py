#config.py

# inbuilt imports
import os

class Config():
    '''
    global configuration class
    '''

    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    '''
    development environment configs
    '''

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

class TestingConfig(Config):
    '''
    testing environment configs
    '''

    TESTING = True

class ProductionConfig(Config):
    '''
    production environment configs
    '''

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}