from pymongo.connection import Connection
from twitter import Api
from time import sleep
api = Api()

connection = Connection("localhost", 27017)

db = connection.twitter
collection = db.public_feed

while True:
	for s in api.GetPublicTimeline():
		doc = {"_id": str(s.id), "source": "twitter", "user": s.user.screen_name, "text": s.text}
		collection.insert(doc)
	sleep(5)

print collection.find_one()


