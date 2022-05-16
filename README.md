
# Sentiment-analysis-with-Twitter-API

This project is a combination of several Libraries in python with the NPL

#### -- Project Status: [Completed]

## Project Intro/Objective
 To do Sentiment analysis for the input keyword on Twitter Api 


### Methods Used
* Inferential Statistics
* Machine Learning
* API call 

### Technologies
* Python
* Api


## Project Description
The purpose of this project is to get 2 word as input statement as keyword from user and we search the keyword in the twitter api then we clean the data after that we use some python linbarere to do sentiment analysis and get sentiment core and compire them.  

## Getting Started

1. Get access to the Twitter API [you can do that here](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

2. Get the api key, api key secret, access token and access token secret from the twitter developer website and put it in a [.ini] file.
```
[twitter]

api_key = Put your api key here
api_key_secret = Put your api key secret here

access_token = Put your access token here
access_token_secret = Put your access token secret here
```
    
3. Create a new [.py] and import the required Libraries
```
import tweepy
import configparser
import preprocessor as p
from textblob import TextBlob
import statistics
from typing import List
```

4. Use config library go get the access to api key, api key secret, access token and access token secret from [.ini] file. then put it in variable called api
```
config = configparser.ConfigParser()
config.read('apicon.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
```

5. Then get the tweets using this function with tweepy library in python 
```
def get_tweet(keyword:str)-> List[str]:
    all_tweets = []
    for tweet in tweepy.Cursor(api.search_tweets, q=keyword, tweet_mode = 'extended',lang='en').items(100):
        all_tweets.append(tweet.full_text)
    return all_tweets
```

6. Then clean the tweets using this function with preprocessor library in python.
```
def clean_tweet(all_tweets: List[str])-> List[str]:
    tweets_clean = []
    for tweet in all_tweets:
        tweets_clean.append(p.clean(tweet))
    return tweets_clean
```

7. Then use TextBlob library to do Sentiment analysis.
```
def get_sentiment(tweets_clean: List[str])-> List[float]:
    sentiment_scores = []
    for tweet in tweets_clean:
        blob = TextBlob(tweet)
        sentiment_scores.append(blob.sentiment.polarity)
        return sentiment_scores
```

8. Then use statistics library to find out Sentiment score of Sentiment analysis.
```
def get_avg_sentiment(keyword:str)-> int:
    tweets = get_tweet(keyword)
    tweets_clean= clean_tweet(tweets)
    sentiment_scores = get_sentiment(tweets_clean)
    average_score = statistics.mean(sentiment_scores)
    return average_score
```

9. Then use input() statement to get input from user and print the output.
```
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
```
8. Follow setup instructions [Get the files here](https://github.com/AbishekAsir/Sentiment-analysis-with-Twitter-API/blob/main/sentiment_analysis.py)

 

