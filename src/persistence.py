import pymongo

class MongoPersistence(object):
    def __init__(self):
        self.connection = pymongo.connection.Connection()
        self.db = self.connection.underpants

    def add(self, obj):
        print "adding"
        pass
        

