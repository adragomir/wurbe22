from pymongo.connection import Connection
import re

connection = Connection('localhost', 27017)

db = connection.twitter
collection = db.public_feed
mongo_users = db.users
mongo_hashtags = db.hashtags
mongo_replies = db.replies

def increment_hash(dictionary, collection, mongo, key):
    for h in collection:
        if dictionary.has_key(h):
            dictionary[h] = dictionary[h] + 1
        else:
            dictionary[h] = 1

        existing_h = mongo.find({key: h})
        exists = None
        try:
            exists = existing_h.next()
        except Exception:
            pass
        
        if exists is not None:
            exists['count'] = exists['count'] + 1
            mongo.save(exists)
        else:
            mongo.save({key: h, 'count': 1})


hashtags = {}
users = {}
for twit in collection.find({'proceessed': None}):
    text = twit['text']
    twit['proceessed'] = 2
    replies = re.findall('\@[a-zA-Z0-9\_]+', text)
    ht = re.findall('\#[a-zA-Z0-9\_]+', text)
    
    increment_hash(hashtags, ht, mongo_hashtags, 'hashtag')
    increment_hash(users, [twit['user']], mongo_users, 'user')


    if len(replies) > 0:
        print '------------------------------------------------------------'
        print text
        print '@%s replied to ' % twit['user']
        for r in replies:
            print '\t %s:' % r
            mongo_replies.save({'user':twit['user'], 'replied_to':r[1:]})
            msgs = collection.find({'user': r[1:]})
            for m in msgs:
                print '\t\t:\n\t\t\t\t %s' % (m['text'] )
    collection.save(twit)

print 'hashtags: \n%s'
for tag in sorted(hashtags.iteritems(), key=lambda (k,v):(v,k), reverse=True):
    if tag[1] > 1:
        print tag


for user in sorted(users.iteritems(), key=lambda (k,v):(v,k), reverse=True):
    if user[1] > 1:
        print user



