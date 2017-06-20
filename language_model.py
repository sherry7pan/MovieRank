#load libraries and classes
from Nthgram import Nthgram
import math
import itertools
import numpy as np



class Language_model(object):
    """
    Takes in four different nthgram classes and instantiates an ensemble language model class.
    Finding optimal weights using grid search approach.
    """
   
    def __init__(self,corpus,grid_weights=None):
       
        s
        self.unigram = Nthgram(1, corpus)
        self.bigram = Nthgram(2, corpus)
        self.trigram = Nthgram(3, corpus)
        self.fourthgram = Nthgram(4,corpus)

    def fit(self):
        """ 
        traning the submodels to get frequency dictionaries.
        """
        self.unigram.get_frequency()
        self.bigram.get_frequency()
        self.trigram.get_frequency()
        self.fourthgram.get_frequency()
        
    def create_grid_weights(self):
        """
        create the list of different weight combination for grid searching.
        """
        lst_weights_comb = np.linesplace(0,1,10)
        for ele in iterpools.product(lst_weights_comb, repeat = 3):
            if sum(ele) <=1:
                last_weight = 1 - sum(ele)
                temp= list(ele)
                temp.append(last_weight)
                self.grid_weights.append(tuple(temp)

    def get_optimal_weight(self, corpus):
        """
        Takes the list of possible weight combination and give back the best performeing weight 
        combination for the language model
        """
                                         

    def predict_perplexity(self,movie):
        doc_lst = movie.split()
        prob_sum = 0
        for iter in xrange(3, len(doc_lst)):
            part_1 = self.unigram.prob_next_ensemble(doc_lst[iter])
            part_2 = self.bigram.prob_next_ensemble(doc_lst[iter],doc_lst[iter-1])
            part_3 = self.trigram.prob_next_ensemble(doc_lst[iter],tuple(doc_lst[iter-2:iter]))
            part_4 = self.fourthgram.prob_next_ensemble(doc_lst[iter],tuple(doc_lst[iter-3:iter]))
            prob_sum += math.log(self.unigram_w * part_1 + self.bigram_w * part_2 + self.trigram_w * part_3 + self.fourthgram_w * part_4)
        return np.abs(prob_sum/float(len(doc_lst)))



