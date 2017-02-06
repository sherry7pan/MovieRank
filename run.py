import pandas as pd
import string
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from Nthgram import Nthgram
from Language_model import Language_model
from Cleaning import data_cleaning





if __name__ == '__main__':
    corpus, movie_df = data_cleaning()
    U = Nthgram(1,corpus)
    c = U.get_count()
    common = c.most_common(400)

    print common
    print '***'*10

    B = Nthgram(2,corpus)
    Bc = B.get_count()
    Bcommon = Bc.most_common(400)

    print Bcommon
    print '***'*10

    T = Nthgram(3,corpus)
    Tc = T.get_count()
    Tcommon = Tc.most_common(400)

    print Tcommon
    print '***'*10

    F = Nthgram(4,corpus)
    Fc = F.get_count()
    Fcommon = Fc.most_common(400)

    print Fcommon
    print '***'*10

    # Five = Nthgram(5,corpus)
    # Fivec = Five.get_count()
    # Fivecommon = Fivec.most_common(400)
    # print Fivecommon
    # print '***'*10
    #
    # Six = Nthgram(6,corpus)
    # Sixc = Six.get_count()
    # Sixcommon = Sixc.most_common(400)
    # print Sixcommon
    # print '***'*10
    #
    # Seven = Nthgram(7,corpus)
    # Sevenc = Seven.get_count()
    # Sevencommon = Sevenc.most_common(400)
    # print Sevencommon
    # print '***'*10
    #
    # Eight = Nthgram(8,corpus)
    # Eightc = Eight.get_count()
    # Eightcommon = Eightc.most_common(400)
    # print Eightcommon
    # print '***'*10
    # LM = Language_model(corpus)
    # LM.fit()
    # # lst = LM.get_optimal_weight(corpus)
    #
    # movie_score_lst = list()
    # for movie, movie_con in zip(movie_df['movie_name'], movie_df['whole_con']):
    #     score = LM.predict_perplexity(movie_con)
    #     t = [movie,score]
    #     # import pdb; pdb.set_trace()
    #     print t
    #     movie_score_lst.append(t)
    # movie_score_lst.sort(key=lambda x: x[1])
    # print movie_score_lst
