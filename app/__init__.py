from flask import Flask
from flask_json import FlaskJSON
from flask_cors import *
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    json = FlaskJSON(app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)

    from .api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')

    return app
