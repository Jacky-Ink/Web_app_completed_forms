import datetime
import re
from typing import Optional
from flask import jsonify
from pymongo.cursor import Cursor


class Validator:

    @classmethod
    def type_mapper(cls):
        return {
            'str': cls._validate_str,
            'date': cls._validate_date,
            'phone': cls._validate_phone,
            'email': cls._validate_email
        }

    @staticmethod
    def _validate_str(string: str) -> re.Match:
        return re.compile(r'^.+$').match(string)

    @staticmethod
    def _validate_date(string: str) -> Optional[datetime.datetime]:
        date = None
        try:
            date = datetime.datetime.strptime(string, '%d.%m.%Y')
        except ValueError:
            pass
        try:
            date = datetime.datetime.strptime(string, '%Y-%m-%d')
        except ValueError:
            pass
        return date

    @staticmethod
    def _validate_phone(string: str) -> re.Match:
        return re.compile(r'^\+7 [0-9]{3} [0-9]{3} [0-9]{2} [0-9]{2}$').match(string)

    @staticmethod
    def _validate_email(string: str) -> re.Match:
        return re.compile(r'^[a-zA-Z0-9-_]+@[a-zA-Z-]+.[a-zA-Z]+$').match(string)

    def __init__(self, request_data: dict, db_data: Cursor) -> None:
        """
        :param request_data: dict with requested fields and its values
        :param db_data: instance of pymongo Cursor: db.collection.find()
        """
        self.db_data = [data for data in db_data]
        self.request_data = request_data

    def __str__(self) -> str:
        return f'Validator: {self.request_data}'

    def __repr__(self) -> str:
        return f'Validator: {self.request_data}'

    def define_form(self) -> Optional[dict]:
        """
        compare form attrs and request data attrs and define form
        """
        for doc in self.db_data:
            doc_id, form = doc
            db_attrs = set(doc[form].keys())
            request_attrs = set(self.request_data.keys())
            if db_attrs & request_attrs == db_attrs:
                return {form: doc[form]}

    def validate(self) -> jsonify:
        """
        compares attrs values with expected attrs types and validate
        """
        form = self.define_form()
        if not form:
            return jsonify({'ValidationError': 'Form not found'}), 404
        form_name = next(iter(form))
        attrs = form[form_name]

        errors = {}

        for field, value in self.request_data.items():
            if field in attrs:
                field_type = attrs[field]
                validate = self.type_mapper()[field_type](value)
                if not validate:
                    errors.update({field: field_type})
        if errors:
            return jsonify(errors), 400

        return jsonify({'Form': form_name})
