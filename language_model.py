from Nthgram import Nthgram
import math
import numpy as np



class Language_model(object):

    def __init__(self,corpus,unigram_w =0.05,bigram_w=0.25,trigram_w=0.5,fourthgram_w=0.2):
        self.unigram_w = unigram_w
        self.bigram_w = bigram_w
        self.trigram_w = trigram_w
        self.fourthgram_w = fourthgram_w

        self.unigram = Nthgram(1, corpus)
        self.bigram = Nthgram(2, corpus)
        self.trigram = Nthgram(3, corpus)
        self.fourthgram = Nthgram(4,corpus)

    def fit(self):
        self.unigram.get_frequency()
        self.bigram.get_frequency()
        self.trigram.get_frequency()
        self.fourthgram.get_frequency()


    # def get_optimal_weight(self, corpus):
    #     unigram_weights = np.linspace(0.1,0.5, num=5)
    #     bigram_weights = np.linspace(0.1,0.7, num=7)
    #     trigram_weights = np.linspace(0.1,0.9, num=9)
    #
    #     result=[]
    #     for weight1 in unigram_weights:
    #         for weight2 in bigram_weights:
    #             for weight3 in trigram_weights:
    #                     cur_weight = [weight1,weight2,weight3,max(0,1-weight1-weight2-weight3)]
    #                     total_weight = np.sum(cur_weight)
    #                     # import pdb; pdb.set_trace()
    #                     if total_weight == 1 :
    #                             prob_sum=0
    #                             for document in corpus:
    #                                 doc_lst = document.split()
    #                                 # prob_sum += math.log(self.unigram.prob_next_ensemble(doc_lst[0]))
    #                                 # if self.bigram.prob_next_ensemble(doc_lst[1],doc_lst[0]) != 0:
    #                                 #     prob_sum += math.log(self.bigram.prob_next_ensemble(doc_lst[1],doc_lst[0]))
    #                                 for iter in xrange(2, len(doc_lst)):
    #                                     part_1 = self.unigram.prob_next_ensemble(doc_lst[iter])
    #                                     part_2 = self.bigram.prob_next_ensemble(doc_lst[iter],doc_lst[iter-1])
    #                                     part_3 = self.trigram.prob_next_ensemble(doc_lst[iter],tuple(doc_lst[iter-2:iter]))
    #                                     part_4 = self.fourthgram.prob_next_ensemble(doc_lst[iter],tuple(doc_lst[iter-3:iter]))
    #
    #                                     prob_sum += math.log(cur_weight[0]*part_1 + cur_weight[1]*part_2 + cur_weight[2] * part_3 + cur_weight[3] * part_4)
    #                             report=tuple()
    #                             report = (prob_sum,cur_weight)
    #                             result.append(report)
    #
    #     result.sort(key=lambda x: x[0])
    #     print result
    #     self.unigram_w= result[-1][1][0]
    #     self.bigram_w= result[-1][1][1]
    #     self.triram_w= result[-1][1][2]
    #     self.fourthgram_w= result[-1][1][3]

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



    # def perdict_perplexity(self, doc):
    #
    #     for document in corpus:
    #         pass
            # iter = 0
            # word_doc = document.split()
            # prob.append()
            # iter +=1
            # prob.append(unigram_w * unigram.prob_next(word_doc[iter] + bigram_w * bigram.prob_next(word_doc[iter],word_doc[iter-1])










# doc_bodies = con['doc']
# vectorizer = TfidfVectorizer(max_features=100, stop_words='english')
# document_term_mat = vectorizer.fit_transform(doc_bodies)
# feature_words = vectorizer.get_feature_names()
