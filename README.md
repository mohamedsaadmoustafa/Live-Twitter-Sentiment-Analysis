# Live Twitter Sentiment Analysis using Tweepy, HuggingFace Transformers and Streamlit

This app uses tweepy to get tweets from twitter based on the input name/phrase. It then processes the tweets through HuggingFace transformers pipeline function for sentiment analysis. The resulting sentiments and corresponding tweets are then put in a dataframe for display which is what you see as result.


## Generating access tokens
Login to your Twitter account on developer.twitter.com. Navigate to the Twitter app dashboard and open the Twitter app for which you would like to generate access tokens. Navigate to the "Keys and Tokens" page. Select 'Create' under the "Access token & access token secret" section.

[Using .env Files](https://pypi.org/project/python-dotenv/) for saving generated access tokens as 'Environment Variables' safely.

```
# load .env
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ["API_KEY"]
api_key_secret = os.environ["API_KEY_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]
```

## File Structure

```tree
Live-Twitter-Sentiment-Analysis
├── data
│   ├── chatwords.csv
│   └── smileys.csv
├── images
│   └── cover.png
├── Notebooks
│   ├── Sentiment_analysis.ipynb
│   └── stream_tweets_using_tweepy.ipynb
├── preprocessing
│   ├── chatwords_conversion.py
│   ├── correct_sentence_spelling.py
│   ├── lemmatizing.py
│   ├── remove_handle.py
│   ├── remove_html.py
│   ├── remove_non_ascii.py
│   ├── remove_punc.py
│   ├── remove_rt.py
│   ├── remove_url.py
│   ├── remove_whitespace.py
│   ├── replace_emoji.py
│   ├── stemming.py
│   └── word_tokenizer.py
├── requirements.txt
├── scrapping
│   ├── chatwords_conversion.py
│   ├── requirements.txt
│   ├── smileys_corresponding_text.py
│   ├── src
│   │   ├── app.py
│   │   ├── get_tweets.py
│   │   ├── pipline.py
│   │   └── sentiment_analysis.py
│   └── Visualization
│       ├── sentiment_pie.py
│       ├── top_tweet_bigrams.py
│       └── word_cloud.py
├── src
│   ├── app.py
│   ├── get_tweets.py
│   ├── pipline.py
│   └── sentiment_analysis.py
├── Untitled
└── Visualization
    ├── sentiment_pie.py
    ├── top_tweet_bigrams.py
    └── word_cloud.py

```


## Deploying Demo
[Live Twitter Sentiment Analysis Streamlit](https://mohamedsaadmoustafa-live-twitter-sentiment-analys-srcapp-6q068p.streamlitapp.com/)
