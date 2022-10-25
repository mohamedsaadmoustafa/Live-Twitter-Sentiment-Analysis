import numpy as np  # linear algebra
# visualization packages
import matplotlib.pyplot as plt
# scikit-learn
from sklearn.feature_extraction.text import CountVectorizer


def get_top_tweet_bigrams(df, column_name="Tweet", ngram=2, n=None):
    # select all text for selected dialect
    txt = df[column_name].str.lower()
    # create a matrix of token counts
    vec = CountVectorizer(ngram_range=(ngram, ngram)).fit(txt)
    # bag of words
    bag_of_words = vec.transform(txt)
    # sum bag of words
    sum_words = bag_of_words.sum(axis=0)
    # frequency of each word in selected texts
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
    # top n words repeates in selected texts
    top = words_freq[:n]
    # print(top)
    x, y = map(list, zip(*top))
    nn = np.arange(len(x))

    plt.barh(x, y, align='center', alpha=0.2)
    plt.plot(y, nn, '-o', markersize=5, alpha=0.8)
    plt.yticks(nn, x);
    plt.xlabel('Word Number');
    plt.title(f'Top {n} words in  tweets')
