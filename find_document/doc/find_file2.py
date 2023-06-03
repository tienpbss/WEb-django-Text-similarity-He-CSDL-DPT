from sklearn.metrics.pairwise import cosine_similarity

from pymongo import MongoClient
import pickle
import os

# MONGO_URL = 'mongodb+srv://tien:123456Aa@cluster0.l9o94oo.mongodb.net/test?retryWrites=true&w=majority'
MONGO_LOCAL = 'mongodb://localhost:27017'
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))


client = MongoClient(MONGO_LOCAL)
database = client['documentCSDLDPT']
collection = database['docFeature']

tfidfvec_path = os.path.join(SITE_ROOT, 'pickle', 'tfidfvec.pickle')

with open(tfidfvec_path, 'rb') as file :
    tfidfvec = pickle.load(file)



def find_similarity2(text):
    text_to_vec = tfidfvec.transform([text])
    allDocs = list(collection.find())
    for i in allDocs:
        score = cosine_similarity(text_to_vec, pickle.loads(i['vector']))[0][0]
        i['score'] = round(score, 2)
    allDocs.sort(reverse=True, key=lambda x: x['score'])
    res = allDocs[0:5]
    return res
