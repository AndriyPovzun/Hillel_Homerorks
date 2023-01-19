import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')

data_base = client['shoes']
my_collection = data_base['shoes']
