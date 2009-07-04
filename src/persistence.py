import pymongo

class MongoPersistence(Persistence):
    def __init__(self):
        self.connection = pymongo.connection.Connection()
        self.db = self.connections.underpants

