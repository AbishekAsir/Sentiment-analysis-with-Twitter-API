import tweepy
import configparser
import pandas as pd
import preprocessor as p
from textblob import TextBlob
import statistics
from typing import List

# read configs
config = configparser.ConfigParser()
config.read('apicon.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def get_tweet(keyword:str)-> List[str]:
    all_tweets = []
    for tweet in tweepy.Cursor(api.search_tweets, q=keyword, tweet_mode = 'extended',lang='en').items(100):
        all_tweets.append(tweet.full_text)
    return all_tweets

def clean_tweet(all_tweets: List[str])-> List[str]:
    tweets_clean = []
    for tweet in all_tweets:
        tweets_clean.append(p.clean(tweet))
    return tweets_clean

def get_sentiment(tweets_clean: List[str])-> List[float]:
    sentiment_scores = []
    for tweet in tweets_clean:
        blob = TextBlob(tweet)
        sentiment_scores.append(blob.sentiment.polarity)
        return sentiment_scores

def get_avg_sentiment(keyword:str)-> int:
    tweets = get_tweet(keyword)
    tweets_clean= clean_tweet(tweets)
    sentiment_scores = get_sentiment(tweets_clean)
    average_score = statistics.mean(sentiment_scores)
    return average_score


if __name__ == "__main__":
    print("What world you like")
    first = input()
    print("----OR-----")
    second = input()
    print("\n")
    frist_score = get_avg_sentiment(first)
    second_score = get_avg_sentiment(second)
    if (frist_score > second_score):
        print("The world Prefer",first)
    else :
        print("The world Prefer",second)