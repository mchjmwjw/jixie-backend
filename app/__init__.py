from flask import Flask
from flask_json import FlaskJSON
from flask_cors import *

def create_app():
    app = Flask(__name__)
    json = FlaskJSON(app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    from .api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')

    return app
