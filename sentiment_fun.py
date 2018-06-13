import tweepy
from textblob import TextBlob

#get these 4 keys from your Twitter Developer account
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#retrieve tweets
public_tweets = api.search('BTS')

for tweet in public_tweets:
	print(tweet.text)
	#perform sentiment analysis on tweets
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	print("")