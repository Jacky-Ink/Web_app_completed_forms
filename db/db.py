from pathlib import Path
import json

from app.config import Config
import pymongo.collection
from pymongo import MongoClient


class MongoCollectionsDB:
    def __init__(self, collections_dir: Path) -> None:
        self.collections_dir = collections_dir
        collections = [c for c in self.collections_dir.iterdir() if c.suffix == '.json']
        self.collections = collections

    def __str__(self) -> str:
        return f'MongoCollectionsDB: {self.collections}'

    def __repr__(self) -> str:
        return f'MongoCollectionsDB: {self.collections}'


class MongoCollection:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.name = path.stem
        self.docs = self.get_docs()

    def __str__(self) -> str:
        return f'MongoCollection: {self.name}'

    def __repr__(self) -> str:
        return f'MongoCollection: {self.name}'

    def get_docs(self) -> json:
        with open(self.path, 'r', encoding='utf-8') as f:
            docs = json.load(f)
        return docs


class MongoDB(object):

    def __init__(self, db: str) -> None:
        self.db = db
        self.conn = self.get_connection()

    def __str__(self) -> str:
        return f'MongoDB: {self.db}'

    def __repr__(self) -> str:
        return f'MongoDB: {self.db}'

    @staticmethod
    def get_connection() -> MongoClient:
        mongo_host = Config.MONGODB_SETTINGS['host']
        mongo_port = Config.MONGODB_SETTINGS['port']
        return MongoClient(f'mongodb://{mongo_host}:{mongo_port}/')

    def get_db(self) -> MongoClient:
        return self.conn[self.db]

    def get_db_collection(self, collection: str) -> pymongo.collection.Collection:
        return self.get_db()[collection]

    def check_collections_exists(self, collections_obj: MongoCollection):
        return collections_obj.name in self.get_db().list_collection_names()

    def create_collection(self, collection_obj: MongoCollection):
        collection = self.get_db_collection(collection_obj.name)
        collection.insert_many(collection_obj.docs)

    def init_mongo(self):
        collections = MongoCollectionsDB(Config.MONGODB_SETTINGS['collections_dir']).collections
        collection_objs = [MongoCollection(c) for c in collections]

        for collection in collection_objs:
            if not self.check_collections_exists(collection):
                self.create_collection(collection)
