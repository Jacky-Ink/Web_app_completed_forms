from flask import request
from app import app
from form_validator.validator import Validator
from db.db import MongoDB
from app.config import Config


@app.post('/get_form')
def get_form():
    db = Config.MONGODB_SETTINGS['db']
    request_data = request.json
    db_data = MongoDB(db).get_db_collection('forms').find()
    validator = Validator(request_data, db_data)
    return validator.validate()
