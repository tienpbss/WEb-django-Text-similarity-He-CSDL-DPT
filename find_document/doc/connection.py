from pymongo import MongoClient


# MONGO_URL = 'mongodb+srv://tien:123456Aa@cluster0.l9o94oo.mongodb.net/test?retryWrites=true&w=majority'
MONGO_LOCAL = 'mongodb://localhost:27017'

client = MongoClient(MONGO_LOCAL)

