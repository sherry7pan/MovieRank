#load libraries
from collections import Counter,defaultdict
import numpy as np
import nltk
import string
from nltk.util import ngrams


class Nthgram(object):
    """
    Takes a series from a DataFrame and an n and trains a model of a given n.
    Parameters
    ----------
    ngram: int
        Size of the words to look at.
    frequencies : dict of dicts, optional
        Contains frequencies if the models is being instantiated from other files.
    """
    
    def __init__(self, ngram, corpus):
        self.corpus = corpus
        self.ngram = ngram
        self.frequency = None
        self.total_word = 0

    def get_count(self):
        """
        Create a dictionary of Counter() with the n-gram as key and the count of that occuring as value
        """
        ctn= Counter()
        for conversation in self.corpus:
            ctn.update(ngrams(conversation.split(" "), self.ngram))
        return ctn

    def get_frequency(self):
        """
        Create a frequency dictionary with the n-gram as outer key,the word following the n-gram as inner key and 
        the value as the count of occurence of inner key following the outer n-gram.
        """
        ctn = self.get_count()
        if self.ngram == 1:
            self.frequency = defaultdict(dict)
            self.total_word = float(sum(ctn.values()))
            for key, value in ctn.iteritems():
                self.frequency[key] = value/self.total_word
        else:
            if self.ngram == 2:
                self.frequency = defaultdict(dict)
                for key, value in ctn.iteritems():
                    o_key = key[:-1][0]
                    i_key = key[-1]
                    self.frequency[o_key][i_key] = value
            else:
                for key,value in ctn.iteritems():
                    o_key = key[:-1]
                    i_key = key[-1]
                    self.frequency[o_key][i_key]=value

            for key_outer in self.frequency.iterkeys():    
                inner_dict = self.frequency[key_outer]
                total_count = sum(inner_dict.values())
                for key_inner , value_inner in inner_dict.iteritems():
                    self.frequency[key_outer][key_inner]= value_inner/float(total_count)

   
    def prob_next_single_model(self,next_one,given):
        """
        return the frequency count of a specific word sequence.
        """
        if not self.frequency.get(given):
            return 1e-10
        elif not self.frequency[given].get(next_one):
            return 1e-10
        else:
            return self.frequency[given][next_one]

    def predict_perplexity(self,doc):
        """
        returns the perplexity of a given document that is being normalized with its document length.
        """
        doc_lst = doc.split()
        prob_sum = 0
        for iter in xrange(self.ngram-1,len(doc_lst)):
            prob_sum += np.log(self.prob_next_single_model(doc_lst[iter],tuple(doc_lst[iter-self.ngram:iter]))+ 1e-10)
        return np.abs(prob_sum/float(len(doc_lst)))
