from flask import Flask

from . import app
from app.config import Config
from db.db import MongoDB
from form_validator import routes


def init_app() -> Flask:
    mongo = MongoDB(Config.MONGODB_SETTINGS['db'])
    mongo.init_mongo()
    app.config.from_object(Config)
    return app
