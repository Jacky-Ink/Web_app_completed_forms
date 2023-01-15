from flask import Flask, request, Response
import json
from tinydb import TinyDB
import jsonschema


SCHEMA = {
        'type': 'object',
        'properties': {
            'date': {
                'type': 'string',
                'format': 'date',
                'pattern': '^[0-3]?[0-9]\\.[01]?[0-9]\\.(19)|(20)[0-9]{2}$'
            },
            'phone': {
                'type': 'string',
                'pattern': '^\\+7 [0-9]{3} [0-9]{3} [0-9]{2} [0-9]{2}$'
            },
            'email': {
                'type': 'string',
                'format': 'idn-email',
                'pattern': '^.+@.+\\..+$'
            },
            'text': {
                'type': 'string'
            }
        }
    }

db = TinyDB('db.json')
app = Flask(__name__)


def type_define(value):
    supported_types = ['date', 'phone', 'email', 'text']
    for t in supported_types:
        try:
            jsonschema.validate({t: value}, SCHEMA)
            return t
        except jsonschema.exceptions.ValidationError:
            continue
    return None


def to_json(data):
    return json.dumps(data) + "\n"


def resp(code, data):
    return Response(
        status=code,
        mimetype="application/json",
        response=to_json(data)
    )


@app.errorhandler(404)
def page_not_found(e):
    return resp(404, {})


@app.route('/get_form', methods=['POST'])
def post_themes():
    name = None
    data = db.all()
    for item in data:
        count = len(item) - 1
        for i in item:
            if i == 'name':
                continue
            if i in request.args:
                count -= 1
            else:
                break
        if count == 0:
            name = item['name']
            break
    if name is None:
        res = dict()
        for arg in request.args:
            value_type = type_define(request.args[arg])
            res[arg] = value_type
        return resp(200, res)
    else:
        return resp(200, name)


if __name__ == '__main__':
    app.debug = True
    app.run()
