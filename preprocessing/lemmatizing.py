# nltk
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from word_tokenizer import word_tokenizer

nltk.download('punkt')
nltk.download('omw-1.4')
nltk.download('wordnet')


def do_lemmatizing(text):
    # Create instance of a PorterStemmer
    word_lemmatizer = WordNetLemmatizer()
    new_str = ""
    for word in text.split():
        tokenizer = word_tokenizer(word)
        new_str = new_str + word_lemmatizer.lemmatize(tokenizer) + " "
    return new_str
