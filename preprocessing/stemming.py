# nltk
import nltk
from nltk.stem.snowball import SnowballStemmer
from word_tokenizer import word_tokenizer

nltk.download('punkt')
nltk.download('omw-1.4')
nltk.download('wordnet')
nltk.download('stopwords')


def do_stemming(text):
    # Create instance of a PorterStemmer
    # stemmer = PorterStemmer()
    stemmer = SnowballStemmer(language='english')
    new_str = ""
    for word in text.split():
        tokenizer = word_tokenizer(word)
        new_str = new_str + stemmer.stem(tokenizer) + " "
    return new_str
