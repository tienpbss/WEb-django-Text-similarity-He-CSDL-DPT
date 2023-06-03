import os
import pickle
from sklearn.metrics.pairwise import cosine_similarity


SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

listFilePath = os.path.join(SITE_ROOT, 'pickle', 'listFile.pickle')
tfidf_file_to_vec_path = os.path.join(SITE_ROOT, 'pickle', 'tfidf-file-to-vec.pickle')
tfidfvec_path = os.path.join(SITE_ROOT, 'pickle', 'tfidfvec.pickle')

with open(listFilePath, 'rb') as file :
    listFile = pickle.load(file)

with open(tfidfvec_path, 'rb') as file :
    tfidfvec = pickle.load(file)

with open(tfidf_file_to_vec_path, 'rb') as file :
    tfidf_file_to_vec = pickle.load(file)


def find_similarity(text):
    text_to_vec = tfidfvec.transform([text])
    similarity = cosine_similarity(text_to_vec, tfidf_file_to_vec)
    similar_indices = similarity.argsort()[0][::-1][:5]
    res = [{'name': listFile[i],'score': round(similarity[0][i], 2)} for i in similar_indices]
    return res


