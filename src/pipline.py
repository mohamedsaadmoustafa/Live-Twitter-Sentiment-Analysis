import sys

sys.path.insert(0, 'preprocessing')

from remove_url import *
from remove_handle import *
from remove_rt import *
from replace_emoji import *
from remove_html import *
from remove_punc import *
from chatwords_conversion import *
from remove_whitespace import *
from stemming import *
from lemmatizing import *


def clean_text(tweet, normalize=None):
    tweet = tweet.lower()
    tweet = word_tokenizer(tweet)
    tweet = remove_handle(tweet)
    tweet = remove_rt(tweet)
    tweet = remove_url(tweet)
    tweet = remove_html(tweet)
    # tweet = remove_non_ascii(tweet)
    # tweet = correct_sentence_spelling(tweet)
    tweet = replace_emoji(tweet)
    tweet = remove_punc(tweet)
    #tweet = convert_chat_words(tweet)
    #tweet = remove_whitespace(tweet)

    if normalize == 'lemmatize':
        tweet = do_lemmatizing(tweet)
    elif normalize == 'stem':
        tweet = do_stemming(tweet)
    else:
        pass

    # if empty tweet
    if not tweet:
        tweet = ' '

    return tweet
