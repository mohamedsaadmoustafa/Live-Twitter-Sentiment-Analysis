import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import emoji

# read smileys_df
smileys_df = pd.read_csv("./data/smileys.csv")


def replace_emoji(text):
    # replace emojis by their corresponding text
    text = emoji.demojize(text, delimiters=("", ""))
    # replace smileys by their corresponding text
    new_text = ""
    for w in text.split():
        if w.upper() in smileys_df.smiley:
            new_text = new_text + smileys_df.meaning[smileys_df.smiley == w.upper()].values[0] + " "
        else:
            new_text = new_text + w + " "
    return new_text
