"""
Sucks in data from social services. Currently FF implemented and dumps it into a persistence layer
"""
class Ingester(object):
    def __init__(self, persistence):
        self.persistence = persistence

    def ingest(self, items):
        for item in items:
            self.persistence.add(item)
