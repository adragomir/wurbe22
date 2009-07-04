class FriendFeedInput(object):
    def __init__(self):
        self.data = []
        self.current = 0

    def massage(self, obj):
        return obj

    def next(self):
        if self.current == len(self.data):
            raise StopIteration
        else:
            to_ret = self.massage(self.data[self.current])
            self.current += 1
            return to_ret

    def __getitem__(self, item):
        return self.massage(self.l[item])

    def __iter__(self):
        return self
