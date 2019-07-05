 import os

class Config:

    MOVIE_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/quotes.json'
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}