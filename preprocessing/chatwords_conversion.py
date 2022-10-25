import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

# read chat words
chat_words = pd.read_csv("./data/chatwords.csv")


def convert_chat_words(text):
    new_text = ""
    abbrs = chat_words.abbreviation
    for w in text.split():
        if w.upper() in abbrs.tolist():
            new_text = new_text + chat_words.meaning[abbrs == w.upper()].values[0] + " "
        else:
            new_text = new_text + w + " "
    return new_text
