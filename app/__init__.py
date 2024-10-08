import os
import logging
from flask import Flask, render_template
from flask.logging import default_handler
from logging.handlers import RotatingFileHandler
from jinja2 import ChoiceLoader, FileSystemLoader

def create_app():
    app = Flask(__name__)

    # Configure Flask App Instance
    CONFIG_TYPE = os.getenv('CONFIG_TYPE', default='config.DevelopementConfig')
    app.config.from_object(CONFIG_TYPE)

    # Register blueprints
    register_blueprints(app)
    
    # Initialize flask extension objects
    initialize_extensions(app)
    
    # Configure logging
    configure_logging(app)
    
    # Register error handlers
    register_error_handlers(app)
    
    # Overwrite Flask jinja_loader, using ChoiceLoader
    template_loader = ChoiceLoader([
        app.jinja_loader,
        FileSystemLoader('static'),
    ])

    return app

def register_blueprints(app):
    from app.about import about_bp
    from app.main import main_bp

    app.register_blueprint(about_bp, url_prefix='/about')
    app.register_blueprint(main_bp)


def initialize_extensions(app):
    pass

def register_error_handlers(app):
    pass

def configure_logging(app):
    # Deactivate the default flask logger so that log messages do not get duplicated
    app.logger.removeHandler(default_handler)
    
    # Create a file handler object
    file_handler = RotatingFileHandler('flaskapp.log', maxBytes=16384, backupCount=20)
    
    # Set logging level of file handler object so it logs INFO & up
    file_handler.setLevel(logging.INFO)
    
    # Create file formatter object
    file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(filename)s: %(lineno)d]')
    
    # Apply file formatter object to file handler
    file_handler.setFormatter(file_formatter)
    
    # Add file handler to logger
    app.logger.addHandler(file_handler)