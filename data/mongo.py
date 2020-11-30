from pymongo import MongoClient
import pandas as pd

class Mongo:

    def __init__(self):
        self.uri = "mongodb://localhost:27017/"

        self.client = MongoClient(self.uri)
        self.db = self.client.corgi4news

    def read_mongo(self, collection, no_id=True):
        """
        Reads all data from a Mongo collection 
        and stores into DataFrame
        """
        cursor = self.db[collection].find()
        df = pd.DataFrame(list(cursor))
        if no_id:
            del df['_id']
        return df