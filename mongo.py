import os
import pymongo
if os.path.exists("env.py"):
	import env

MONGO_URI = os.environ.get("MONGO_URI")
DATABASE  = "recipes"
COLLECTION = "recipes"


def mongo_connect(url):
	try: 
		conn = pymongo.MongoClient(url)
		print("mongo is connected")
		return conn
	except pymongo.errors.ConnectionFailure as e: 
		print("Could not connect to MongodB: %s") % e

def create_item():
	first = input


def read_item():
	pass


def update_item():
	pass


def delete_item():
	pass


conn = mongo_connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]

print(coll)

items = coll.find()

for item in items: 
	print(item)