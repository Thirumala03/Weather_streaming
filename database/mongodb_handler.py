from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "weather_db"
COLLECTION_NAME = "weather_data"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def insert_to_mongodb(data):
    collection.insert_one({"weather_data": data})

def get_latest_data():
    return list(collection.find().sort("_id", -1).limit(10))
