# visualization packages
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator


def word_cloud(df, column_name="Tweet"):
    # create instance of the WordCloud()
    word_cloud = WordCloud(height=1080, width=2048, background_color='white')

    # get the text in a big string
    txt = df[column_name].str.lower()
    text = " ".join([str(word) for word in txt])

    # generate the word cloud
    word_cloud.generate(text)

    # display now
    plt.figure(figsize=(14, 12));
    plt.imshow(word_cloud);
    plt.axis("off");
    plt.title(f"Most {column_name} Common Words");
