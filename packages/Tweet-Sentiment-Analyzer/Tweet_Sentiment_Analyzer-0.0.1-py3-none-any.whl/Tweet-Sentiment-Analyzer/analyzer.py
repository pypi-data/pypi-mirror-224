#!/usr/bin/env python3
import os
import tweepy
from dotenv import load_dotenv
from textblob import TextBlob

class TwitterSentimentAnalyzer:
    def __init__(self):
        # Load the stored environment variables
        load_dotenv()

        # Get the values
        api_key = os.getenv("api_key")
        api_secret = os.getenv("api_secret")
        access_token = os.getenv("access_token")
        access_token_secret = os.getenv("access_token_secret")

        # Authenticate with the Tweepy API
        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def analyze(self, query):
        # Search for tweets about any product
        tweets = tweepy.Cursor(
            self.api.search,
            q=query,
            count=100,
        ).items()

        # Analyze the sentiment of each tweet
        positive_tweets = [tweet for tweet in tweets if TextBlob(tweet.text).sentiment.polarity > 0]
        negative_tweets = [tweet for tweet in tweets if TextBlob(tweet.text).sentiment.polarity < 0]
        neutral_tweets = [tweet for tweet in tweets if TextBlob(tweet.text).sentiment.polarity == 0]

        # Return the results
        return {
            "positive": positive_tweets,
            "negative": negative_tweets,
            "neutral": neutral_tweets
        }

def main():
    analyzer = TwitterSentimentAnalyzer()
    results = analyzer.analyze("product name")

    # Print the results
    print("Number of positive tweets:", len(results["positive"]))
    print("Number of negative tweets:", len(results["negative"]))
    print("Number of neutral tweets:", len(results["neutral"]))

if __name__ == "__main__":
    main()
