# Movie Rank - A Movie Difficulty scorer for English learner


### Motivation
***
What's the most fun way to learn English?
If you're tired of going to classes or reading a book, there's noting better than learning English through movies.

By watching movies, learners will get to learn REAL English conversations in context but not textbook English. Moreover, they get to hear how things are said like the tone of voice.

However, selecting a movie that matches the learner's current English level is not always obvious. A wrong match may lead to a frustrating and dissatisfying experience.

The goal of this capstone project is to build a scorer that rates English movie difficulty and extracts the keywords using various natural language processing techniques.


### Data
***

The Movie Rank scorer was trained on the Cornell Movie-Dialogs Corpus which contains 220,579 conversational exchanges between 10,292 pairs of movie characters from 617 movies.


### Modelling
***
There are no one specific way to measure language difficulty. Important hints include frequency of the words in everyday usages, context within sentences, and words senses in sematics.

This scorer provides two scores as well as the keywords of the movie based on the converstaional exchanges from the dialogs corpus.

Note: the model was trained on the movie corpus and provides a relative score and ranking. It's possible that an English learn may still find the easiest movie in the system challanging. The bottom line is that if a learner has to pick a movie to learn English from, it would be beneficial to start with the movies that has the relatively most frequency words and phrases used in daily conversation.

1. vocabulary difficulty.
The vocabulary difficulty score is provided using the N-gram class with n=1. The unigram will return how frequent the words in a specific movie occurs in the whole movie-dialog corpus.

2. phrases/sentence difficulty.
This sentence difficulty score is provided using an ensemble language model class with several N-gram class and is optimized using iterative grid search approach.

3. keyword extractor.
The keyword exractor utilized the tfidfvectorizer to provide keywords but not common words like a, an, the, me, you etc. of the movie so learner might focus on studying these keywords beforehand to better follow alond the movie.



