import pymongo

class MongoPersistence(object):
    def __init__(self):
        # localhost connection
        self.connection = pymongo.connection.Connection()
        self.db = self.connection.underpants
        self.entries = self.db.entries
        self.create_indexes()

    def create_indexes(self):
        self.entries.create_index("calaised", pymongo.ASCENDING)
        self.entries.create_index("published", pymongo.ASCENDING)
        self.entries.create_index("updated", pymongo.ASCENDING)

    def add(self, obj):
        self.db.entries.save(obj)

    def find(self, conditions):
        return self.db.entries.find(conditions)

    def get_non_calaised_entries(self):
        return self.find({"calaised": None})

