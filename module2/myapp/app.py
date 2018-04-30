from flask import Flask

from myapp.blueprints.page import page
def create_app():
    """
    Create a Flask Application using the app factory pattern

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)  
    ## True tells flask to look for an instance module at the same directory depth as the main module, which is myapp dir

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)
    ## True tells flask not to crash if that file does not exist

    app.register_blueprint(page)
    
    return app
    