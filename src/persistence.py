import pymongo

class MongoPersistence(object):
    def __init__(self):
        self.connection = pymongo.connection.Connection()
        self.db = self.connection.underpants
        self.entries = self.db.entries
        self.create_indexes()

    def create_indexes(self):
        self.entries.create_index("calaised", pymongo.ASCENDING)
        self.entries.create_index("published", pymongo.ASCENDING)
        self.entries.create_index("updated", pymongo.ASCENDING)

    def add(self, obj):
        print "Saving entry...."
        self.db.entries.save(obj)

    def find(conditions):
        pass

