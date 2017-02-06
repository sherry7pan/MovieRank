from collections import Counter,defaultdict
import numpy as np
import nltk
from nltk.util import ngrams

class Unigram(object):
    def __init__(self,):
        pass

class Nthgram(object):

    def __init__(self, ngram, corpus):
        self.corpus = corpus
        self.ngram = ngram
        self.frequency = defaultdict(dict)
        self.total_word = 0

    def get_count(self):
        ctn= Counter()
        for conversation in self.corpus:
            ctn.update(ngrams(conversation.split(" "), self.ngram))
        return ctn

    def get_frequency(self):

        ctn = self.get_count()
        if self.ngram == 1:
            self.total_word = float(sum(ctn.values()))
            for key, value in ctn.iteritems():
                self.frequency[key] = value/self.total_word
        else:
            if self.ngram == 2:
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
                    # import pdb; pdb.set_trace()
                inner_dict = self.frequency[key_outer]

                # import pdb; pdb.set_trace()
                total_count = sum(inner_dict.values())
                for key_inner , value_inner in inner_dict.iteritems():
                    self.frequency[key_outer][key_inner]= value_inner/float(total_count)

    def prob_next_ensemble(self,next_one,given=None):
        if self.ngram == 1:
            return self.frequency.get(next_one, 1/self.total_word)
        else:
            return self.frequency[given].get(next_one,0)


    def prob_next_single_model(self,next_one,given):
        if not self.frequency.get(given):
            return 0.0000000001
        elif not self.frequency[given].get(next_one):
            return 0.0000000001
        else:
            return self.frequency[given][next_one]

    def predict_perplexity(self,doc):
        doc_lst = doc.split()
        prob_sum = 0
        for iter in xrange(self.ngram-1,len(doc_lst)):
            prob_sum += np.log(self.prob_next_single_model(doc_lst[iter],tuple(doc_lst[iter-self.ngram:iter])))
        return np.abs(prob_sum/float(len(doc_lst)))
