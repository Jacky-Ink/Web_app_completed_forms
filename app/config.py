from pathlib import Path


class Config(object):
    DEBUG = True
    BASE_DIR = str(Path.cwd())
    HOST = "0.0.0.0"
    PORT = "5000"
    SERVER_NAME = f'{HOST}:{PORT}'
    MONGODB_SETTINGS = {
        'db': 'form_validator',
        'host': 'form_validator_mongodb',
        'port': 27017,
        'collections_dir': Path(BASE_DIR) / 'db' / 'collections'
    }
