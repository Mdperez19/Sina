from dotenv import load_dotenv
import pymongo
import os


class Dictionary:
    def __init__(self):
        if os.path.exists('.env'):
            load_dotenv()

        self.connection_string = os.environ.get("COSMOS_CONNECTION_STRING")
        self.db_name = os.environ.get("DB_NAME")
        self.collection_name = os.environ.get("COLLECTION_NAME")
        self.database = None

    def connect_to_database(self) -> None:
        client = pymongo.MongoClient(self.connection_string)
        self.database = client[self.db_name]

    def get_collection_from_database(self) -> pymongo.collection:
        collection = self.database[self.collection_name]

        return collection
