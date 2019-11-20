import os
from flask import Flask
from config import app_config


def create_app(envi_name):
    app = Flask(__name__)
    app.config.from_object(app_config[envi_name])

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/modulelog')

    from resources.Model import db
    db.init_app(app)

    return app


env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)


