from flask import Flask
from flask import Blueprint

from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

# Initializing application
app = Flask(__name__) 

def create_app():

    bootstrap.init_app(app)

    # Registering the blueprint

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app