from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from nltk import sent_tokenize
from nltk.corpus import stopwords

def tldr(text_to_summarize):
    sentence_tokens = np.array(sent_tokenize(text_to_summarize))
    vectorizer = TfidfVectorizer(stop_words=set(stopwords.words("english")))
    sent_scores = np.array(vectorizer.fit_transform(sentence_tokens).sum(axis=1)).squeeze()
    return ''.join(sentence_tokens[np.where(sent_scores > 3)])
    
