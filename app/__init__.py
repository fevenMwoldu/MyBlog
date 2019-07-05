from flask import Flask
from flask import Blueprint

from flask_bootstrap import Bootstrap
from .config import DevConfig

# Initializing application
app = Flask(__name__,instance_relative_config = True)

# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

bootstrap = Bootstrap()


def create_app():

    bootstrap.init_app(app)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Registering the blueprint

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app