from flask import Flask
from flask_migrate import Migrate
from db_setup import db


def create_app(config_file):
    app = Flask(__name__)
    app.config.from_object(config_file)
    migrate = Migrate(app, db)
    db.init_app(app)
    return app