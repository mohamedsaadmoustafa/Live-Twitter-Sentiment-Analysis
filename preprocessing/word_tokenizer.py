import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('omw-1.4')
nltk.download('wordnet')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))


def word_tokenizer(text):
    """
    word tokenize
    remove non alpha
    remove stopwords (such as “the”, “a”, “an”, “in”)
    """
    words = [word for word in word_tokenize(text) if ((word not in stop_words) & (word.isalpha()) & (len(word) > 1))]
    # words = [word for word in word_tokenize(text) if((word.isalpha())&(len(word)>1))]
    return ' '.join(words)
