import sys
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from get_tweets import *
from pipline import *
from sentiment_analysis import *
from sentiment_pie import *
from top_tweet_bigrams import *
from word_cloud import *

sys.path.insert(0, 'Visualization')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('Live Twitter Sentiment Analysis')
st.image('./images/cover.png')

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')


def run():
    with st.form(key='Enter name'):
        search_words = st.text_input(
            label='Enter a topic for the sentiment',
            value="Arsenal",
        )
        number_of_tweets = st.slider(
            'Enter the number of latest tweets for the sentiment(Maximum 5000 tweets)',
            min_value=10,
            max_value=5000,
            value=10
        )
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        # Create a text element and let the reader know the data is loading.
        data_load_state = st.info('Loading data...')

        returned_df = get_tweets(
            topic=search_words,
            count=number_of_tweets,
            save=False
        )
        returned_df["clean_tweet"] = returned_df.Tweet.apply(lambda tweet: clean_text(tweet))
        returned_df = sentiment_analysis(returned_df, 'clean_tweet')

        if not returned_df.empty:
            st.write(returned_df)
            data_load_state.success('Data is ready!')
            # Convert results to download
            csv = convert_df(returned_df)
            # Notify the reader that the data was successfully loaded.
            st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name='large_df.csv',
                mime='text/csv',
            )
            # plots
            st.pyplot(get_top_tweet_bigrams(returned_df, column_name="clean_tweet", ngram=2, n=10))
            st.pyplot(word_cloud(returned_df, column_name="clean_tweet"))
            st.pyplot(sentiment_pie(returned_df))


if __name__ == '__main__':
    run()
