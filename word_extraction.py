from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import nltk.data
import numpy as np
import pandas as pd


vectorizer = TfidfVectorizer(stop_words='english')
vectors = vectorizer.fit_transform(movie_con['whole_con']).toarray()
words = vectorizer.get_feature_names()

def get_important_words(lst, n, doc):
        '''
        INPUT: LIST, INTEGER, LIST
        OUTPUT: LIST

        Given a list of values, find the indices with the highest n values.
        Return the words for each of these indices.

        '''
        return [doc[i] for i in np.argsort(lst)[-1:-n-1:-1]]
