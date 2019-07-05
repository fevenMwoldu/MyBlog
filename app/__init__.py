from flask import Flask
from flask import Blueprint

# Initializing application
app = Flask(__name__) 

def create_app():

    # Registering the blueprint

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app