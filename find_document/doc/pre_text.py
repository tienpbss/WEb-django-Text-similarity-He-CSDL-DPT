import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

def remove_stopwords(text):
    '''Remove stop word'''
    stop_words = set(stopwords.words('english')) # Define the set of English stopwords
    words = nltk.word_tokenize(text) # Tokenize the input text
    filtered_words = [word for word in words if word.lower() not in stop_words] # Remove stopwords
    return ' '.join(filtered_words) # Join the filtered words into a string

def stem_words(text):
    '''convert to root word'''
    word_tokens = nltk.word_tokenize(text)
    stems = [stemmer.stem(word) for word in word_tokens]
    return ' '.join(stems)

def remove_urls(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return re.sub(url_pattern, '', text)

def clean_text(text):
    text = text.lower()
    text = remove_urls(text) # remove url
    # text = ''.join([i for i in text if not i.isdigit()]) #remove number
    text = re.sub(r'\d+', '', text) #remove number
    text = re.sub(r'[^\w\s]', '', text) # remove special character
    text = remove_stopwords(text) # remove stop word
    text = stem_words(text) #conver words to root words
    text = re.sub(r'_{2,}', '', text)
    text = text.encode('ascii', 'ignore').decode() #remove character not ascii
    return text