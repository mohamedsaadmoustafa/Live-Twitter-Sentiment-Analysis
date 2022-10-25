import tweepy
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
# load .env
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ["API_KEY"]
api_key_secret = os.environ["API_KEY_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

# Use the above credentials to authenticate the API.
auth = tweepy.OAuthHandler( api_key , api_key_secret )
auth.set_access_token( access_token , access_token_secret )
api = tweepy.API(auth)


def get_tweets(topic, count, save=True):
    columns = ["Date", "User", "IsVerified", "Tweet", "Likes", "RT", 'User_location']
    df = pd.DataFrame(columns=columns)

    cursor = tweepy.Cursor(
        api.search_tweets,
        q=topic,
        count=count,
        lang="en",
        exclude='retweets'
    ).items()

    for index, tweet in zip(range(count), cursor):
        print(index, end='\r')
        df.loc[index, "Date"] = tweet.created_at
        df.loc[index, "User"] = tweet.user.name
        df.loc[index, "IsVerified"] = tweet.user.verified
        df.loc[index, "Tweet"] = tweet.text
        df.loc[index, "Likes"] = tweet.favorite_count
        df.loc[index, "RT"] = tweet.retweet_count
        df.loc[index, "User_location"] = tweet.user.location

    if save:
        df.to_csv("TweetDataset.csv", index=False)

    return df

